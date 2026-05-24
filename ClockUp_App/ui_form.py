# # -*- coding: utf-8 -*-

# ################################################################################
# # Form generated from reading UI file 'form.ui'
# ##
# # Created by: Qt User Interface Compiler version 6.9.1
# ##
# # WARNING! All changes made in this file will be lost when recompiling UI file!
# ################################################################################

# from PySide6.QtCore import (
#     QCoreApplication,
#     QDate,
#     QDateTime,
#     QLocale,
#     QMetaObject,
#     QObject,
#     QPoint,
#     QRect,
#     QSize,
#     QTime,
#     QUrl,
#     Qt,
# )
# from PySide6.QtGui import (
#     QBrush,
#     QColor,
#     QConicalGradient,
#     QCursor,
#     QFont,
#     QFontDatabase,
#     QGradient,
#     QIcon,
#     QImage,
#     QKeySequence,
#     QLinearGradient,
#     QPainter,
#     QPalette,
#     QPixmap,
#     QRadialGradient,
#     QTransform,
# )
# from PySide6.QtWidgets import (
#     QAbstractSpinBox,
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDateTimeEdit,
#     QGroupBox,
#     QLabel,
#     QLineEdit,
#     QMainWindow,
#     QPushButton,
#     QSizePolicy,
#     QStackedWidget,
#     QStatusBar,
#     QVBoxLayout,
#     QWidget,
#     QPlainTextEdit,
# )
from datetime import datetime
import os

# # Source - https://stackoverflow.com/a/53605128
# # Posted by Kamal, modified by community. See post 'Timeline' for change history
# # Retrieved 2026-02-08, License - CC BY-SA 4.0

import sys
# import os
# import sys


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):

#         if not MainWindow.objectName():
#             MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(517, 445)
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.stackedWidget = QStackedWidget(self.centralwidget)
#         self.stackedWidget.setObjectName("stackedWidget")
#         self.stackedWidget.setGeometry(QRect(0, -10, 521, 461))
#         font = QFont()
#         font.setPointSize(8)
#         self.stackedWidget.setFont(font)
#         self.page = QWidget()
#         self.page.setObjectName("page")
#         self.verticalLayoutWidget = QWidget(self.page)
#         self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
#         self.verticalLayoutWidget.setGeometry(QRect(390, 80, 115, 291))
#         self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.verticalLayout.setContentsMargins(5, 5, 5, 5)
#         self.gspreadComboBox = QComboBox(self.verticalLayoutWidget)
#         self.gspreadComboBox.setGeometry(QRect(220, 279, 141, 30))
#         # Use the function to access your file
#         self.file_path = self.resource_path(os.path.join("down-arrow.png"))
#         self.file_path = self.file_path.replace("\\", "/")

#         self.gspreadComboBox.setObjectName("GSpread")
#         self.verticalLayout.addWidget(self.gspreadComboBox)

#         self.Off_pushButton = QPushButton(self.verticalLayoutWidget)
#         self.Off_pushButton.setObjectName("Off_pushButton")
#         self.Off_pushButton.setStyleSheet("background-color: rgb(181, 181, 181);")

#         self.verticalLayout.addWidget(self.Off_pushButton)

#         self.FedgeLookUp = QPushButton(self.verticalLayoutWidget)
#         self.FedgeLookUp.setObjectName("FedgeLookUp")
#         self.FedgeLookUp.setStyleSheet("background-color: rgb(16, 255, 136);")

#         self.verticalLayout.addWidget(self.FedgeLookUp)

#         self.Break_pushButton = QPushButton(self.verticalLayoutWidget)
#         self.Break_pushButton.setObjectName("Break_pushButton")
#         self.Break_pushButton.setStyleSheet("background-color: rgb(255, 53, 35);")

#         self.verticalLayout.addWidget(self.Break_pushButton)

#         self.Lunch_pushButton = QPushButton(self.verticalLayoutWidget)
#         self.Lunch_pushButton.setObjectName("Lunch_pushButton")
#         self.Lunch_pushButton.setStyleSheet("background-color: rgb(229, 204, 102);")

#         self.verticalLayout.addWidget(self.Lunch_pushButton)

