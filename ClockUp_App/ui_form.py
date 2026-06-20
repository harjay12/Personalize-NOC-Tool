# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
import sys
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

        self.speechToTextBnt = QPushButton(self.verticalLayoutWidget)
        self.speechToTextBnt.setObjectName("Speech To Text")
        self.speechToTextBnt.setStyleSheet("background-color: rgb(106, 205, 36);")

        self.verticalLayout.addWidget(self.speechToTextBnt)

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
        self.speechToTextBnt.setText(QCoreApplication.translate("MainWindow", "Speech To Text", None))
      
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


