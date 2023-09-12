from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
# from PySide6.QtGui import 
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget, QLineEdit, QFormLayout)

class ValidateKey(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        if not self.objectName():
            self.setObjectName(u"Form")
        self.setWindowTitle( u"Enter the Secure KEY")
        self.resize(635, 90)
        self.setMinimumSize(QSize(635, 90))
        self.setMaximumSize(QSize(635, 90))
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 5, -1, -1)
        self.enterKeyLabel = QLabel(self)
        self.enterKeyLabel.setObjectName(u"enterKeyLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.enterKeyLabel)

        self.enterKeyLineEdit = QLineEdit(self)
        self.enterKeyLineEdit.setObjectName(u"enterKeyLineEdit")
        self.enterKeyLineEdit.setClearButtonEnabled(True)
        self.enterKeyLineEdit.setStyleSheet(u"QLineEdit#enterKeyLineEdit{padding:1px 3px; font-size:15px;}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.enterKeyLineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnCancel = QPushButton(self.frame)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.horizontalSpacer = QSpacerItem(450, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnKeySubmit = QPushButton(self.frame)
        self.btnKeySubmit.setObjectName(u"btnKeySubmit")

        self.horizontalLayout.addWidget(self.btnKeySubmit)


        self.verticalLayout.addWidget(self.frame)

        QMetaObject.connectSlotsByName(self)

        self.card_id = None

        self.btnCancel.clicked.connect(lambda:self.close())
        self.enterKeyLabel.setText(u"Enter Key :")
        self.btnCancel.setText(u"CANCEL THIS")
        self.btnKeySubmit.setText(u"PROCEED IT")




