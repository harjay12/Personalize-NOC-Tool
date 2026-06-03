import os 
import sys 
import asyncio 
from dotenv import *
import assemblyai as aai 
from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from assemblyai.streaming.v3 import StreamingClient, StreamingClientOptions, StreamingParameters, StreamingEvents

dotenv_path = find_dotenv(rf'c:\Users\{os.environ["username"]}\Documents\.env')
load_dotenv(dotenv_path)

# Configure your API key
aai.settings.api_key = os.getenv("ASSEMBLY_KEY")


class TranscriptionWorker(QThread):
    """
    Worker thread that handles PyAudio microphone reading and AssemblyAI streaming 
    without blocking the PySide6 UI.
    """
    status_signal = Signal(str)
    partial_transcript_signal = Signal(str)
    final_transcript_signal = Signal(str, str) # (Speaker, Text)
    error_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.loop = None
        self.client = None

    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        try:
            self.loop.run_until_complete(self.start_streaming())
        except Exception as e:
            self.error_signal.emit(str(e))
        finally:
            self.loop.close()

    async def start_streaming(self):
        options = StreamingClientOptions(
            api_key=aai.settings.api_key,
            api_host="streaming.assemblyai.com"
        )
        self.client = StreamingClient(options)
        self.client.on(StreamingEvents.Begin, self.on_begin)
        self.client.on(StreamingEvents.Turn, self.on_turn)
        self.client.on(StreamingEvents.Error, self.on_error)

        params = StreamingParameters(
            speech_model="u3-rt-pro",
            sample_rate=16000,
            format_turns=True,
            min_turn_silence=100,
            max_turn_silence=1200,
            max_speakers=2
        )
        try:
            self.client.connect(params)
            self.client.stream(aai.extras.MicrophoneStream(sample_rate=16000))
        except KeyboardInterrupt:
            print("\n\nStopping...")
        finally:
            self.client.disconnect(terminate=True)

    def on_begin(self, client, event):
        self.status_signal.emit("🔴 Recording Live (Listening...)")

    def on_turn(self, client, event):
        if event.end_of_turn:
            self.final_transcript_signal.emit(str(event.speaker_label), event.transcript)
        else:
            self.partial_transcript_signal.emit(event.transcript)

    def on_error(self, client, error):
        self.error_signal.emit(str(error))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live Transcription & Diarization")
        self.resize(650, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.status_label = QLabel("Status: Idle")
        self.status_label.setStyleSheet("font-weight: bold; color: gray;")
        self.layout.addWidget(self.status_label)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setPlaceholderText("Transcripts will appear here in real-time...")
        self.text_area.setStyleSheet("font-family: Consolas, Monaco, monospace; font-size: 13px;")
        self.layout.addWidget(self.text_area)

        self.toggle_button = QPushButton("Start Recording")
        self.toggle_button.setStyleSheet("background-color: #2ecc71; color: white; font-size: 14px; padding: 10px; font-weight: bold; border-radius: 4px;")
        self.toggle_button.clicked.connect(self.handle_toggle)
        self.layout.addWidget(self.toggle_button)

        self.worker = None
        self.finalized_html = "" # Visual Fix: Keeps track of locked text blocks cleanly

    def handle_toggle(self):
        if self.worker and self.worker.isRunning():
            # Your original working stop mechanism
            self.status_label.setText("Stopping stream, finishing final sentences...")
            self.toggle_button.setEnabled(False)
            self.worker.client.disconnect(terminate=True)
            self.toggle_button.setText("Start Recording")
            self.toggle_button.setStyleSheet("background-color: #2ecc71; color: white; font-size: 14px; padding: 10px; font-weight: bold; border-radius: 4px;")
            self.toggle_button.setEnabled(True)
        else:
            if not aai.settings.api_key:
                self.text_area.setHtml("<span style='color: #e74c3c; font-weight: bold;'>⚠️ ERROR: API Key missing from .env</span>")
                return

            self.worker = TranscriptionWorker()
            self.worker.status_signal.connect(self.update_status)
            self.worker.partial_transcript_signal.connect(self.update_partial)
            self.worker.final_transcript_signal.connect(self.update_final)
            self.worker.error_signal.connect(self.handle_error)
            
            self.worker.start()
            self.toggle_button.setText("Stop Recording")
            self.toggle_button.setStyleSheet("background-color: #e74c3c; color: white; font-size: 14px; padding: 10px; font-weight: bold; border-radius: 4px;")

    @Slot(str)
    def update_status(self, text):
        self.status_label.setText(f"Status: {text}")

    @Slot(str)
    def update_partial(self, text):
        if text.strip():
            partial_html = f"{self.finalized_html}<p style='color: #7f8c8d; font-style: italic; margin-top: 5px;'>💬 Hearing: {text}</p>"
            self.text_area.setHtml(partial_html)
            self.text_area.ensureCursorVisible()

    @Slot(str, str)
    def update_final(self, speaker, text):
        color = "#2980b9" if speaker == "A" else "#27ae60"
        formatted_line = f"<p style='margin-bottom: 8px;'><b style='color: {color};'>[Speaker {speaker}]:</b> {text}</p>"
        
        self.finalized_html += formatted_line
        self.text_area.setHtml(self.finalized_html)
        self.text_area.ensureCursorVisible()

    @Slot(str)
    def handle_error(self, error_msg):
        self.status_label.setText("Status: Error Occurred.")
        self.text_area.append(f"<p style='color: #c0392b; font-weight: bold;'>❌ Error: {error_msg}</p>")
        self.status_label.setText("Status: Idle")
        self.toggle_button.setText("Start Recording")
        self.toggle_button.setStyleSheet("background-color: #2ecc71; color: white; font-size: 14px; padding: 10px; font-weight: bold; border-radius: 4px;")

    def closeEvent(self, event):
        if self.worker and self.worker.isRunning():
            self.worker.client.disconnect(terminate=True)
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())