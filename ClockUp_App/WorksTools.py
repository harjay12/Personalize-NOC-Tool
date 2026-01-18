# This Python file uses the following encoding: utf-8
"""
Important:
You need to run the following command to generate the ui_form.py file
     pyside6-uic form.ui -o ui_form.py, or
     pyside2-uic form.ui -o ui_form.py
"""
import re
import os
import sys
import time
import json
import psutil
import ahkFunc
import traceback
import ipaddress
import WorkToolFunc
from dotenv import *
import secretCompdetails
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from ui_form import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow


# Find the .env file
dotenv_path = find_dotenv(rf'c:\Users\{os.environ["username"]}\Documents\.env')
load_dotenv(dotenv_path)


ipBloks = {
    "": "",
    "/32 Single Block": 1,
    "/31 Block of 2*": 1,
    "/30 Block of 2": 2,
    "/29 Block of 5": 6,
    "/28 Block of 16": 14,
}
usableIP = []


class WorkerSignals(QObject):

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    bar_Progress = Signal(int)


class Worker_QRunnable(QRunnable):

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        # self.kwargs['progressCnt'] = self.signals.bar_Progress

    @Slot()
    def run(self):
        print("MyRunnable is running...")
        try:
            result = self.func(*self.args, **self.kwargs)  # Simulate some work

        except Exception:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()
        print("MyRunnable finished.")


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        # Ensure the window is customizable to allow flag changes
        self.setWindowFlag(Qt.CustomizeWindowHint, True)
        try:
            self.ui.comboBox.addItems([x for x in secretCompdetails.conductors])
            # print(self.ui.CCABBRcomboBox.setin(0))
            self.ui.CCABBRcomboBox.addItem("Select a carrier to call", 0)

            self.ui.CCABBRcomboBox.addItems(
                sorted([x.upper() for x in secretCompdetails.CarrierPH])
            )

            self.ui.Subnet_Box.addItems([blk for blk in ipBloks])
            self.ui.NipComboBox.addItems(["", "60", "100", "250", "Continuous Ping"])
            self.processList = []
            self.cliWidgesList = []
            self.statusLink = ""
            # self.phoneNm = ""
            self.msg_box = QMessageBox(
                QMessageBox.Information,
                # This title will not be displayed
                "Title (will be hidden)",
                "",
                QMessageBox.Ok,
                None,
                Qt.WindowType.FramelessWindowHint,
            )

            # ----------------Sign in/ out/ Lunch---------------
            self.ui.ClockInpushButton.clicked.connect(self.SignIn_Send)
            # ------------------CCA Sign i------------------------------------
            self.ui.CCA_pushButton.clicked.connect(self.CCA_Send)
            # ---------------------NOC Google Sheet status change IN------------------
            self.ui.Off_pushButton.clicked.connect(self.NOC_StatusBtns)
            self.ui.In_pushButton.clicked.connect(self.NOC_StatusBtns)
            self.ui.Break_pushButton.clicked.connect(self.NOC_StatusBtns)
            self.ui.Lunch_pushButton.clicked.connect(self.NOC_StatusBtns)
            self.ui.IW_pushButton.clicked.connect(self.NOC_StatusBtns)
            self.ui.Out_pushButton.clicked.connect(self.NOC_StatusBtns)
            self.ui.Training_pushButton.clicked.connect(self.NOC_StatusBtns)
            self.ui.InterEscal_pushButton.clicked.connect(self.NOC_StatusBtns)
            self.ui.CCABlock_pushButton.clicked.connect(self.NOC_StatusBtns)

            # ----------------------------Condustors--------------------------
            self.ui.comboBox.currentTextChanged.connect(self.conductors)
            self.ui.CCABBRcomboBox.currentTextChanged.connect(self.CarrierCalls)
            # -----------------------------CLI for ping initiate-----------------------
            self.ui.PingButton.clicked.connect(self.multi_Pages)
            # -------------------------------- Page navigation
            self.ui.Prev_pushButton.clicked.connect(self.go_to_previous_page)
            self.ui.Next_Button.clicked.connect(self.go_to_next_page)
            self.ui.Home_Button.clicked.connect(
                lambda: self.ui.stackedWidget.setCurrentIndex(0)
            )
            self.ui.stackedWidget.currentChanged.connect(self.changesPages)
            self.ui.CloseTab.clicked.connect(self.clear_stacked_widget)

            self.ui.End_Pings.clicked.connect(self.terminateSinglePing)
            self.ui.allEnd_Pings.clicked.connect(
                lambda: [p.kill() for p in self.processList]
            )

            self.ui.NSOID.setPlaceholderText("Enter the NSOID...")

            # Connect the textChanged signal to a slot
            self.ui.NSOID.returnPressed.connect(self.on_nsoidStr)

            self.timer = QTimer(self)
            self.timer.timeout.connect(self.show_time)
            self.timer.start()

            self.ui.Prev_pushButton.setVisible(False)
            self.ui.Home_Button.setVisible(False)
            self.ui.Next_Button.setVisible(False)
            self.ui.CloseTab.setVisible(False)
            self.ui.End_Pings.setVisible(False)
            self.ui.allEnd_Pings.setVisible(False)
            self.ui.NSOID.setVisible(False)
            self.ui.CCABBRcomboBox2.setVisible(False)
            self.ui.CCABBRcomboBox3.setVisible(False)

            self.threadpool = QThreadPool().globalInstance()

        except KeyboardInterrupt:
            pass

    # ---------------------------------------Current time function---------------------------------------------

    @Slot()
    def show_time(self):
        try:
            self.ui.dateTimeEdit.setDisplayFormat(f"MMMM/dd/yyyy hh:mm:ss AP")
            self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        except KeyboardInterrupt:
            pass

    # --------------------------------------- ahk Pid functions ---------------------------------------------

    def ahkOld_Pid(self):
        self.old_pids = [
            p.info["pid"]
            for p in psutil.process_iter(["pid", "name"])
            if p.info["name"] == "AutoHotkey64.exe"
        ]
        if not self.old_pids:
            self.old_pids = [-1]
        return self.old_pids

    # --------------------------------------- Threading functions ---------------------------------------------

    def ADP_executeTrhead(self):
        pidCheck = self.ahkOld_Pid()
        WorkToolFunc.ClockingIn()
        WorkToolFunc.kill_process(*pidCheck)
        return "Done."

    def CALLs_executeTrhead(self, phoneNm, pidCheck):
        ahkFunc.CCA_Calls(phoneNm)
        WorkToolFunc.kill_process(*pidCheck)
        time.sleep(3)
        return "Done."

    def CCA_executeTrhead(self, lunchBtn, pidCheck):

        if lunchBtn:
            ahkFunc.CCA_LogSentBreak()
        else:
            ahkFunc.CCA_LogSentIn()
        WorkToolFunc.kill_process(*pidCheck)
        return "Done."

    def GS_executeTrhead(self, btnVal):
        WorkToolFunc.GoogleSheetIn(shStatus=btnVal)
        return "Done."

    def Cond_executeTrhead_Func(self):
        pidCheck = self.ahkOld_Pid()
        win = WorkToolFunc.ahkExe_Path().active_window
        if win:
            win.move(
                x=win.get_position().x, y=win.get_position().y, width=1682, height=977
            )

            time.sleep(3)
            ahkFunc.runCund(
                userN=os.getenv("COND_USERNAME"), condPassW=os.getenv("CON_PASSW")
            )

            WorkToolFunc.kill_process(*pidCheck)
        return "Done."

    # --------------------------------------- Change page---------------------------------------------

    def changesPages(self):

        try:
            if self.ui.stackedWidget.currentIndex() == 0:
                self.ui.CloseTab.setText("Close All Tab")

                self.ui.stackedWidget.setGeometry(QRect(0, -10, 521, 461))

                self.ui.Prev_pushButton.setVisible(False)
                self.ui.Home_Button.setVisible(False)
                self.ui.Next_Button.setVisible(True)
                self.ui.End_Pings.setVisible(False)
                self.ui.allEnd_Pings.setVisible(False)
                self.ui.CloseTab.setVisible(True)

            elif (
                self.ui.stackedWidget.currentIndex()
                == self.ui.stackedWidget.count() - 1
            ):
                self.ui.Prev_pushButton.setVisible(True)
                self.ui.Home_Button.setVisible(True)
                self.ui.Next_Button.setVisible(False)
                self.ui.CloseTab.setVisible(True)
                self.ui.End_Pings.setVisible(True)
                self.ui.allEnd_Pings.setVisible(True)
                self.ui.stackedWidget.setGeometry(QRect(10, 0, 500, 400))

                self.ui.CloseTab.setText(
                    f"Close Tab: {self.ui.stackedWidget.currentIndex()}"
                )

            else:
                self.ui.Prev_pushButton.setVisible(True)
                self.ui.Home_Button.setVisible(True)
                self.ui.Next_Button.setVisible(True)
                self.ui.CloseTab.setVisible(True)
                self.ui.End_Pings.setVisible(True)
                self.ui.allEnd_Pings.setVisible(True)

                self.ui.stackedWidget.setGeometry(QRect(10, 0, 500, 400))
                self.ui.CloseTab.setText(
                    f"Close Tab: {self.ui.stackedWidget.currentIndex()}"
                )
        except BaseException as err:
            print(err)

    # ---------------------------------------Pagination function---------------------------------------------

    def go_to_previous_page(self):
        current_index = self.ui.stackedWidget.currentIndex()
        if current_index > 0:
            self.ui.stackedWidget.setCurrentIndex(current_index - 1)

    def go_to_next_page(self):
        current_index = self.ui.stackedWidget.currentIndex()
        if current_index < self.ui.stackedWidget.count() - 1:
            self.ui.stackedWidget.setCurrentIndex(current_index + 1)

    # ---------------------------------------Part of Run Ping function---------------------------------------------

    def multi_Pages(self):

        try:

            for pidProcess in self.processList:
                if self.process.state() == QProcess.Running:
                    pidProcess.kill()
                    self.process.waitForFinished(10)

            self.processList.clear()

            if self.ui.stackedWidget.count() > 1:
                while self.ui.stackedWidget.count() > 1:
                    widget = self.ui.stackedWidget.widget(1)
                    self.ui.stackedWidget.removeWidget(widget)
                    widget.deleteLater()  # Schedule for deletion

            GWIP = self.ui.GWIPlineEdit.text().replace(" ", "")

            is_ValidIP = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*", GWIP)
            if not is_ValidIP:
                self.msg_box.setText(
                    "The Gateway IP Address is not valid.\t"
                    "\nVerified you have entered a valid gateway IP address."
                )
                self.msg_box.exec()
                self.cliWidgesList.clear()
                usableIP.clear()
                self.ui.Next_Button.setVisible(False)
                self.ui.CloseTab.setVisible(False)

                return

            """ 
            ipLaststr = GWIP.split(".")[-1]
            neighborsIp = GWIP.replace(ipLaststr, str(int(ipLaststr) + i))

            if len(ipLaststr) == 1:
                neighborsIp = f"{GWIP[:-1]}{str(int(ipLaststr) + i)}"
            else:
                neighborsIp = GWIP.replace(ipLaststr, str(int(ipLaststr) + i))

            I needed to rework my approch o update he last IP octet. this time I shifted my focus on the last dot of he sr.
            At First I was converting tthe str to arr with the split func and was spliting with '.'
            Then get the last indes of the arr to get Usabe IPs and proceeded with replacing from orignal str.
            but with replace func it replaced al matches. But now I am ony replacing the last octet with usabe IP
            
            """

            # Find the last Dot in reverse built-in rfind python func.
            ipLstDt = GWIP.rfind(".")
            # Collect the last octet value excluding the dot.
            ipLstOctet = GWIP[ipLstDt + 1 : len(GWIP)]
            currentBlk = self.ui.Subnet_Box.currentText()

            for i in range(0, ipBloks[currentBlk]):

                neighborsIp = f"{GWIP[:ipLstDt+1]}{str(int(ipLstOctet) + i)}"

                print(neighborsIp)

                usableIP.append(neighborsIp)
                self.process = QProcess()
                self.cliWidges = CliWidget(self.ui.centralwidget, self.process)

                self.cliWidgesList.append(self.cliWidges)
                self.ui.stackedWidget.addWidget(self.cliWidges)
                self.processList.append(self.process)

            self.ui.stackedWidget.setCurrentIndex(1)  # Display the first page

            for ip in range(len(usableIP)):
                if self.ui.NipComboBox.currentText() == "Continuous Ping":
                    self.cliWidgesList[ip].start_cli_program(
                        "cmd.exe", ["/k", f"ping -t {usableIP[ip]}"]
                    )

                elif self.ui.NipComboBox.currentText() != "":
                    self.cliWidgesList[ip].start_cli_program(
                        "cmd.exe",
                        [
                            "/k",
                            f"ping -n {self.ui.NipComboBox.currentText()} {usableIP[ip]}",
                        ],
                    )

                else:
                    self.cliWidgesList[ip].start_cli_program(
                        "cmd.exe", ["/k", f"ping  {usableIP[ip]}"]
                    )

            self.cliWidgesList.clear()
            usableIP.clear()
        except BaseException as err:
            print(err)

    # ---------------------------------------Part of Ping Terminate function---------------------------------------------
    @Slot()
    def terminateSinglePing(self):

        try:
            if self.ui.stackedWidget.widget(self.ui.stackedWidget.currentIndex()):
                self.processList[self.ui.stackedWidget.currentIndex() - 1].kill()
                print("Stopping ping process...")

        except OSError as e:
            print(f"Error killing process: {e}")
            pass

        self.process.waitForFinished(100)

    # ---------------------------------------Part of Ping Clean function---------------------------------------------

    def clear_stacked_widget(self):
        """
        Removes all widgets from a QStackedWidget and schedules them for deletion.
        """

        try:
            if self.ui.stackedWidget.currentIndex() != 0:

                widget = self.ui.stackedWidget.widget(
                    self.ui.stackedWidget.currentIndex()
                )
                self.ui.stackedWidget.removeWidget(widget)
                widget.deleteLater()  # Schedule for deletion
                if self.ui.stackedWidget.count() == 1:
                    self.ui.Prev_pushButton.setVisible(False)
                    self.ui.Home_Button.setVisible(False)
                    self.ui.Next_Button.setVisible(False)
                    self.ui.CloseTab.setVisible(False)

            else:
                self.ui.Prev_pushButton.setVisible(False)
                self.ui.Home_Button.setVisible(False)
                self.ui.Next_Button.setVisible(False)
                self.ui.CloseTab.setVisible(False)

                while self.ui.stackedWidget.count() > 1:
                    # Get the widget at index 0
                    widget = self.ui.stackedWidget.widget(1)
                    # Remove it from the stacked widget
                    self.ui.stackedWidget.removeWidget(widget)
                    widget.deleteLater()  # Schedule for deletion

        except BaseException as err:
            print(err)

    # ---------------------------------------ADP Function form---------------------------------------------

    def SignIn_Send(self):
        if self.ui.checkBox.isChecked():
            print("yes")
        filvar = f'{{"ADP_USERNAME":"{self.ui.UserNmtextEdit.text()}",\
            "ADP_PASSW":"{self.ui.PassWtextEdit.text()}"}}'
        filvar = json.loads(filvar)

        for key, value in filvar.items():
            if (
                not os.path.exists(rf'c:\Users\{os.environ["username"]}\Documents\.env')
                or os.getenv(key) is None
                or os.getenv(key) == ""
            ) and value == "":
                self.msg_box.setText(
                    f"Fill out the {self.ui.UserNmlabel.text()} and {self.ui.PassWlabel.text()}"
                )
                self.msg_box.exec()
                return

        self.gui_InputSetup(filvar)

        load_dotenv(dotenv_path, override=True)

        WorkToolFunc.UserName = f"{os.getenv('ADP_USERNAME')}"
        WorkToolFunc.PassWord = f"{os.getenv('ADP_PASSW')}"

        self.With_worker = Worker_QRunnable(self.ADP_executeTrhead)
        self.threadpool.start(self.With_worker)

    # ---------------------------------------GUI Function CCA---------------------------------------------

    def CCA_Send(self):
        pidCheck = self.ahkOld_Pid()
        if not os.path.exists(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Call Center Agent.lnk"
        ):
            self.msg_box.setText(
                "The CCA App is not installed to this computer.\t"
                "\nCheck with IT to have CCA installed."
            )
            self.msg_box.exec()
            return

        self.msgBox = QMessageBox()

        self.msgBox.setWindowTitle("CCA Access! ")
        self.msgBox.setText("\tDo you want to log in or log out of CCA?\t\t")

        yes_button = self.msgBox.addButton("Log To CCA", QMessageBox.YesRole)
        no_button = self.msgBox.addButton("Exit CCA", QMessageBox.NoRole)
        cancel = self.msgBox.addButton("", QMessageBox.RejectRole)
        cancel.hide()
        self.msgBox.exec()

        if self.msgBox.clickedButton() == yes_button:

            win = ""

            if WorkToolFunc.ahkExe_Path().win_exists("ahk_exe CCA.exe"):
                win = WorkToolFunc.ahkExe_Path().find_window(
                    title="My Contact Center Agent"
                )
                win.activate()

            else:
                WorkToolFunc.ahkExe_Path().run_script(f"Run {WorkToolFunc.cca_Path()}")
                time.sleep(1)
                win = WorkToolFunc.ahkExe_Path().active_window

            if win.title == "My Contact Center Agent":
                self.With_worker = Worker_QRunnable(
                    self.CCA_executeTrhead, "", pidCheck
                )
                self.threadpool.start(self.With_worker)

        elif self.msgBox.clickedButton() == no_button:

            if WorkToolFunc.ahkExe_Path().win_exists("ahk_exe CCA.exe"):
                WorkToolFunc.ahkExe_Path().win_close("ahk_exe CCA.exe")
                win = WorkToolFunc.ahkExe_Path().find_window(title="Confirmation")
                win.activate()
                win.send("{Enter}")

            else:
                self.msg_box.setText("The Window not found. CCA was nerver open.\t")
                self.msg_box.exec()
                print("Window not found. Try to sign in first.")
            WorkToolFunc.kill_process(*pidCheck)

        else:
            print("Nonee")

    # ---------------------------------------Google Sign in Sheet---------------------------------------------

    def gui_InputSetup(self, guiParams={}):
        if not os.path.exists(rf'c:\Users\{os.environ["username"]}\Documents\.env'):
            WorkToolFunc.dotEnv_File(guiParams)

        else:
            for key, value in guiParams.items():
                if os.getenv(key) is None:
                    with open(dotenv_path, "a") as f:
                        f.write(f"\n{key}='{value}'")
                elif os.getenv(key) == "":
                    set_key(dotenv_path, f"{key}", f"{value}")

        return

    def NOC_StatusBtns(self):
        pidCheck = self.ahkOld_Pid()

        filvar = f'{{"NOCGSH":"{self.ui.UserNmtextEdit.text()}"}}'
        filvar = json.loads(filvar)

        for key, value in filvar.items():
            if (
                not os.path.exists(rf'c:\Users\{os.environ["username"]}\Documents\.env')
                or os.getenv(key) is None
                or os.getenv(key) == ""
            ) and value == "":
                self.msg_box.setText(
                    "Fill out User Name as it shows in \n"
                    "NOC Department Status Document Google sheet"
                )
                self.msg_box.exec()
                return

        self.gui_InputSetup(filvar)

        load_dotenv(dotenv_path, override=True)

        sender_button = self.sender()  # Get the object that emitted the signal
        btnList = {
            "Off_pushButton": "Off",
            "In_pushButton": "In",
            "Break_pushButton": "Break",
            "Out_pushButton": "Out",
            "Lunch_pushButton": "Lunch",
            "IW_pushButton": "Extended NI",
            "Training_pushButton": "Training",
            "InterEscal_pushButton": "Internal Escalations",
            "CCABlock_pushButton": "CCA Call Block",
        }
        try:
            for btnKey, btnVal in btnList.items():
                if sender_button.objectName() == btnKey:
                    self.With_worker = Worker_QRunnable(self.GS_executeTrhead, btnVal)
                    self.threadpool.start(self.With_worker)

            if sender_button.objectName() == "Lunch_pushButton":
                self.With_worker = Worker_QRunnable(
                    self.CCA_executeTrhead, sender_button.objectName(), pidCheck
                )
                self.threadpool.start(self.With_worker)

        except BaseException as e:

            if "object has no attribute 'row'" in str(e):
                self.msg_box.setText(
                    "Fill out User Name as it shows in \n"
                    "NOC Department Status Document Google sheet"
                )
                set_key(dotenv_path, "NOCGSH", self.ui.UserNmtextEdit.text())
                load_dotenv(dotenv_path, override=True)
            else:
                self.msg_box.setText(f"An Error Occur: {e}")
            self.msg_box.exec()

    """ ---------------------------------------GUI Function Cond---------------------------------------------"""

    def conductors(self):
        self.statusLink = self.ui.comboBox.currentText()
        self.ui.NSOID.setVisible(True)
        self.ui.comboBox.setVisible(False)

    def on_nsoidStr(self):

        nsoidStr = self.ui.NSOID.text()
        bxInput = {
            "COND_USERNAME": "Enter your Conductor User ID",
            "CON_PASSW": "Enter your Conductor Password",
        }
        WorkToolFunc.custmInputBox_Func(bxInput, "Conductors Sign In")
        load_dotenv(dotenv_path, override=True)

        if nsoidStr.startswith("CPEGRT"):
            WorkToolFunc.ahkExe_Path().run_script(
                f'Run "{secretCompdetails.conductors[self.statusLink]}routers/{nsoidStr}"'
            )

        else:
            WorkToolFunc.ahkExe_Path().run_script(
                f'Run "{secretCompdetails.conductors[self.statusLink]}"'
            )
            time.sleep(2.5)

        self.With_worker = Worker_QRunnable(self.Cond_executeTrhead_Func)
        self.threadpool.start(self.With_worker)

        time.sleep(1)
        QTimer().singleShot(100, self.nsoID_Vis)
        self.ui.NSOID.clear()
        self.ui.comboBox.setCurrentIndex(0)

    def nsoID_Vis(self):
        self.ui.NSOID.setVisible(False)
        time.sleep(2)
        self.ui.comboBox.setVisible(True)

    """---------------------------------------CCA Carrier Calls---------------------------------------------"""

    def CarrierCalls(self):
        pidCheck = self.ahkOld_Pid()
        self.phoneNm = self.ui.CCABBRcomboBox.currentText()
        if not os.path.exists(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Call Center Agent.lnk"
        ):
            if self.ui.CCABBRcomboBox.currentIndex() != 0:

                self.msg_box.setText(
                    "The CCA App is not installed to this computer.\t"
                    "\nCheck with IT to have CCA installed."
                )

                self.msg_box.exec()
            self.ui.CCABBRcomboBox.setCurrentIndex(0)

            return

        if self.ui.CCABBRcomboBox.currentIndex() != 0:
            num = secretCompdetails.CarrierPH[self.phoneNm.lower()]
            self.With_worker = Worker_QRunnable(self.CALLs_executeTrhead, num, pidCheck)
            self.threadpool.start(self.With_worker)

        self.ui.CCABBRcomboBox.setCurrentIndex(0)

    def closeEvent(self, event: QCloseEvent):
        try:
            for pidProcess in self.processList:
                if self.process.state() == QProcess.Running:
                    pidProcess.kill()
                    self.process.waitForFinished(50)

        except AttributeError:
            pass


