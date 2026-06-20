
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
import requests
import pgeocode
import subprocess
import speechToText
import traceback
import googlemaps
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

ipv4_REGEX = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*"
url_REGEX = r"^(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{2,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
regexIPV6_V4 = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*|(\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b|\b(?:[0-9a-fA-F]{1,4}:){1,7}:\b|\b(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}\b|\b(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}\b|\b(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}\b|\b(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}\b|\b(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}\b|\b[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}\b|\b:(?::[0-9a-fA-F]{1,4}){1,7}\b|::).*|(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*"

ipBloks = {
    "": "",
    "/32 Single Block": 1,
    "/31 Block of 2*": 1,
    "/30 Block of 2": 2,
    "/29 Block of 5": 6,
    "/28 Block of 16": 14,
    "Trace Route": 1,
}
usableIP = []

clor = [
    "",
    "rgb(181, 181, 181)",
    "rgb(16, 255, 136)",
    "rgb(229, 204, 102)",
    "rgb(229, 204, 102)",
    "rgb(98, 42, 166)",
    "rgb(230, 147, 46)",
    "rgb(21, 60, 186)",
    "rgb(86, 126, 116)",
    "rgb(255, 53, 35)",
    "rgb(154,80,0)",
]

class WorkerSignals(QObject):

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    bar_Progress = Signal(int)


class Worker_QRunnable(QRunnable):

    def __init__(self, func, *args):
        super().__init__()
        self.func = func
        self.args = args
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        print("MyRunnable is running...")
        try:
            result = self.func(*self.args)  # Simulate some work

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
        self.resize(621, 468)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        # Ensure the window is customizable to allow flag changes
        self.setWindowFlag(Qt.CustomizeWindowHint, True)
        self.second_window = None
        self.ui.speechToTextBnt.clicked.connect(self.open_new_window)
     
        self.ui.comboBox.addItems([x for x in secretCompdetails.conductors])
        # print(self.ui.CCABBRcomboBox.setin(0))
        self.ui.CCABBRcomboBox.addItem("Select a carrier to call", 0)

        self.ui.CCABBRcomboBox.addItems(
            sorted([x.upper() for x in secretCompdetails.CarrierPH])
        )

        self.ui.Subnet_Box.addItems([blk for blk in ipBloks])
        self.ui.NipComboBox.addItems(["", "60", "100", "250", "Continuous Ping"])
        # GoogleSheetIn(shCol='P7')
        self.ui.gspreadComboBox.addItem("NOC Status", 0)

        if os.getenv('SHT_KEY'):
            self.ui.gspreadComboBox.addItems(WorkToolFunc.GoogleSheetIn(shCol="P7"))
            self.ui.gspreadComboBox.currentTextChanged.connect(self.NOC_StatusBtns)
        else:
            self.ui.gspreadComboBox.addItems(["Add Sheet ID"])
            self.ui.gspreadComboBox.currentTextChanged.connect(self.gsht_Status)

        self.processList = []

        self.cliWidgesList = []
        self.statusLink = ""
        self.inputCode = ''

        self.msg_box = QMessageBox(
            QMessageBox.Information,
            # This title will not be displayed
            "Title (will be hidden)",
            "",
            QMessageBox.Ok,
            None,
            Qt.WindowType.FramelessWindowHint,
        )
        self.DropDwnStyle()
        self.flexBtnisOn = False

        # ----------------Sign in/ out/ Lunch---------------
        self.ui.ClockInpushButton.clicked.connect(self.SignIn_Send)
        # ------------------CCA Sign i------------------------------------
        self.ui.CCA_pushButton.clicked.connect(self.CCA_Send)
        # ---------------------NOC Google Sheet status change IN------------------
        self.ui.CreateIW_pushBtn.clicked.connect(self.Creat_IW)
        self.ui.FedgeLookUp.clicked.connect(self.flexFun)

        # ----------------------------Condustors--------------------------
        self.ui.comboBox.currentTextChanged.connect(self.conductors)
        self.ui.CCABBRcomboBox.currentTextChanged.connect(self.CarrierCalls)
        # -----------------------------CLI for ping initiate-----------------------
        self.ui.PingButton.clicked.connect(self.multi_Pages)
        # -------------------------------- Page navigation
        self.ui.Prev_pushBtn.clicked.connect(self.go_to_previous_page)
        self.ui.Next_pushBtn.clicked.connect(self.go_to_next_page)
        self.ui.Home_pushBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.ui.stackedWidget.currentChanged.connect(self.changesPages)
        self.ui.Close_pushBtn.clicked.connect(self.clear_stacked_widget)

        self.ui.endPing_pushBtn.clicked.connect(self.terminateSinglePing)
        self.ui.endAllPing_pushBtn.clicked.connect(
            lambda: [p.kill() for p in self.processList]
        )

        self.ui.NSOID.setPlaceholderText("Enter the NSOID...")

        # Connect the textChanged signal to a slot
        self.ui.NSOID.returnPressed.connect(self.on_nsoidStr)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start()

        self.ui.Prev_pushBtn.setVisible(False)
        self.ui.Home_pushBtn.setVisible(False)
        self.ui.Next_pushBtn.setVisible(False)
        self.ui.Close_pushBtn.setVisible(False)
        self.ui.endPing_pushBtn.setVisible(False)
        self.ui.endAllPing_pushBtn.setVisible(False)
        self.ui.NSOID.setVisible(False)

        self.threadpool = QThreadPool().globalInstance()


    def open_new_window(self):
        # Check if the window is already open to prevent duplicate windows
        if self.second_window is None:
            self.second_window = speechToText.TextDisplayWindow()
        
        self.second_window.show()

    # ---------------------------------------Current time function---------------------------------------------

    @Slot()
    def show_time(self):
        try:
            self.ui.dateTimeEdit.setDisplayFormat(f"MMMM/dd/yyyy hh:mm:ss AP")
            self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        except KeyboardInterrupt:
            pass


    def gsht_Status(self):
        bxInput = {"SHT_KEY": "Enter The NOC Sheet Key", }

        if self.ui.gspreadComboBox.currentText() == "Add Sheet ID":
            shtSetin = WorkToolFunc.custmInputBox_Func(bxInput, "Add the NOC Google sheet key.")
            if shtSetin:
                self.ui.gspreadComboBox.clear()
                self.ui.gspreadComboBox.addItem("NOC Status", 0)
                self.ui.gspreadComboBox.addItems(WorkToolFunc.GoogleSheetIn(shCol="P7"))
                self.ui.gspreadComboBox.currentTextChanged.connect(self.NOC_StatusBtns)
                return
            self.ui.gspreadComboBox.setCurrentIndex(0)


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
        StasUp = WorkToolFunc.GoogleSheetIn()
        if self.ui.gspreadComboBox.findText(StasUp):
            self.ui.gspreadComboBox.setCurrentText(StasUp)
        else:
            self.ui.gspreadComboBox.setCurrentIndex(0)
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
                userN=os.getenv("COND_USERNAME"), condPassW=f'{os.getenv("CON_PASSW")},{self.inputCode}'
            )

            WorkToolFunc.kill_process(*pidCheck)
        return "Done."

   

