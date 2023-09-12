from PySide6.QtCore import QSize, QCoreApplication, QMetaObject
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QWidget, QTextEdit, QPlainTextEdit)

class errorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        if not self.objectName():
            self.setObjectName(u"errorWidget")
        self.resize(373, 70)
        self.setMaximumSize(QSize(373, 70))
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setPixmap(QPixmap(u"./icons/icons8-warning-48.png"))
        self.label.setScaledContents(False)

        self.horizontalLayout.addWidget(self.label)

        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setMinimumSize(QSize(290, 0))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 50))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit#plainTextEdit{background-color:#fff;padding:0px 5px;}")
        self.plainTextEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.plainTextEdit)
        QMetaObject.connectSlotsByName(self)

        self.setWindowTitle(QCoreApplication.translate("errorWidget", u"Got an Error", None))
        self.label.setText("")