#         self.IW_pushButton = QPushButton(self.verticalLayoutWidget)
#         self.IW_pushButton.setObjectName("IW_pushButton")
#         self.IW_pushButton.setStyleSheet("background-color: rgb(21, 60, 186);")

#         self.verticalLayout.addWidget(self.IW_pushButton)

#         self.Training_pushButton = QPushButton(self.verticalLayoutWidget)
#         self.Training_pushButton.setObjectName("Training_pushButton")
#         self.Training_pushButton.setStyleSheet("background-color: rgb(86, 126, 116);")

#         self.verticalLayout.addWidget(self.Training_pushButton)

#         self.InterEscal_pushButton = QPushButton(self.verticalLayoutWidget)
#         self.InterEscal_pushButton.setObjectName("InterEscal_pushButton")
#         self.InterEscal_pushButton.setStyleSheet("background-color: rgb(98, 42, 166);")

#         self.verticalLayout.addWidget(self.InterEscal_pushButton)

#         self.CCABlock_pushButton = QPushButton(self.verticalLayoutWidget)
#         self.CCABlock_pushButton.setObjectName("CCABlock_pushButton")
#         self.CCABlock_pushButton.setStyleSheet("background-color: rgb(230, 147, 46);")

#         self.verticalLayout.addWidget(self.CCABlock_pushButton)

#         self.Out_pushButton = QPushButton(self.verticalLayoutWidget)
#         self.Out_pushButton.setObjectName("Out_pushButton")
#         self.Out_pushButton.setStyleSheet("background-color: rgb(195, 0, 0);")

#         self.verticalLayout.addWidget(self.Out_pushButton)

#         self.CCA_pushButton = QPushButton(self.verticalLayoutWidget)
#         self.CCA_pushButton.setObjectName("CCA_pushButton")
#         self.CCA_pushButton.setStyleSheet("background-color: rgb(255, 255, 127);")

#         self.verticalLayout.addWidget(self.CCA_pushButton)

#         self.checkBox = QCheckBox(self.page)
#         self.checkBox.setObjectName("checkBox")
#         self.checkBox.setGeometry(QRect(330, 162, 21, 31))
#         self.comboBox = QComboBox(self.page)
#         self.comboBox.setObjectName("comboBox")
#         self.comboBox.setGeometry(QRect(220, 279, 141, 30))
#         self.ClockInpushButton = QPushButton(self.page)
#         self.ClockInpushButton.setObjectName("ClockInpushButton")
#         self.ClockInpushButton.setGeometry(QRect(30, 220, 341, 35))
#         sizNum = 161
#         current_datetime = datetime.now()

#         current_month_name = current_datetime.strftime("%B")
#         if len(current_month_name) >= 8:
#             sizNum = 185

