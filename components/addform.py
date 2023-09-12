import time
from PySide6.QtCore import QMetaObject, QSize
# from PySide6.QtGui import ()
from PySide6.QtWidgets import (QFormLayout, QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class addData(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(361, 176)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        #################
        #label
        self.urlNameLabel = QLabel(self)
        self.urlNameLabel.setObjectName(u"urlNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.urlNameLabel)
        #linedit
        self.urlNameLineEdit = QLineEdit(self)
        self.urlNameLineEdit.setObjectName(u"urlNameLineEdit")
        self.urlNameLineEdit.setStyleSheet("QLineEdit#urlNameLineEdit{padding: 1px 3px;}")
        self.urlNameLineEdit.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.urlNameLineEdit)
        ##########

        self.usernameLabel = QLabel(self)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.usernameLabel)

        self.usernameLineEdit = QLineEdit(self)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setStyleSheet("QLineEdit#usernameLineEdit{padding: 1px 3px;}")
        self.usernameLineEdit.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.usernameLineEdit)

        self.emailLabel = QLabel(self)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(self)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setStyleSheet("QLineEdit#emailLineEdit{padding: 1px 3px;}")
        self.emailLineEdit.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.emailLineEdit)

        self.passwordLabel = QLabel(self)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setStyleSheet("QLineEdit#passwordLineEdit{padding: 1px 3px;}")
        self.passwordLineEdit.setClearButtonEnabled(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.passwordLineEdit)

        #label
        self.keyLabel = QLabel(self)
        self.keyLabel.setObjectName(u"keyLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.keyLabel)
        #linedit
        self.keyLineEdit = QLineEdit(self)
        self.keyLineEdit.setObjectName(u"keyLineEdit")
        self.keyLineEdit.setStyleSheet("QLineEdit#keyLineEdit{padding: 1px 3px;}")
        self.keyLineEdit.setClearButtonEnabled(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.keyLineEdit)
        ##########


        self.verticalLayout.addLayout(self.formLayout)

        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)

        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.btnSafeClose = QPushButton(self.frame)
        self.btnSafeClose.setObjectName(u"btnSafeClose")

        self.horizontalLayout.addWidget(self.btnSafeClose)

        self.horizontalSpacer = QSpacerItem(158, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnAddSave = QPushButton(self.frame)
        self.btnAddSave.setObjectName(u"btnAddSave")
        self.btnAddSave.setMinimumSize(QSize(75, 24))
        self.btnAddSave.setMaximumSize(QSize(75, 24))

        self.horizontalLayout.addWidget(self.btnAddSave)


        self.verticalLayout.addWidget(self.frame)

        
        self.widget = self #to access the widget ;)
        self.mainWindow = None  # to access mainWindow


        QMetaObject.connectSlotsByName(self)

        self.setWindowTitle(u"Secure your password ( credentials ) ")
        self.urlNameLabel.setText(u"Url Name :",)
        self.usernameLabel.setText(u"Username :")
        self.emailLabel.setText(u"Email :")
        self.passwordLabel.setText(u"Password :")
        self.keyLabel.setText(u"Encreption Key :")
        self.btnSafeClose.setText(u"SAFE CLOSE")
        self.btnAddSave.setText(u"SAVE THIS")

        self.btnSafeClose.clicked.connect(lambda: self.close())
    
    

        #create a card

        # print(self.mainWindow.scrollVerticalLayout)
        # print(self.mainWindow.scrollVerticalLayout.count())


        # verticalLayoutChildren = []
        # for i in range(0, self.mainWindow.scrollVerticalLayout.count()):
        #     item = self.mainWindow.scrollVerticalLayout.itemAt(i)
        #     # print(item.widget())
        #     if item.widget() is not None:
        #         verticalLayoutChildren.append(item.widget())
        # print(verticalLayoutChildren)


        # for index, obj in enumerate(verticalLayoutChildren):
        #     # print(obj)
        #     self.mainWindow.scrollVerticalLayout.removeRow(obj)
        # # then insert data
  
        # self.mainWindow.data_list = all_data()
        # self.mainWindow.load_all(listData=self.mainWindow.data_list)
        # # print('done...')
       
        time.sleep(0.5)

        self.close()