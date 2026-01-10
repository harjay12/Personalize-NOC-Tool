# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'form.ui'
##
# Created by: Qt User Interface Compiler version 6.9.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QStackedWidget,
    QStatusBar,
    QVBoxLayout,
    QWidget,
    QPlainTextEdit,
)
from datetime import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(517, 445)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, -10, 521, 461))
        font = QFont()
        font.setPointSize(8)
        self.stackedWidget.setFont(font)
        self.page = QWidget()
        self.page.setObjectName("page")
        self.verticalLayoutWidget = QWidget(self.page)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(400, 80, 85, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.Off_pushButton = QPushButton(self.verticalLayoutWidget)
        self.Off_pushButton.setObjectName("Off_pushButton")
        self.Off_pushButton.setStyleSheet("background-color: rgb(181, 181, 181);")

        self.verticalLayout.addWidget(self.Off_pushButton)

        self.In_pushButton = QPushButton(self.verticalLayoutWidget)
        self.In_pushButton.setObjectName("In_pushButton")
        self.In_pushButton.setStyleSheet("background-color: rgb(16, 255, 136);")

        self.verticalLayout.addWidget(self.In_pushButton)

        self.Break_pushButton = QPushButton(self.verticalLayoutWidget)
        self.Break_pushButton.setObjectName("Break_pushButton")
        self.Break_pushButton.setStyleSheet("background-color: rgb(255, 53, 35);")

        self.verticalLayout.addWidget(self.Break_pushButton)

        self.Lunch_pushButton = QPushButton(self.verticalLayoutWidget)
        self.Lunch_pushButton.setObjectName("Lunch_pushButton")
        self.Lunch_pushButton.setStyleSheet("background-color: rgb(229, 204, 102);")

        self.verticalLayout.addWidget(self.Lunch_pushButton)

        self.IW_pushButton = QPushButton(self.verticalLayoutWidget)
        self.IW_pushButton.setObjectName("IW_pushButton")
        self.IW_pushButton.setStyleSheet("background-color: rgb(21, 60, 186);")

        self.verticalLayout.addWidget(self.IW_pushButton)

        self.Training_pushButton = QPushButton(self.verticalLayoutWidget)
        self.Training_pushButton.setObjectName("Training_pushButton")
        self.Training_pushButton.setStyleSheet("background-color: rgb(86, 126, 116);")

        self.verticalLayout.addWidget(self.Training_pushButton)

        self.InterEscal_pushButton = QPushButton(self.verticalLayoutWidget)
        self.InterEscal_pushButton.setObjectName("InterEscal_pushButton")
        self.InterEscal_pushButton.setStyleSheet("background-color: rgb(98, 42, 166);")

        self.verticalLayout.addWidget(self.InterEscal_pushButton)

        self.CCABlock_pushButton = QPushButton(self.verticalLayoutWidget)
        self.CCABlock_pushButton.setObjectName("CCABlock_pushButton")
        self.CCABlock_pushButton.setStyleSheet("background-color: rgb(230, 147, 46);")

        self.verticalLayout.addWidget(self.CCABlock_pushButton)

        self.Out_pushButton = QPushButton(self.verticalLayoutWidget)
        self.Out_pushButton.setObjectName("Out_pushButton")
        self.Out_pushButton.setStyleSheet("background-color: rgb(195, 0, 0);")

        self.verticalLayout.addWidget(self.Out_pushButton)

        self.CCA_pushButton = QPushButton(self.verticalLayoutWidget)
        self.CCA_pushButton.setObjectName("CCA_pushButton")
        self.CCA_pushButton.setStyleSheet("background-color: rgb(255, 255, 127);")

        self.verticalLayout.addWidget(self.CCA_pushButton)

        self.checkBox = QCheckBox(self.page)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setGeometry(QRect(330, 162, 21, 31))
        self.comboBox = QComboBox(self.page)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(220, 279, 141, 30))
        self.ClockInpushButton = QPushButton(self.page)
        self.ClockInpushButton.setObjectName("ClockInpushButton")
        self.ClockInpushButton.setGeometry(QRect(30, 220, 341, 35))
        sizNum = 161
        current_datetime = datetime.now()

        current_month_name = current_datetime.strftime("%B")
        if len(current_month_name) >= 8:
            sizNum = 185

        self.dateTimeEdit = QDateTimeEdit(self.page)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(300, 30, sizNum, 31))
        self.dateTimeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateTimeEdit.setTimeSpec(Qt.TimeSpec.LocalTime)
        self.PassWtextEdit = QLineEdit(self.page)
        self.PassWtextEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.PassWtextEdit.setObjectName("PassWtextEdit")
        self.PassWtextEdit.setGeometry(QRect(90, 120, 300, 30))
        self.PassWtextEdit.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.PassWtextEdit.setDragEnabled(False)
        self.UserNmtextEdit = QLineEdit(self.page)
        self.UserNmtextEdit.setObjectName("UserNmtextEdit")
        self.UserNmtextEdit.setGeometry(QRect(90, 80, 300, 30))
        self.UserNmtextEdit.setStyleSheet("")
        self.PassWlabel = QLabel(self.page)
        self.PassWlabel.setObjectName("PassWlabel")
        self.PassWlabel.setGeometry(QRect(23, 120, 50, 27))
        self.UserNmlabel = QLabel(self.page)
        self.UserNmlabel.setObjectName("UserNmlabel")
        self.UserNmlabel.setGeometry(QRect(23, 80, 58, 28))
        self.CodelineEdit = QLineEdit(self.page)
        self.CodelineEdit.setObjectName("CodelineEdit")
        self.CodelineEdit.setGeometry(QRect(90, 160, 230, 30))
        self.Code_Label = QLabel(self.page)
        self.Code_Label.setObjectName("Code_Label")
        self.Code_Label.setGeometry(QRect(23, 160, 57, 28))
        self.CCABBRcomboBox = QComboBox(self.page)
        self.CCABBRcomboBox.setObjectName("CCABBRcomboBox")
        self.CCABBRcomboBox.setGeometry(QRect(40, 279, 160, 30))
        self.CCABBRcomboBox2 = QComboBox(self.page)
        self.CCABBRcomboBox2.setObjectName("CCABBRcomboBox2")
        self.CCABBRcomboBox2.setGeometry(QRect(40, 279, 160, 30))
        self.CCABBRcomboBox3 = QComboBox(self.page)
        self.CCABBRcomboBox3.setObjectName("CCABBRcomboBox3")
        self.CCABBRcomboBox3.setGeometry(QRect(40, 279, 160, 30))
        self.IPPings = QGroupBox(self.page)
        self.IPPings.setObjectName("IPPings")
        self.IPPings.setGeometry(QRect(30, 325, 351, 81))
        self.Subnet_Box = QComboBox(self.IPPings)
        self.Subnet_Box.setObjectName("Subnet_Box")
        self.Subnet_Box.setGeometry(QRect(15, 20, 158, 22))
        self.Subnet_Box.setFont(font)
        self.GWIPlineEdit = QLineEdit(self.IPPings)
        self.GWIPlineEdit.setObjectName("GWIPlineEdit")
        self.GWIPlineEdit.setGeometry(QRect(190, 20, 141, 22))
        self.NipComboBox = QComboBox(self.IPPings)
        self.NipComboBox.setObjectName("NipComboBox")
        self.NipComboBox.setGeometry(QRect(30, 50, 105, 22))
        self.NipComboBox.setFont(font)
        self.PingButton = QPushButton(self.IPPings)
        self.PingButton.setObjectName("PingButton")
        self.PingButton.setGeometry(QRect(200, 50, 111, 22))
        self.stackedWidget.addWidget(self.page)
        # self.page_2 = QWidget()
        # self.page_2.setObjectName(u"page_2")
        self.Prev_pushButton = QPushButton(self.centralwidget)
        self.Prev_pushButton.setObjectName("pushButton")
        self.Prev_pushButton.setGeometry(QRect(360, 400, 45, 24))
        self.Prev_pushButton.setFont(font)
        self.Prev_pushButton.setStyleSheet(
            "background-color: rgb(98, 98, 98);\n" "color: rgb(255, 255, 255);"
        )
        self.Next_Button = QPushButton(self.centralwidget)
        self.Next_Button.setObjectName("pushButton_2")
        self.Next_Button.setGeometry(QRect(460, 400, 45, 24))
        self.Next_Button.setFont(font)
        self.Next_Button.setStyleSheet(
            "background-color: rgb(98, 98, 98);\n" "color: rgb(255, 255, 255);"
        )
        self.Home_Button = QPushButton(self.centralwidget)
        self.Home_Button.setObjectName("pushButton_3")
        self.Home_Button.setGeometry(QRect(410, 400, 45, 24))
        self.Home_Button.setFont(font)
        self.Home_Button.setStyleSheet("background-color: rgb(85, 255, 255);")

        self.CloseTab = QPushButton(self.centralwidget)
        self.CloseTab.setObjectName("CloseTab")
        self.CloseTab.setGeometry(QRect(20, 400, 70, 22))
        self.CloseTab.setFont(font)
        self.CloseTab.setStyleSheet("background-color: rgb(179, 110, 141);")
        self.allEnd_Pings = QPushButton(self.centralwidget)
        self.allEnd_Pings.setObjectName("allPinshBtn")
        self.allEnd_Pings.setGeometry(QRect(220, 400, 75, 22))
        self.allEnd_Pings.setFont(font)
        self.allEnd_Pings.setStyleSheet("background-color: rgb(133, 98, 168);")

        self.End_Pings = QPushButton(self.centralwidget)
        self.End_Pings.setObjectName("pushButton_2")
        self.End_Pings.setGeometry(QRect(100, 400, 70, 22))
        self.End_Pings.setFont(font)
        self.End_Pings.setStyleSheet("background-color: rgb(133, 98, 168);")
        self.stackedWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(-1)
        self.CCABBRcomboBox.setCurrentIndex(-1)
        self.CCABBRcomboBox2.setCurrentIndex(-1)
        self.CCABBRcomboBox3.setCurrentIndex(-1)

        self.NSOID = QLineEdit(self.page)
        self.NSOID.setObjectName("NSOID")
        self.NSOID.setEnabled(True)
        self.NSOID.setGeometry(QRect(220, 279, 165, 24))
        # self.NSOID.setVerticalScrollBarPolicy(
        #     Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # self.NSOID.setHorizontalScrollBarPolicy(
        #     Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # self.ResulttDisplay = QPlainTextEdit(self.centralwidget)
        # self.ResulttDisplay.setObjectName(u"ResulttDisplay")
        # self.ResulttDisplay.setEnabled(True)
        # self.ResulttDisplay.setGeometry(QRect(10, 250, 391, 116))

        # self.stackedWidget.addWidget()
        MainWindow.setCentralWidget(self.centralwidget)
        # self.statusbar = QStatusBar(MainWindow)
        # self.statusbar.setObjectName(u"statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        # self.setWindowTitle("JH Customize NOC Tool")

        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "JH Customize NOC Tool", None)
        )
        self.In_pushButton.setText(QCoreApplication.translate("MainWindow", "IN", None))
        self.Break_pushButton.setText(
            QCoreApplication.translate("MainWindow", "BREAK", None)
        )
        self.Lunch_pushButton.setText(
            QCoreApplication.translate("MainWindow", "LUNCH", None)
        )
        self.IW_pushButton.setText(
            QCoreApplication.translate("MainWindow", "IW/NI", None)
        )
        self.Out_pushButton.setText(
            QCoreApplication.translate("MainWindow", "OUT", None)
        )
        self.CCA_pushButton.setText(
            QCoreApplication.translate("MainWindow", "CCA", None)
        )
        self.Off_pushButton.setText(
            QCoreApplication.translate("MainWindow", "OFF", None)
        )

        self.Training_pushButton.setText(
            QCoreApplication.translate("MainWindow", "TRAINING", None)
        )

        self.InterEscal_pushButton.setText(
            QCoreApplication.translate("MainWindow", "ESCALATIONS", None)
        )

        self.CCABlock_pushButton.setText(
            QCoreApplication.translate("MainWindow", "CALL BLOCK", None)
        )

        self.checkBox.setText("")
        self.ClockInpushButton.setText(
            QCoreApplication.translate("MainWindow", "Submit", None)
        )
        self.PassWlabel.setText(
            QCoreApplication.translate("MainWindow", "Password", None)
        )
        self.UserNmlabel.setText(
            QCoreApplication.translate("MainWindow", "User Name", None)
        )
        self.Code_Label.setText(
            QCoreApplication.translate("MainWindow", "Auth Code", None)
        )
        self.IPPings.setTitle(
            QCoreApplication.translate("MainWindow", "IP Pings", None)
        )
        # if QT_CONFIG(tooltip)
        self.Subnet_Box.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:10pt;\">Choose the </span><span style=\" font-family:'Arial','Helvetica','sans-serif'; font-size:10pt; font-weight:700; color:#222222;\">Subnet Mask</span></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.GWIPlineEdit.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Use The <span style=" font-weight:700;">Gateway IP</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.PingButton.setText(
            QCoreApplication.translate("MainWindow", "Send Ping", None)
        )
        self.Prev_pushButton.setText(
            QCoreApplication.translate("MainWindow", "Prev", None)
        )
        self.Next_Button.setText(QCoreApplication.translate("MainWindow", "Next", None))
        self.Home_Button.setText(QCoreApplication.translate("MainWindow", "Home", None))
        self.PingButton.setText(
            QCoreApplication.translate("MainWindow", "Send Ping", None)
        )
        self.CloseTab.setText(
            QCoreApplication.translate("MainWindow", "Close Tab", None)
        )
        self.End_Pings.setText(
            QCoreApplication.translate("MainWindow", "End Ping", None)
        )
        self.allEnd_Pings.setText(
            QCoreApplication.translate("MainWindow", "End All Ping", None)
        )

    retranslateUi


# x = int(eval(input('enter an int: ')))
# # if ((x % 2) == 0):5
# #     print('even')
# # else:
# #     print('odd')
# n = 1
# while x >= 1:
#     print(x)
#     n = n*(x)
#     x -= 1

# print(n)