#         self.dateTimeEdit = QDateTimeEdit(self.page)
#         self.dateTimeEdit.setObjectName("dateTimeEdit")
#         self.dateTimeEdit.setGeometry(QRect(300, 30, sizNum, 31))
#         self.dateTimeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
#         self.dateTimeEdit.setTimeSpec(Qt.TimeSpec.LocalTime)
#         self.PassWtextEdit = QLineEdit(self.page)
#         self.PassWtextEdit.setEchoMode(QLineEdit.EchoMode.Password)
#         self.PassWtextEdit.setObjectName("PassWtextEdit")
#         self.PassWtextEdit.setGeometry(QRect(90, 120, 280, 30))
#         self.PassWtextEdit.setInputMethodHints(Qt.InputMethodHint.ImhNone)
#         self.PassWtextEdit.setDragEnabled(False)
#         self.UserNmtextEdit = QLineEdit(self.page)
#         self.UserNmtextEdit.setObjectName("UserNmtextEdit")
#         self.UserNmtextEdit.setGeometry(QRect(90, 80, 280, 30))
#         self.UserNmtextEdit.setStyleSheet("")
#         self.PassWlabel = QLabel(self.page)
#         self.PassWlabel.setObjectName("PassWlabel")
#         self.PassWlabel.setGeometry(QRect(23, 120, 50, 27))
#         self.UserNmlabel = QLabel(self.page)
#         self.UserNmlabel.setObjectName("UserNmlabel")
#         self.UserNmlabel.setGeometry(QRect(23, 80, 58, 28))
#         self.CodelineEdit = QLineEdit(self.page)
#         self.CodelineEdit.setObjectName("CodelineEdit")
#         self.CodelineEdit.setGeometry(QRect(90, 160, 230, 30))
#         self.Code_Label = QLabel(self.page)
#         self.Code_Label.setObjectName("Code_Label")
#         self.Code_Label.setGeometry(QRect(23, 160, 57, 28))
#         self.CCABBRcomboBox = QComboBox(self.page)
#         self.CCABBRcomboBox.setObjectName("CCABBRcomboBox")
#         self.CCABBRcomboBox.setGeometry(QRect(40, 279, 160, 30))
#         self.CCABBRcomboBox2 = QComboBox(self.page)
#         self.CCABBRcomboBox2.setObjectName("CCABBRcomboBox2")
#         self.CCABBRcomboBox2.setGeometry(QRect(40, 279, 160, 30))
#         self.CCABBRcomboBox3 = QComboBox(self.page)
#         self.CCABBRcomboBox3.setObjectName("CCABBRcomboBox3")
#         self.CCABBRcomboBox3.setGeometry(QRect(40, 279, 160, 30))
#         self.IPPings = QGroupBox(self.page)
#         self.IPPings.setObjectName("IPPings")
#         self.IPPings.setGeometry(QRect(30, 325, 351, 81))
#         self.Subnet_Box = QComboBox(self.IPPings)
#         self.Subnet_Box.setObjectName("Subnet_Box")
#         self.Subnet_Box.setGeometry(QRect(15, 20, 158, 22))
#         self.Subnet_Box.setFont(font)
#         self.GWIPlineEdit = QLineEdit(self.IPPings)
#         self.GWIPlineEdit.setObjectName("GWIPlineEdit")
#         self.GWIPlineEdit.setGeometry(QRect(190, 20, 141, 22))
#         self.NipComboBox = QComboBox(self.IPPings)
#         self.NipComboBox.setObjectName("NipComboBox")
#         self.NipComboBox.setGeometry(QRect(30, 50, 105, 22))
#         self.NipComboBox.setFont(font)
#         self.PingButton = QPushButton(self.IPPings)
#         self.PingButton.setObjectName("PingButton")
#         self.PingButton.setGeometry(QRect(200, 50, 111, 22))
#         self.stackedWidget.addWidget(self.page)
#         # self.page_2 = QWidget()
#         # self.page_2.setObjectName(u"page_2")
#         self.Prev_pushButton = QPushButton(self.centralwidget)
#         self.Prev_pushButton.setObjectName("pushButton")
#         self.Prev_pushButton.setGeometry(QRect(360, 400, 45, 24))
#         self.Prev_pushButton.setFont(font)
#         self.Prev_pushButton.setStyleSheet(
#             "background-color: rgb(98, 98, 98);\n" "color: rgb(255, 255, 255);"
#         )
#         self.Next_Button = QPushButton(self.centralwidget)
#         self.Next_Button.setObjectName("pushButton_2")
#         self.Next_Button.setGeometry(QRect(460, 400, 45, 24))
#         self.Next_Button.setFont(font)
#         self.Next_Button.setStyleSheet(
#             "background-color: rgb(98, 98, 98);\n" "color: rgb(255, 255, 255);"
#         )
#         self.Home_Button = QPushButton(self.centralwidget)
#         self.Home_Button.setObjectName("pushButton_3")
#         self.Home_Button.setGeometry(QRect(410, 400, 45, 24))
#         self.Home_Button.setFont(font)
#         self.Home_Button.setStyleSheet("background-color: rgb(85, 255, 255);")

#         self.CloseTab = QPushButton(self.centralwidget)
#         self.CloseTab.setObjectName("CloseTab")
#         self.CloseTab.setGeometry(QRect(20, 400, 70, 22))
#         self.CloseTab.setFont(font)
#         self.CloseTab.setStyleSheet("background-color: rgb(179, 110, 141);")
#         self.allEnd_Pings = QPushButton(self.centralwidget)
#         self.allEnd_Pings.setObjectName("allPinshBtn")
#         self.allEnd_Pings.setGeometry(QRect(220, 400, 75, 22))
#         self.allEnd_Pings.setFont(font)
#         self.allEnd_Pings.setStyleSheet("background-color: rgb(133, 98, 168);")