class CliWidget(QWidget):
    def __init__(self, parent=None, args=None):
        super().__init__(parent)

        self.text_output = QTextEdit()
        self.process = args
        self.layout = QVBoxLayout()
        self.ping_times = []
        self.timesOut = []

        self.text_output.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-family: Verdana, Arial, Helvetica, sans-serif;\n"
            "font-size: 13px;\n"
            "font-style: normal;\n"
            "font-variant: normal;\n"
            "font-weight: normal;\n"
            "border-radius: 5px;"
        )

        self.layout.addWidget(self.text_output)

        self.setLayout(self.layout)

        # Connect signals
        self.process.readyReadStandardOutput.connect(self.read_output)
        self.process.readyReadStandardError.connect(self.read_error)
        self.process.finished.connect(self.handle_finished)

    @Slot()
    def start_cli_program(self, program, param):
        print(f"Starting: {program} {param}")
        self.process.start(program, param)

    @Slot()
    def read_output(self):
        data = self.process.readAllStandardOutput().data().decode().strip()
        if data:
            self.text_output.append(data)
            self.parse_ping_times(data)

    @Slot()
    def read_error(self):
        data = self.process.readAllStandardError().data().decode().strip()
        self.text_output.append(f"ERROR: {data}")

    @Slot()
    def handle_finished(self, exitCode, exitStatus):

        print(f"Process finished with exit code {exitCode} and status {exitStatus}")

        pingMatch = re.search(
            r"(?=.*data)(?=.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})).*",
            self.text_output.toPlainText(),
            flags=re.IGNORECASE,
        )

        if self.ping_times or self.timesOut:
            stattsVal = re.search(
                r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*",
                pingMatch[0],
                flags=re.IGNORECASE,
            ).group(1)
            if len(self.timesOut) >= 1:
                drpStr = ""

                if len(self.ping_times) == 0:

                    drpStr = (
                        f"\nPing statistics for {stattsVal}:\n"
                        f"     Packets: Sent = {len(self.timesOut)}, Received = {len(self.ping_times)}, "
                        f"Lost = {len(self.timesOut)} (100% loss)\n"
                    )
                self.text_output.append(drpStr)

            if len(self.ping_times) >= 1:
                perDrop = 0
                min_ms = min(self.ping_times)
                max_ms = max(self.ping_times)
                avg_ms = sum(self.ping_times) / len(self.ping_times)
                count = len(self.ping_times)
                pSent = count + len(self.timesOut)
                if len(self.timesOut) >= 1:
                    perDrop = round(((len(self.timesOut) / pSent) * 100))

                stats_text = (
                    f"\nPing statistics for {stattsVal}:"
                    f"\n    Packets: Sent = {pSent}, received = {count}, "
                    f"Lost = {len(self.timesOut)} ({perDrop}% loss)\n"
                    f"Approximate round trip times in milli-seconds:"
                    f"\n    Min = {min_ms:.2f} ms, Avg = {avg_ms:.2f} ms, Max = {max_ms:.2f} ms \n"
                )
                self.text_output.append(stats_text)

        self.text_output.append(
            f"Process finished with exit code {exitCode} and status {exitStatus} (1=Crashed, 0=Normal).\n"
        )

    def parse_ping_times(self, output):
        # Use regex to extract time in ms from ping output lines
        # Windows example line: "Reply from 142.250.186.78: bytes=32 time=25ms TTL=117"
        # Linux example line: "64 bytes from 142.250.186.78: icmp_seq=1 ttl=117 time=25.1 ms"
        match = re.search(r"time=(\d+)\s*ms", output)
        match1 = re.search(r"time<1ms", output)
        match2 = re.search(r"timed\s*out.|unreachable.|General failure.", output)

        try:
            if match:
                self.ping_times.append(float(match.group(1)))
            elif match1:
                self.ping_times.append(0)
            elif match2:
                self.timesOut.append(str(match2))
        except ValueError:
            print("error found!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
