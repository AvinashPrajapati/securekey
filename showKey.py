# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'showKey.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget,QMainWindow)

import time 
from subMain import Ui_MainWindow as mainWindow
from utils.enc_dec import generate_key
from utils.process_state import read_ini_file, setState

# mainWindow = Ui_MainWindow

class Ui_Form(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(729, 90)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.lineEditKey = QLineEdit(self.frame)
        self.lineEditKey.setObjectName(u"lineEditKey")
        self.lineEditKey.setMinimumSize(QSize(228, 0))
        self.lineEditKey.setStyleSheet(u"QLineEdit#lineEditKey{padding:1px 3px; font-size:15px;}")
        self.lineEditKey.setReadOnly(True)
        self.lineEditKey.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.lineEditKey)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonClear = QPushButton(self.frame_2)
        self.pushButtonClear.setObjectName(u"pushButtonClear")

        self.horizontalLayout_2.addWidget(self.pushButtonClear)

        self.horizontalSpacer = QSpacerItem(416, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButtonConfirm = QPushButton(self.frame_2)
        self.pushButtonConfirm.setObjectName(u"pushButtonConfirm")

        self.horizontalLayout_2.addWidget(self.pushButtonConfirm)


        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)

        self.uiWidget = Form

        QMetaObject.connectSlotsByName(Form)


    # setupUi

        self.pushButtonClear.clicked.connect(lambda: self.cancelSetup(Form))
        self.pushButtonConfirm.clicked.connect(lambda: self.confirmSetup(Form))
        self.pushButton.clicked.connect(self.on_copy_button_clicked)



    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Make sure to: save or write this KEY", None))
        self.label.setText(QCoreApplication.translate("Form", u"SAVE THIS ENCREPTION KEY :", None))
        self.lineEditKey.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"COPY TO CLIPBOARD", None))
        self.pushButtonClear.setText(QCoreApplication.translate("Form", u"CANCEL SETUP", None))
        self.pushButtonConfirm.setText(QCoreApplication.translate("Form", u"HAVE YOU SAVED SUCCESSFULLY?", None))
    # retranslateUi
        ####setup key
        self.lineEditKey.setText(self.decodeKey())

    def decodeKey(self):
        decodedKey = generate_key().decode('utf-8')
        return decodedKey

    def cancelSetup(self, thisWindow):
        thisWindow.close()

    def confirmSetup(self, thisWindow):
        thisWindow.close()
        setState()
        time.sleep(1)

        self.widget = QMainWindow()
        self.mainWindow_ui = mainWindow()
        self.mainWindow_ui.setupUi(self.widget)
        self.widget.show()
    
    def on_copy_button_clicked(self):
        self.pushButton.setText(u"COPY SUCCESSFUL")
        self.copy_to_clipboard()
        QTimer.singleShot(1000, self.reset_copy_button_text)

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.lineEditKey.text())

    def reset_copy_button_text(self):
        self.pushButton.setText(u"COPY TO CLIPBOARD")


###########################################

import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)

    currentState = read_ini_file()
    # print(currentState)

    if currentState == 1:
        #show the mainui
        widget = QMainWindow()
        mainWindow_ui = mainWindow()
        mainWindow_ui.setupUi(widget)
        widget.show()
    else:
        window = QWidget()
        ui = Ui_Form()
        ui.setupUi(window)
        window.show()
    sys.exit(app.exec())