#         self.End_Pings = QPushButton(self.centralwidget)
#         self.End_Pings.setObjectName("pushButton_2")
#         self.End_Pings.setGeometry(QRect(100, 400, 70, 22))
#         self.End_Pings.setFont(font)
#         self.End_Pings.setStyleSheet("background-color: rgb(133, 98, 168);")
#         self.stackedWidget.setCurrentIndex(0)
#         self.comboBox.setCurrentIndex(-1)
#         self.CCABBRcomboBox.setCurrentIndex(-1)
#         self.CCABBRcomboBox2.setCurrentIndex(-1)
#         self.CCABBRcomboBox3.setCurrentIndex(-1)

#         self.NSOID = QLineEdit(self.page)
#         self.NSOID.setObjectName("NSOID")
#         self.NSOID.setEnabled(True)
#         self.NSOID.setGeometry(QRect(220, 279, 165, 24))

#         self.page_2 = QWidget()
#         self.page_2.setObjectName("page_2")
#         self.dateTimeEdit_2 = QDateTimeEdit(self.page_2)
#         self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
#         self.dateTimeEdit_2.setGeometry(QRect(350, 40, 131, 21))
#         self.pushButton = QPushButton(self.page_2)
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton.setGeometry(QRect(380, 370, 75, 24))
#         self.verticalLayoutWidget_2 = QWidget(self.page_2)
#         self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
#         self.verticalLayoutWidget_2.setGeometry(QRect(10, 50, 191, 284))
#         self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.label = QLabel(self.verticalLayoutWidget_2)
#         self.label.setObjectName("label")

#         self.verticalLayout_2.addWidget(self.label)

#         self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget_2)
#         self.lineEdit_3.setObjectName("lineEdit_3")

#         self.verticalLayout_2.addWidget(self.lineEdit_3)

#         self.label_2 = QLabel(self.verticalLayoutWidget_2)
#         self.label_2.setObjectName("label_2")

#         self.verticalLayout_2.addWidget(self.label_2)

#         self.lineEdit = QLineEdit(self.verticalLayoutWidget_2)
#         self.lineEdit.setObjectName("lineEdit")

#         self.verticalLayout_2.addWidget(self.lineEdit)

#         self.label_3 = QLabel(self.verticalLayoutWidget_2)
#         self.label_3.setObjectName("label_3")

#         self.verticalLayout_2.addWidget(self.label_3)

#         self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget_2)
#         self.lineEdit_2.setObjectName("lineEdit_2")

#         self.verticalLayout_2.addWidget(self.lineEdit_2)

#         self.label_4 = QLabel(self.verticalLayoutWidget_2)
#         self.label_4.setObjectName("label_4")

#         self.verticalLayout_2.addWidget(self.label_4)

#         self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget_2)
#         self.lineEdit_5.setObjectName("lineEdit_5")

#         self.verticalLayout_2.addWidget(self.lineEdit_5)

#         self.label_6 = QLabel(self.verticalLayoutWidget_2)
#         self.label_6.setObjectName("label_6")

#         self.verticalLayout_2.addWidget(self.label_6)

#         self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget_2)
#         self.lineEdit_4.setObjectName("lineEdit_4")

#         self.verticalLayout_2.addWidget(self.lineEdit_4)

#         self.label_7 = QLabel(self.verticalLayoutWidget_2)
#         self.label_7.setObjectName("label_7")

#         self.verticalLayout_2.addWidget(self.label_7)

#         self.lineEdit_6 = QLineEdit(self.verticalLayoutWidget_2)
#         self.lineEdit_6.setObjectName("lineEdit_6")

#         self.verticalLayout_2.addWidget(self.lineEdit_6)