#----------------------------------------------------------------------------
    def flexFun(self,):
        flexArr = (self.threadpool,self.ui.stackedWidget)
        FlexEdgeLookUpObj = FlexEdgeookUp(self.ui.centralwidget,flexArr)
       
        if not self.flexBtnisOn:
            while self.ui.stackedWidget.count() > 1:
                    widget = self.ui.stackedWidget.widget(1)
                    self.ui.stackedWidget.removeWidget(widget)
                    widget.deleteLater()  # Schedule for deletion

        FlexEdgeLookUpObj.edComboBox.currentTextChanged.connect(lambda: self.Flex_combosetup(FlexEdgeLookUpObj))
        
        self.ui.stackedWidget.addWidget(FlexEdgeLookUpObj)
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.count() - 1)  # Display the first page
        self.flexBtnisOn = True
     
        self.ui.endPing_pushBtn.setVisible(False)
        self.ui.endAllPing_pushBtn.setVisible(False)

 
    def Flex_combosetup(self,FlexEdgeLookUpObj):
        flexArr = (self.threadpool,self.ui.stackedWidget)
        temp = FlexEdgeookUp(self.ui.centralwidget,flexArr)
        if self.ui.stackedWidget.count() - 1 < 2:
            if (FlexEdgeLookUpObj.edComboBox.currentText() == 'ED Standdard'
                and self.ui.stackedWidget.currentIndex() == 1):
                FlexEdgeLookUpObj.edComboBox.setCurrentIndex(0)
                self.ui.stackedWidget.addWidget(temp)
                temp.edComboBox.setCurrentIndex(1)
                temp.condPushBtn.setVisible(False)
                temp.text_outputF.clear()
                temp.text_outputF.append(f'{temp.startScreen1}')
            
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.count() - 1)  # Display the first page


    # -------------------------------IW Create---------------------------

    def Creat_IW(self):
        if not self.flexBtnisOn:
            while self.ui.stackedWidget.count() > 1:
                    widget = self.ui.stackedWidget.widget(1)
                    self.ui.stackedWidget.removeWidget(widget)
                    widget.deleteLater()  # Schedule for deletion

        self.ui.stackedWidget.addWidget(Create_IW(self.ui.centralwidget))
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.count() - 1)
        self.flexBtnisOn = True

        self.ui.endPing_pushBtn.setVisible(False)
        self.ui.endAllPing_pushBtn.setVisible(False)

    # --------------------------------------- Change page---------------------------------------------

    def changesPages(self):

        try:
                    
            if self.ui.stackedWidget.currentIndex() == 0:
                self.ui.Close_pushBtn.setText("Close All Tab")

                self.resize(621, 468)

                self.ui.Prev_pushBtn.setVisible(False)
                self.ui.Home_pushBtn.setVisible(False)
                self.ui.Next_pushBtn.setVisible(True)
                self.ui.endPing_pushBtn.setVisible(False)
                self.ui.endAllPing_pushBtn.setVisible(False)
                self.ui.Close_pushBtn.setVisible(True)

            elif (
                self.ui.stackedWidget.currentIndex()
                == self.ui.stackedWidget.count() - 1
            ):
                self.ui.Prev_pushBtn.setVisible(True)
                self.ui.Home_pushBtn.setVisible(True)
                self.ui.Next_pushBtn.setVisible(False)
                self.ui.Close_pushBtn.setVisible(True)
                self.ui.endPing_pushBtn.setVisible(True)
                self.ui.endAllPing_pushBtn.setVisible(True)

                self.ui.Close_pushBtn.setText(
                    f"Close Tab: {self.ui.stackedWidget.currentIndex()}"
                )

            else:
                self.ui.Prev_pushBtn.setVisible(True)
                self.ui.Home_pushBtn.setVisible(True)
                self.ui.Next_pushBtn.setVisible(True)
                self.ui.Close_pushBtn.setVisible(True)
                self.ui.endPing_pushBtn.setVisible(True)
                self.ui.endAllPing_pushBtn.setVisible(True)

                self.ui.Close_pushBtn.setText(
                    f"Close Tab: {self.ui.stackedWidget.currentIndex()}"
                )
            if self.flexBtnisOn or self.ui.FedgeLookUp.isChecked():
        
                    self.ui.endPing_pushBtn.setVisible(False)
                    self.ui.endAllPing_pushBtn.setVisible(False)

            
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
        self.flexBtnisOn = False

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

            is_ValidIP = bool(re.search(ipv4_REGEX, GWIP))
            is_ValidURL = bool(re.search(url_REGEX, GWIP))

            """ 
            ipLaststr = GWIP.split(".")[-1]
            neighborsIp = GWIP.replace(ipLaststr, str(int(ipLaststr) + i))

            if len(ipLaststr) == 1:
                neighborsIp = f"{GWIP[:-1]}{str(int(ipLaststr) + i)}"
            else:
                neighborsIp = GWIP.replace(ipLaststr, str(int(ipLaststr) + i))

            I needed to rework my approch to update the last IP octet to ping usabe IPs. This time I shifted my focus on the last dot from the IP input str.
            At First I was converting the str to arr with the split built-in func and was spliting with '.'
            Then get the last arr index to get Usabe IPs and proceeded with replacing last arr index with coverted last index.
            But with replace func it replaced all possible matches. But now I am ony replacing the last octet with usabe IP.

            The if statement worked but i was not to happy about it.
            
            """

            # Find the last Dot in reverse built-in rfind python func.
            ipLstDt = GWIP.rfind(".")
            # Collect the last octet value excluding the dot.
            ipLstOctet = GWIP[ipLstDt + 1 : len(GWIP)]
            currentBlk = self.ui.Subnet_Box.currentText()

            for i in range(0, ipBloks[currentBlk]):

                # usableIP.append(neighborsIp)
                self.process = QProcess()
                self.cliWidges = CliWidget(self.ui.centralwidget, self.process)

                self.cliWidgesList.append(self.cliWidges)
                self.ui.stackedWidget.addWidget(self.cliWidges)
                self.processList.append(self.process)
                if is_ValidURL:
                    usableIP.append(GWIP) 
                    break
                elif is_ValidIP:
                    neighborsIp = f"{GWIP[:ipLstDt+1]}{str(int(ipLstOctet) + i)}"
                    usableIP.append(neighborsIp)

                else:
                    self.msg_box.setText(
                    "The Gateway IP Address or the URL is not valid.\t"
                    "\nVerified you have entered a valid gateway IP address or a valid URL.")
                    self.msg_box.exec()
                    self.cliWidgesList.clear()
                    usableIP.clear()
                    self.ui.Next_pushBtn.setVisible(False)
                    self.ui.Close_pushBtn.setVisible(False)

                    return
                    
            self.ui.stackedWidget.setCurrentIndex(1)  # Display the first page
            if self.ui.Subnet_Box.currentText() == "Trace Route":
                self.cliWidgesList[0].start_cli_program(
                            "cmd.exe", ["/k", f"tracert {usableIP[0]}"]
                        )
            else:

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
                    self.ui.Prev_pushBtn.setVisible(False)
                    self.ui.Home_pushBtn.setVisible(False)
                    self.ui.Next_pushBtn.setVisible(False)
                    self.ui.Close_pushBtn.setVisible(False)

            else:
                self.ui.Prev_pushBtn.setVisible(False)
                self.ui.Home_pushBtn.setVisible(False)
                self.ui.Next_pushBtn.setVisible(False)
                self.ui.Close_pushBtn.setVisible(False)

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
            print("None")

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

        try:
            if self.ui.gspreadComboBox.currentIndex() != 0:
                currentstatus = self.ui.gspreadComboBox.currentText()
                if currentstatus:

                    print(currentstatus)

                    self.With_worker = Worker_QRunnable(
                        self.GS_executeTrhead, currentstatus
                    )
                    self.threadpool.start(self.With_worker)

                    if currentstatus == "Lunch":

                        self.With_worker = Worker_QRunnable(
                            self.CCA_executeTrhead, currentstatus.strip(), pidCheck
                        )
                        self.threadpool.start(self.With_worker)
            else:
                self.With_worker = Worker_QRunnable(self.GS_executeTrhead, "")
                self.threadpool.start(self.With_worker)

            self.DropDwnStyle()

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
        if self.ui.CodelineEdit.text()=="":
            self.msg_box.setText(
                "Enter The Oakta codee please.\t"
                
            )
            self.msg_box.exec()
            return
        self.inputCode = self.ui.CodelineEdit.text()


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
        QTimer().singleShot(5000, lambda: self.ui.CodelineEdit.clear())
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
            WorkToolFunc.Stop_portListener()  

        except AttributeError:
            pass

    def DropDwnStyle(self):

        self.ui.gspreadComboBox.setStyleSheet(
            f"""
            QComboBox {{
                border: 2px solid darkgray;
                border-radius: 5px;
                padding: 1px 18px 1px 3px; /* Adjust padding for the arrow */
                background-color: {clor[self.ui.gspreadComboBox.currentIndex()]}
                
            }}
            QComboBox:hover {{
                border: 0.5px solid black;
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: darkgray;
                border-left-style: solid;
                border-top-right-radius: 4px;
                border-bottom-right-radius: 4px;
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                  stop: 0 #E1E1E1, stop: 1 #D3D3D3);
                
            }}
            QComboBox::down-arrow {{
                /* You can use an image here */
               image: url({self.ui.file_path}); 
                
                height: 10px;
                width: 10px;
            }}
            QComboBox QAbstractItemView {{
                border: 2px solid darkgray;
                selection-background-color: blue;
                background-color: white;
                color: black;
            }}
        """
        )


