from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel,QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
   
class Card(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.cardContainer = QFrame(parent)
        # self.setObjectName(u"cardContainer")
        self.setMinimumSize(QSize(0, 0))
        self.setMaximumSize(QSize(16777215, 16777215))
        self.setStyleSheet(u"background-color: rgb(255, 250, 224);")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topBox = QFrame(self)
        self.topBox.setObjectName(u"topBox")
        self.topBox.setFrameShape(QFrame.StyledPanel)
        self.topBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.topBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 0)
        #####################
        # self.btnItemEdit = QPushButton(self.topBox)
        # self.btnItemEdit.setObjectName(u"btnItemEdit")
        # icon1 = QIcon()
        # icon1.addFile(u"./icons/icons8-edit-50.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.btnItemEdit.setIcon(icon1)

        # self.horizontalLayout_9.addWidget(self.btnItemEdit)
        #####################
        self.btnItemDelete = QPushButton(self.topBox)
        self.btnItemDelete.setObjectName(u"btnItemDelete")
        self.btnItemDelete.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"./icons/icons8-trash-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnItemDelete.setIcon(icon2)

        self.horizontalLayout_9.addWidget(self.btnItemDelete)

        self.urlvalueLineEdit = QLineEdit(self.topBox)
        self.urlvalueLineEdit.setObjectName(u"urlvalueLineEdit")
        self.urlvalueLineEdit.setMinimumSize(QSize(0, 0))
        self.urlvalueLineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.urlvalueLineEdit.setStyleSheet(u"QLineEdit#urlvalueLineEdit{background-color: rgb(255, 255, 255);padding:0px 2px;}")

        self.horizontalLayout_9.addWidget(self.urlvalueLineEdit)
        ####################
        self.btnItemSave = QPushButton(self.topBox)
        self.btnItemSave.setObjectName(u"btnItemSave")

        self.btnItemSave.setEnabled(False)
        self.btnItemSave.setStyleSheet("border:1px solid grey; padding:3px 3px 3px 3px;border-radius:3px;")

        icon3 = QIcon()
        icon3.addFile(u"./icons/icons8-save-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnItemSave.setIcon(icon3)
        self.btnItemSave.setFlat(False)

        self.horizontalLayout_9.addWidget(self.btnItemSave)
        ################
        self.btnItemView = QPushButton(self.topBox)
        self.btnItemView.setObjectName(u"btnItemView")
        icon4 = QIcon()
        icon4.addFile(u"./icons/icons8-key-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnItemView.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.btnItemView)


        self.verticalLayout_13.addWidget(self.topBox)

        self.bottomBox = QFrame(self)
        self.bottomBox.setObjectName(u"bottomBox")
        self.bottomBox.setFrameShape(QFrame.StyledPanel)
        self.bottomBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.bottomBox)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 5, 5)
        self.usernameFrame = QFrame(self.bottomBox)
        self.usernameFrame.setObjectName(u"usernameFrame")
        self.usernameFrame.setFrameShape(QFrame.StyledPanel)
        self.usernameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.usernameFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.usernameFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.uservalueLineEdit = QLineEdit(self.usernameFrame)
        self.uservalueLineEdit.setObjectName(u"uservalueLineEdit")
        self.uservalueLineEdit.setStyleSheet(u"QLineEdit#uservalueLineEdit{background-color: rgb(255, 255, 255);padding:0px 2px;}")

        self.horizontalLayout_5.addWidget(self.uservalueLineEdit)


        self.horizontalLayout_10.addWidget(self.usernameFrame)

        self.emailFrame = QFrame(self.bottomBox)
        self.emailFrame.setObjectName(u"emailFrame")
        self.emailFrame.setFrameShape(QFrame.StyledPanel)
        self.emailFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.emailFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.emailFrame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.emailvalueLineEdit = QLineEdit(self.emailFrame)
        self.emailvalueLineEdit.setObjectName(u"emailvalueLineEdit")
        self.emailvalueLineEdit.setStyleSheet(u"QLineEdit#emailvalueLineEdit{background-color: rgb(255, 255, 255);padding:0px 2px;}")

        self.horizontalLayout_6.addWidget(self.emailvalueLineEdit)


        self.horizontalLayout_10.addWidget(self.emailFrame)

        self.passFrame = QFrame(self.bottomBox)
        self.passFrame.setObjectName(u"passFrame")
        self.passFrame.setFrameShape(QFrame.StyledPanel)
        self.passFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.passFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.passFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.passvalueLineEdit = QLineEdit(self.passFrame)
        self.passvalueLineEdit.setObjectName(u"passvalueLineEdit")
        self.passvalueLineEdit.setStyleSheet(u"QLineEdit#passvalueLineEdit{background-color: rgb(255, 255, 255);padding:0px 2px;}")

        self.horizontalLayout_7.addWidget(self.passvalueLineEdit)


        self.horizontalLayout_10.addWidget(self.passFrame)


        self.verticalLayout_13.addWidget(self.bottomBox)

        self.card_index = None

        ########
        # self.btnItemEdit.setText("")
        self.btnItemDelete.setText("")
        self.btnItemSave.setText("")
        self.btnItemView.setText("")
        ###########
        self.label_8.setText(u"USERNAME : ")
        self.label_9.setText(u"EMAIL :  ")
        self.label_10.setText(u"PASSWORD : ")