#         self.comboBox_2 = QComboBox(self.page_2)
#         self.comboBox_2.setObjectName("comboBox_2")
#         self.comboBox_2.setGeometry(QRect(240, 370, 121, 21))
#         self.comboBox_3 = QComboBox(self.page_2)
#         self.comboBox_3.setObjectName("comboBox_3")
#         self.comboBox_3.setGeometry(QRect(110, 370, 121, 21))
#         self.comboBox_4 = QComboBox(self.page_2)
#         self.comboBox_4.setObjectName("comboBox_4")
#         self.comboBox_4.setGeometry(QRect(20, 370, 71, 21))
#         self.plainTextEdit = QPlainTextEdit(self.page_2)
#         self.plainTextEdit.setObjectName("plainTextEdit")
#         self.plainTextEdit.setGeometry(QRect(220, 100, 241, 251))
#         self.label_5 = QLabel(self.page_2)
#         self.label_5.setObjectName("label_5")
#         self.label_5.setGeometry(QRect(240, 70, 171, 16))
#         # self.stackedWidget.addWidget(self.page_2)
#         # self.NSOID.setVerticalScrollBarPolicy(
#         #     Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         # self.NSOID.setHorizontalScrollBarPolicy(
#         #     Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

#         # self.ResulttDisplay = QPlainTextEdit(self.centralwidget)
#         # self.ResulttDisplay.setObjectName(u"ResulttDisplay")
#         # self.ResulttDisplay.setEnabled(True)
#         # self.ResulttDisplay.setGeometry(QRect(10, 250, 391, 116))

#         # self.stackedWidget.addWidget()
#         MainWindow.setCentralWidget(self.centralwidget)
#         # self.statusbar = QStatusBar(MainWindow)
#         # self.statusbar.setObjectName(u"statusbar")
#         # MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)

#         QMetaObject.connectSlotsByName(MainWindow)

#     # setupUi
#     def resource_path(self, relative_path):
#         """Get absolute path to resource, works for dev and for PyInstaller"""
#         base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
#         return os.path.join(base_path, relative_path)

#     def retranslateUi(self, MainWindow):
#         # self.setWindowTitle("JH Customize NOC Tool")

#         MainWindow.setWindowTitle(
#             QCoreApplication.translate("MainWindow", "JH Customize NOC Tool", None)
#         )
#         self.FedgeLookUp.setText(QCoreApplication.translate("MainWindow", "FedgeLookUp", None))
#         self.Break_pushButton.setText(
#             QCoreApplication.translate("MainWindow", "BREAK", None)
#         )
#         self.Lunch_pushButton.setText(
#             QCoreApplication.translate("MainWindow", "LUNCH", None)
#         )
#         self.IW_pushButton.setText(
#             QCoreApplication.translate("MainWindow", "IW/NI", None)
#         )
#         self.Out_pushButton.setText(
#             QCoreApplication.translate("MainWindow", "OUT", None)
#         )
#         self.CCA_pushButton.setText(
#             QCoreApplication.translate("MainWindow", "CCA", None)
#         )
#         self.Off_pushButton.setText(
#             QCoreApplication.translate("MainWindow", "Create An IW", None)
#         )

#         self.Training_pushButton.setText(
#             QCoreApplication.translate("MainWindow", "TRAINING", None)
#         )

#         self.InterEscal_pushButton.setText(
#             QCoreApplication.translate("MainWindow", "ESCALATIONS", None)
#         )

#         self.CCABlock_pushButton.setText(
#             QCoreApplication.translate("MainWindow", "CALL BLOCK", None)
#         )

#         self.checkBox.setText("")
#         self.ClockInpushButton.setText(
#             QCoreApplication.translate("MainWindow", "Submit", None)
#         )
#         self.PassWlabel.setText(
#             QCoreApplication.translate("MainWindow", "Password", None)
#         )
#         self.UserNmlabel.setText(
#             QCoreApplication.translate("MainWindow", "User Name", None)
#         )
#         self.Code_Label.setText(
#             QCoreApplication.translate("MainWindow", "Auth Code", None)
#         )
#         self.IPPings.setTitle(
#             QCoreApplication.translate("MainWindow", "IP Pings", None)
#         )
#         # if QT_CONFIG(tooltip)
#         self.Subnet_Box.setToolTip(
#             QCoreApplication.translate(
#                 "MainWindow",
#                 "<html><head/><body><p><span style=\" font-size:10pt;\">Choose the </span><span style=\" font-family:'Arial','Helvetica','sans-serif'; font-size:10pt; font-weight:700; color:#222222;\">Subnet Mask</span></p></body></html>",
#                 None,
#             )
#         )
#         # endif // QT_CONFIG(tooltip)
#         # if QT_CONFIG(tooltip)
#         self.GWIPlineEdit.setToolTip(
#             QCoreApplication.translate(
#                 "MainWindow",
#                 '<html><head/><body><p>Use The <span style=" font-weight:700;">Gateway IP</span></p></body></html>',
#                 None,
#             )
#         )
#         # endif // QT_CONFIG(tooltip)
#         self.PingButton.setText(
#             QCoreApplication.translate("MainWindow", "Send Ping", None)
#         )
#         self.Prev_pushButton.setText(
#             QCoreApplication.translate("MainWindow", "Prev", None)
#         )
#         self.Next_Button.setText(QCoreApplication.translate("MainWindow", "Next", None))
#         self.Home_Button.setText(QCoreApplication.translate("MainWindow", "Home", None))
#         self.PingButton.setText(
#             QCoreApplication.translate("MainWindow", "Send Ping", None)
#         )
#         self.CloseTab.setText(
#             QCoreApplication.translate("MainWindow", "Close Tab", None)
#         )
#         self.End_Pings.setText(
#             QCoreApplication.translate("MainWindow", "End Ping", None)
#         )
#         self.allEnd_Pings.setText(
#             QCoreApplication.translate("MainWindow", "End All Ping", None)
#         )