class CliWidget(QWidget):
    def __init__(self, parent=None, args=None):
        super().__init__(parent)

        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)
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

        while self.process.canReadLine():
            line = self.process.readLine().data().decode('utf-8').strip()
            self.text_output.append(line)
            self.parse_ping_times(line)

    @Slot()
    def read_error(self):
        data = self.process.readAllStandardError().data().decode().strip()
        self.text_output.append(f"ERROR: {data}")

    @Slot()
    def handle_finished(self, exitCode, exitStatus):

        print(f"Process finished with exit code {exitCode} and status {exitStatus}")

        pingMatch = re.search(
            regexIPV6_V4,
            self.text_output.toPlainText(),
            flags=re.IGNORECASE,
        )
  
        if self.ping_times or self.timesOut:
            stattsVal = re.search(
                regexIPV6_V4,
                pingMatch[0],
                flags=re.IGNORECASE,
            )
# (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*

            if stattsVal:
                stattsVal = stattsVal.group(1) or stattsVal.group(2)

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


 # ------------------------------- FlexEdge look up ---------------------------
'''
For this particular class we are working specific item can't go into details.
'''
class FlexEdgeookUp(QWidget):
    def __init__(self,parent=None, args=None):
        super().__init__(parent)
        self.args = args
        self.threadpool,self.stackedWidget = args
        #initiat some object from Pyside6 lib for grafical view. layouts, buttons etc...
        self.layout = QVBoxLayout()
        self.text_outputF = QTextEdit()
        self.text_outputF.setReadOnly(True)
        self.command_input = QLineEdit()
        self.condPushBtn = QPushButton('Conductor')
        self.GlinlPushBtn = QPushButton('Close GLink')
        self.horizontalLayout_4 = QHBoxLayout()
        # Simple variable to display a message 
        self.startScreen = '+----------------------+\n| FlexEdge Lookup Tool |' \
        '\n+----------------------+\nNSOID Format: CPEGRT00000xxxxx\n\nEnter NSOID to find: '

        self.startScreen1 = '+----------------------+\n| FlexEdge Lookup Tool |' \
                    '\n+----------------------+\nNSOID Format: ' \
                    'CPEGRT00000xxxxx, or NSODIA00000xxxxx, or CPEVYS00000xxxxx.\n\nEnter NSOID to find: '
        self.text_outputF.append(f'{self.startScreen}')
        self.edComboBox = QComboBox()
        self.edComboBox.addItems(['NSO Config','ED Standdard'])
    
        self.horizontalLayout_4.addWidget(self.edComboBox)
        self.horizontalLayout_4.addWidget(self.command_input)
        self.horizontalLayout_4.addWidget(self.condPushBtn)
        self.horizontalLayout_4.addWidget(self.GlinlPushBtn)

        self.conInput = ''
        self.nsoidFormat = ''
        self.stattsVal = ''

        self.layout.addWidget(self.text_outputF)
        self.layout.addLayout(self.horizontalLayout_4)
  
        self.setLayout(self.layout)

        # text display format.
        self.text_outputF.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-family: Verdana, Arial, Helvetica, sans-serif;\n"
            "font-size: 13px;\n"
            "font-style: normal;\n"
            "font-variant: normal;\n"
            "font-weight: normal;\n"
            "border-radius: 5px;"
        )
        # Connect signals
        self.command_input.returnPressed.connect(self.edNSOIDLookUp)
        self.condPushBtn.clicked.connect(self.condSearch)
        self.GlinlPushBtn.clicked.connect(lambda: WorkToolFunc.closeSel())
        
    # Help with a quick search vu opening the browser and add creds.
    def condSearch(self):
        self.stattsVal = re.search(
                ipv4_REGEX,
                self.text_outputF.toPlainText(),
                flags=re.IGNORECASE)
    
        if self.stattsVal and self.nsoidFormat:
            self.stattsVal = self.stattsVal.group(0)
            urlLink= f"https://{self.stattsVal}/routers/{self.nsoidFormat}"
            print(urlLink)
            text, ok = QInputDialog.getText(None, "OKTA CODE", "Enter your Okta code:")
            if text and ok:
                
                self.mainWinComponent = MainWindow()
                self.mainWinComponent.inputCode = text
                WorkToolFunc.ahkExe_Path().run_script(
                    f'Run "{urlLink}"'
                )
                self.With_worker = Worker_QRunnable(self.mainWinComponent.Cond_executeTrhead_Func)
                self.threadpool.start(self.With_worker)
            else:
                return
        
    def edNSOI_executeTrhead(self):
      
        if self.edComboBox.currentIndex() == 0:
       
            self.text_outputF.append(f'{self.startScreen}')
            self.text_outputF.append(f'{self.nsoidFormat}\n')

            self.text_outputF.append(
                WorkToolFunc.edConfig_Srch(self.nsoidFormat
            ))
            self.condPushBtn.setVisible(True)
     
                
        elif self.edComboBox.currentIndex() == 1:
           
            self.text_outputF.append(f'{self.startScreen1}')
            self.text_outputF.append(f'{self.nsoidFormat}\n')

            search2 = WorkToolFunc.stdrdNSO_srchFormatter(
                                WorkToolFunc.NSOLook(self.nsoidFormat))

            self.text_outputF.append(search2)

        return "Done."


    def edNSOIDLookUp(self):
        self.text_outputF.clear()

        self.nsoidFormat = self.command_input.text().upper()

        self.CPEGRTchecker = re.search( r'(^CPEGRT0{5,}\d{5}$)',self.nsoidFormat, flags=re.IGNORECASE) 
        self.NSODIchecker =  re.search( r'(^NSODIA0{5,}\d{5}$)',self.nsoidFormat, flags=re.IGNORECASE)
        self.CPEVYSTchecker = re.search( r'(^CPEVYS0{5,}\d{5}$)',self.nsoidFormat, flags=re.IGNORECASE)
        self.command_input.clear()

        if not self.CPEGRTchecker and self.edComboBox.currentIndex() == 0:
            self.text_outputF.append(f'{self.startScreen}')
            self.text_outputF.append(f'{self.nsoidFormat}\n')

            self.text_outputF.append(f'Error: NSOID entered is invalid; format '
                    'CPEGRT00000xxxxx\n\nEnter NSOID to find:')
            return
        elif not (self.CPEGRTchecker or self.NSODIchecker or self.CPEVYSTchecker):
            self.text_outputF.append(f'{self.startScreen1}')
            self.text_outputF.append(f'{self.nsoidFormat}\n')

            self.text_outputF.append(f'Error: NSOID entered is invalid; see the format below: \n'+
                        '\tCPEGRT00000xxxxx \n\tNSODIA00000xxxxx '
                        '\n\tCPEVYS00000xxxxx\n\nEnter NSOID to find:')
            return
            
        self.With_worker = Worker_QRunnable(self.edNSOI_executeTrhead)
        self.threadpool.start(self.With_worker)
      