#     retranslateUi


# # x = int(eval(input('enter an int: ')))
# # # if ((x % 2) == 0):5
# # #     print('even')
# # # else:
# # #     print('odd')
# # n = 1
# # while x >= 1:
# #     print(x)
# #     n = n*(x)
# #     x -= 1

# # print(n)


# -------------------------------------------------------------------New Set Up--------------------------------------------------------------------


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(621, 468)


        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(8)
        self.stackedWidget.setFont(font)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setMinimumSize(QSize(527, 0))

        self.file_path = self.resource_path(os.path.join("down-arrow.png"))
        self.file_path = self.file_path.replace("\\", "/")
       
        self.verticalLayoutWidget = QWidget(self.page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(450, 70, 141, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.gspreadComboBox = QComboBox(self.verticalLayoutWidget)
        self.gspreadComboBox.setGeometry(QRect(220, 279, 141, 30))
        self.gspreadComboBox.setObjectName("GSpread")
        self.verticalLayout.addWidget(self.gspreadComboBox)

        self.CreateIW_pushBtn = QPushButton(self.verticalLayoutWidget)
        self.CreateIW_pushBtn.setObjectName("CreateIW_pushBtn")
        self.CreateIW_pushBtn.setStyleSheet("background-color: rgb(181, 181, 181);")

        self.verticalLayout.addWidget(self.CreateIW_pushBtn)

        self.FedgeLookUp = QPushButton(self.verticalLayoutWidget)
        self.FedgeLookUp.setObjectName("FedgeLookUp")
        self.FedgeLookUp.setStyleSheet("background-color: rgb(16, 255, 136);")

        self.verticalLayout.addWidget(self.FedgeLookUp)

        self.CCA_pushButton = QPushButton(self.verticalLayoutWidget)
        self.CCA_pushButton.setObjectName(u"CCA_pushButton")
        self.CCA_pushButton.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.verticalLayout.addWidget(self.CCA_pushButton)

        self.checkBox = QCheckBox(self.page)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(370, 140, 21, 31))
        self.comboBox = QComboBox(self.page)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(250, 240, 161, 30))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.ClockInpushButton = QPushButton(self.page)
        self.ClockInpushButton.setObjectName(u"ClockInpushButton")
        self.ClockInpushButton.setGeometry(QRect(20, 192, 401, 35))
        sizePolicy2.setHeightForWidth(self.ClockInpushButton.sizePolicy().hasHeightForWidth())
        self.ClockInpushButton.setSizePolicy(sizePolicy2)
        self.PassWtextEdit = QLineEdit(self.page)
        self.PassWtextEdit.setObjectName(u"PassWtextEdit")
        self.PassWtextEdit.setGeometry(QRect(90, 98, 331, 30))
        sizePolicy2.setHeightForWidth(self.PassWtextEdit.sizePolicy().hasHeightForWidth())
        self.PassWtextEdit.setSizePolicy(sizePolicy2)
        self.PassWtextEdit.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.PassWtextEdit.setDragEnabled(False)
        self.UserNmtextEdit = QLineEdit(self.page)
        self.UserNmtextEdit.setObjectName(u"UserNmtextEdit")
        self.UserNmtextEdit.setGeometry(QRect(90, 58, 331, 30))
        sizePolicy2.setHeightForWidth(self.UserNmtextEdit.sizePolicy().hasHeightForWidth())
        self.UserNmtextEdit.setSizePolicy(sizePolicy2)
        self.UserNmtextEdit.setStyleSheet(u"")
        self.PassWlabel = QLabel(self.page)
        self.PassWlabel.setObjectName(u"PassWlabel")
        self.PassWlabel.setGeometry(QRect(23, 98, 50, 27))
        self.UserNmlabel = QLabel(self.page)
        self.UserNmlabel.setObjectName(u"UserNmlabel")
        self.UserNmlabel.setGeometry(QRect(23, 58, 58, 28))
        self.CodelineEdit = QLineEdit(self.page)
        self.CodelineEdit.setObjectName(u"CodelineEdit")
        self.CodelineEdit.setGeometry(QRect(90, 138, 261, 30))
        sizePolicy2.setHeightForWidth(self.CodelineEdit.sizePolicy().hasHeightForWidth())
        self.CodelineEdit.setSizePolicy(sizePolicy2)
        self.Code_Label = QLabel(self.page)
        self.Code_Label.setObjectName(u"Code_Label")
        self.Code_Label.setGeometry(QRect(23, 138, 57, 28))
        self.CCABBRcomboBox = QComboBox(self.page)
        self.CCABBRcomboBox.setObjectName(u"CCABBRcomboBox")
        self.CCABBRcomboBox.setGeometry(QRect(30, 240, 181, 30))
        sizePolicy2.setHeightForWidth(self.CCABBRcomboBox.sizePolicy().hasHeightForWidth())
        self.CCABBRcomboBox.setSizePolicy(sizePolicy2)
    
        self.NSOID = QLineEdit(self.page)
        self.NSOID.setObjectName(u"NSOID")
        self.NSOID.setEnabled(True)
        self.NSOID.setGeometry(QRect(250, 240, 165, 30))
        

        self.gridLayoutWidget_3 = QWidget(self.page)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 10, 591, 31))
        self.TopGridDate = QGridLayout(self.gridLayoutWidget_3)
        self.TopGridDate.setObjectName(u"TopGridDate")
        self.TopGridDate.setContentsMargins(0, 0, 0, 0)
        self.dateTimeEdit = QDateTimeEdit(self.gridLayoutWidget_3)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateTimeEdit.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.TopGridDate.addWidget(self.dateTimeEdit, 0, 2, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_3)
        self.label_19.setObjectName(u"label_19")

        self.TopGridDate.addWidget(self.label_19, 0, 1, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.page)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(20, 290, 421, 101))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.IPPings = QGroupBox(self.gridLayoutWidget_4)
        self.IPPings.setObjectName(u"IPPings")
        sizePolicy2.setHeightForWidth(self.IPPings.sizePolicy().hasHeightForWidth())
        self.IPPings.setSizePolicy(sizePolicy2)
        self.gridLayout_8 = QGridLayout(self.IPPings)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.Subnet_Box = QComboBox(self.IPPings)
        self.Subnet_Box.setObjectName(u"Subnet_Box")
        sizePolicy2.setHeightForWidth(self.Subnet_Box.sizePolicy().hasHeightForWidth())
        self.Subnet_Box.setSizePolicy(sizePolicy2)
        self.Subnet_Box.setFont(font)

        self.gridLayout_8.addWidget(self.Subnet_Box, 0, 0, 1, 1)

        self.GWIPlineEdit = QLineEdit(self.IPPings)
        self.GWIPlineEdit.setObjectName(u"GWIPlineEdit")
        sizePolicy2.setHeightForWidth(self.GWIPlineEdit.sizePolicy().hasHeightForWidth())
        self.GWIPlineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.GWIPlineEdit, 0, 1, 1, 1)

        self.NipComboBox = QComboBox(self.IPPings)
        self.NipComboBox.setObjectName(u"NipComboBox")
        sizePolicy2.setHeightForWidth(self.NipComboBox.sizePolicy().hasHeightForWidth())
        self.NipComboBox.setSizePolicy(sizePolicy2)
        self.NipComboBox.setFont(font)

        self.gridLayout_8.addWidget(self.NipComboBox, 1, 0, 1, 1)

        self.PingButton = QPushButton(self.IPPings)
        self.PingButton.setObjectName(u"PingButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.PingButton.sizePolicy().hasHeightForWidth())
        self.PingButton.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.PingButton, 1, 1, 1, 1)

        self.gridLayout_6.addWidget(self.IPPings, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.Bns_Layout = QGridLayout()
        self.Bns_Layout.setObjectName(u"Bns_Layout")
        self.endPing_pushBtn = QPushButton(self.centralwidget)
        self.endPing_pushBtn.setObjectName(u"endPing_pushBtn")

        self.Bns_Layout.addWidget(self.endPing_pushBtn, 0, 2, 1, 1)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.Bns_Layout.addWidget(self.label_16, 0, 3, 1, 1)

        self.endAllPing_pushBtn = QPushButton(self.centralwidget)
        self.endAllPing_pushBtn.setObjectName(u"endAllPing_pushBtn")

        self.Bns_Layout.addWidget(self.endAllPing_pushBtn, 0, 5, 1, 1)

        self.Home_pushBtn = QPushButton(self.centralwidget)
        self.Home_pushBtn.setObjectName(u"Home_pushBtn")

        self.Bns_Layout.addWidget(self.Home_pushBtn, 0, 9, 1, 1)

        self.Next_pushBtn = QPushButton(self.centralwidget)
        self.Next_pushBtn.setObjectName(u"Next_pushBtn")

        self.Bns_Layout.addWidget(self.Next_pushBtn, 0, 10, 1, 1)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.Bns_Layout.addWidget(self.label_17, 0, 4, 1, 1)

        self.Close_pushBtn = QPushButton(self.centralwidget)
        self.Close_pushBtn.setObjectName(u"Close_pushBtn")

        self.Bns_Layout.addWidget(self.Close_pushBtn, 0, 1, 1, 1)

        self.Prev_pushBtn = QPushButton(self.centralwidget)
        self.Prev_pushBtn.setObjectName(u"Prev_pushBtn")

        self.Bns_Layout.addWidget(self.Prev_pushBtn, 0, 8, 1, 1)

        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.Bns_Layout.addWidget(self.label_18, 0, 7, 1, 1)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.Bns_Layout.addWidget(self.label_20, 0, 6, 1, 1)


        self.gridLayout.addLayout(self.Bns_Layout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(-1)
        self.CCABBRcomboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def resource_path(self, relative_path):
        """Get absolute path to resource, works for dev and for PyInstaller"""
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"JH Customize NOC Tool", None))

        self.CreateIW_pushBtn.setText(QCoreApplication.translate("MainWindow", "Create An IW", None))
        self.FedgeLookUp.setText(QCoreApplication.translate("MainWindow", "FedgeLookUp", None))
      
        self.CCA_pushButton.setText(QCoreApplication.translate("MainWindow", u"CCA", None))
        self.checkBox.setText("")
        self.ClockInpushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.PassWlabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.UserNmlabel.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.Code_Label.setText(QCoreApplication.translate("MainWindow", u"Auth Code", None))
        self.label_19.setText("")
        self.IPPings.setTitle(QCoreApplication.translate("MainWindow", u"IP Pings", None))
#if QT_CONFIG(tooltip)
        self.Subnet_Box.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Choose the </span><span style=\" font-family:'Arial','Helvetica','sans-serif'; font-size:10pt; font-weight:700; color:#222222;\">Subnet Mask</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.GWIPlineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Use The <span style=\" font-weight:700;\">Gateway IP</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.PingButton.setText(QCoreApplication.translate("MainWindow", u"Send Ping", None))
    
        self.endPing_pushBtn.setText(QCoreApplication.translate("MainWindow", u"End Ping", None))
        self.label_16.setText("")
        self.endAllPing_pushBtn.setText(QCoreApplication.translate("MainWindow", u"End All Pings", None))
        self.Home_pushBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Next_pushBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_17.setText("")
        self.Close_pushBtn.setText(QCoreApplication.translate("MainWindow", u"Close Tab", None))
        self.Prev_pushBtn.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.label_18.setText("")
        self.label_20.setText("")
    # retranslateUi