class Create_IW(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.TickInfo = QLabel()
        self.TickInfo.setObjectName(u"TickInfo")

        self.gridLayout_7.addWidget(self.TickInfo, 1, 1, 1, 2)

        self.pushButton = QPushButton('Send')
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_7.addWidget(self.pushButton, 3, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_4 = QComboBox()
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout.addWidget(self.comboBox_4)

        self.comboBox_3 = QComboBox()
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout.addWidget(self.comboBox_3)

        self.comboBox_2 = QComboBox()
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.gridLayout_7.addLayout(self.horizontalLayout, 3, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.accName_label = QLabel('Account Name')
        self.verticalLayout_2.addWidget(self.accName_label)

        self.accName_lineEdit = QLineEdit()
        self.verticalLayout_2.addWidget(self.accName_lineEdit)

        self.childAcc_label = QLabel('Child Account#')
        self.verticalLayout_2.addWidget(self.childAcc_label)

        self.child_AcclineEdit = QLineEdit('')
        self.verticalLayout_2.addWidget(self.child_AcclineEdit)

        self.zipCode = QLabel('Zip Code')
        self.verticalLayout_2.addWidget(self.zipCode)

        self.zipCode_lineEdit = QLineEdit()
        self.verticalLayout_2.addWidget(self.zipCode_lineEdit)

        self.time_label = QLabel('Time')
        self.verticalLayout_2.addWidget(self.time_label)

        self.time_lineEdit = QLineEdit()
        self.verticalLayout_2.addWidget(self.time_lineEdit)

        self.CID_label = QLabel('Circuitt ID')
        self.verticalLayout_2.addWidget(self.CID_label)

        self.CID_lineEdit = QLineEdit()
        self.verticalLayout_2.addWidget(self.CID_lineEdit)

        self.ticket_label = QLabel('Ticket #')
        self.verticalLayout_2.addWidget(self.ticket_label)

        self.ticket_lineEdit = QLineEdit()
        self.verticalLayout_2.addWidget(self.ticket_lineEdit)


        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 3, 1)

        self.notesTextEdit = QPlainTextEdit()
        self.notesTextEdit.setObjectName(u"notesTextEdit")
        self.notesTextEdit.setStyleSheet(u"border-color: rgb(0, 0, 0);\n""border: 1 solid black;")
        

        self.gridLayout_7.addWidget(self.notesTextEdit, 2, 1, 1, 2)

        self.dateTimeEdit_2 = QDateTimeEdit(QDate.currentDate())
     
        self.dateTimeEdit_2.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setDisplayFormat("MMMM/dd/yyyy")
        self.dateTimeEdit_2.dateChanged.connect(
            lambda date: print(date.toString("MMMM/dd/yyyy"))
        )
        self.pushButton.clicked.connect(lambda: self.timeZone(str(self.zipCode_lineEdit.text())))
        self.zipCode_lineEdit.returnPressed.connect(lambda: self.timeZone(str(self.zipCode_lineEdit.text())))

        self.gridLayout_7.addWidget(self.dateTimeEdit_2, 0, 1, 1, 2)

        self.setLayout(self.gridLayout_7)



    def timeZone(self,PostalCode):
   
        Canadapattern = r"^[A-Z]\d[A-Z] \d[A-Z]\d$"# 
        timestamp = int(time.time())
        geocode_result = ''
        cityName = ''
        timeZone_data = ''
   
        gmaps = googlemaps.Client(key=os.getenv("TIMEZ_KEY"))
        URL =  "https://maps.googleapis.com/maps/api/timezone/json?location={}%2C{}&timestamp={}&key={}"

        try:
            country = 'us'
            PostalCode = PostalCode.strip()
            if re.match(Canadapattern,PostalCode):
                country = 'ca'    
            geocode_result = gmaps.geocode(PostalCode)
            if not geocode_result:
                    nomi = pgeocode.Nominatim(country)
                    cityName = nomi.query_postal_code(PostalCode)
                    geocode_result = gmaps.geocode(cityName['place_name'])

            cityName = geocode_result[0]['formatted_address']
            lat = geocode_result[0]['geometry']['location']['lat'] 
            lng = geocode_result[0]['geometry']['location']['lng']
            URL = URL.format(lat,lng,timestamp,os.getenv("TIMEZ_KEY"))
            request_Resp = requests.get(URL).content
            timeZone_data = json.loads(request_Resp)
            tz = QTimeZone(timeZone_data['timeZoneId'].encode('utf-8'))
            current_time = QDateTime.currentDateTime(tz)
            current_time = current_time.toString("MMMM/dd/yyyy h:m AP")

            timeZone_Forma = (f'City Name:   {cityName}\n'
                                f'Time Zone:   {timeZone_data['timeZoneName']} \n' 
                                f'Time Zone ID:   {timeZone_data['timeZoneId']} \n'            
                                f'The Current Time: {current_time}\n'
                                )
            self.notesTextEdit.appendPlainText(timeZone_Forma)
            self.zipCode_lineEdit.clear()


        except BaseException as err:
            print(err)
            

        return timeZone_data
  

if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
