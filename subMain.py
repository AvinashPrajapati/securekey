# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordKbDbRF.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication, QMetaObject, QRect, QSize
    )
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QApplication, QFrame, QHBoxLayout, QLabel, 
    QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget, QFormLayout
    )

from components.errorWindow import errorWindow
from components.card import Card
from components.validate import ValidateKey
from components.addform import addData

from utils.actions import encrypted_str,decrypted_str, insert_data, all_data, delete_single, return_single_data, update_item
from utils.extras import get_updated_date, get_url
import time
from datetime import date, datetime

class Ui_MainWindow(object):

    def __init__(self) -> None:
        self.add_data = addData()
        # directly attached to main ui
        self.add_data.btnAddSave.clicked.connect(self.addData)

        self.keyInput_UI = None

        self.error_ui = None

        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 720)
        MainWindow.setMinimumSize(QSize(700, 400))
        MainWindow.setMaximumSize(QSize(880, 850))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 0)
        self.topFrame = QFrame(self.centralwidget)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setMinimumSize(QSize(0, 0))
        self.topFrame.setMaximumSize(QSize(16777215, 40))
        self.topFrame.setStyleSheet(u"QFrame#topFrame{background-color:#474747; border:1px solid #aaaaaa;}")
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 3, 5, 3)
        self.label = QLabel(self.topFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel#label{background-color:transparent; color:#ffffff;font-weight:bold;}")

        self.horizontalLayout.addWidget(self.label)

        self.btnSortDate = QPushButton(self.topFrame)
        self.btnSortDate.setObjectName(u"btnSortDate")

        self.horizontalLayout.addWidget(self.btnSortDate)

        self.btnSortUrl = QPushButton(self.topFrame)
        self.btnSortUrl.setObjectName(u"btnSortUrl")
        self.btnSortUrl.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btnSortUrl)

        self.horizontalSpacer = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.topFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel#label_2{background-color:transparent; color:#ffffff;font-weight:bold;}")

        self.horizontalLayout.addWidget(self.label_2)

        self.btnAddItem = QPushButton(self.topFrame)
        self.btnAddItem.setObjectName(u"btnAddItem")
        self.btnAddItem.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"./icons/icons8-plus-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAddItem.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnAddItem)


        self.verticalLayout.addWidget(self.topFrame)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color:#474747;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 814, 661))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        #############QVBoxLayout -> Form Layut
        self.scrollVerticalLayout = QFormLayout()
        self.scrollVerticalLayout.setSpacing(5)
        self.scrollVerticalLayout.setObjectName(u"scrollVerticalLayout")
        self.scrollVerticalLayout.setContentsMargins(5, 5, 5, 5)
        # ui card
        

        #adding card ui -> for loop
        # self.card1 = Card(self.scrollAreaWidgetContents)
        # # self.card1.btnItemView.clicked.connect(self.showkey)
        # self.scrollVerticalLayout.addRow(self.card1)



        # self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.scrollVerticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_4.addLayout(self.scrollVerticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #########
        self.btnAddItem.clicked.connect(self.show_addData_form)
        self.btnSortDate.clicked.connect(self.sort_by_date)
        self.btnSortUrl.clicked.connect(self.sort_by_url)

        ##### add cards in it here
        ######load all data on start
        self.data_list = all_data()
        # print(self.data_list)
        self.load_cardList(dataList=all_data())
        #######

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Secure Key", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"  SORT BY:  ", None))
        self.btnSortDate.setText(QCoreApplication.translate("MainWindow", u"DATE ADDED", None))
        self.btnSortUrl.setText(QCoreApplication.translate("MainWindow", u"URL NAME", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"  ADD ITEM :  ", None))
        self.btnAddItem.setText("")
        # set some parameters
        self.add_data.mainWindow = self
    # retranslateUi

    def show_addData_form(self):
        self.add_data.show()
    def load_cardList(self, dataList):
        for _, item in enumerate(dataList):
            card = Card(self.scrollAreaWidgetContents)
            card.card_index = item.doc_id
            card.setObjectName(f"cardContainer_{card.card_index}")
            
            ##### btn modification
            card.btnItemDelete.setObjectName(f"btnItemDelete_{card.card_index}")
            # card.btnItemEdit.setObjectName(f"btnItemEdit_{card.card_index}")
            card.btnItemSave.setObjectName(f"btnItemSave_{card.card_index}")
            card.btnItemView.setObjectName(f"btnItemView_{card.card_index}")

            card.btnItemDelete.clicked.connect(self.delListItem)
            # card.btnItemEdit.clicked.connect(self.editListItem)
            card.btnItemSave.clicked.connect(self.saveListItem)
            card.btnItemView.clicked.connect(self.viewListItem)

            #------decryption
            card.urlvalueLineEdit.setReadOnly(True)

            card.uservalueLineEdit.setEnabled(False)
            card.emailvalueLineEdit.setEnabled(False)
            card.passvalueLineEdit.setEnabled(False)

            ##### input modification
            card.urlvalueLineEdit.setText(item["url"])

            self.scrollVerticalLayout.addRow(card)

    def viewListItem(self):
        item = QApplication.focusWidget().objectName()
        item_id = item[-1:]
        cardlist = self.returnCardList()
        carditem = self.returnCardItem(cardlist, item_id)
        # card_children = carditem.children()[1].children()
        # card_children[4].setEnabled(False)
        # card_children[4].setStyleSheet("border:1px solid grey; padding:3px 3px 3px 3px;border-radius:3px;")

        self.keyInput_UI = ValidateKey()
        self.keyInput_UI.btnKeySubmit.clicked.connect(lambda: self.valid_key(carditem))
        self.keyInput_UI.show()

    def valid_key(self,carditem):
        # print(carditem)
        key = self.keyInput_UI.enterKeyLineEdit.text()
        # print(key)
        card_children = carditem.children()[1].children()
        card_bottom_children = carditem.children()[2].children()
        # print(card_children)
        # # make editbtn disabled and save btn enabled
        
        card_url_val = card_children[2].text()
        card_dataset = return_single_data(card_url_val)
        # # load correct data
        # print(card_dataset)
        try:
            card_bottom_children[1].children()[2].setText(f"{decrypted_str(key, card_dataset[0]['username'])}")
            card_bottom_children[2].children()[2].setText(f"{decrypted_str(key,card_dataset[0]['email'])}")
            card_bottom_children[3].children()[2].setText(f"{decrypted_str(key,card_dataset[0]['password'])}")
            # then enable url
            card_children[2].setReadOnly(False)
            # then enable line edit
            card_bottom_children[1].children()[2].setEnabled(True)
            card_bottom_children[2].children()[2].setEnabled(True)
            card_bottom_children[3].children()[2].setEnabled(True)

            # then clear and close
            self.keyInput_UI.enterKeyLineEdit.clear()
            self.keyInput_UI.close()

            # change the view to disabled
            card_children[4].setEnabled(False)
            card_children[4].setStyleSheet("border:1px solid grey; padding:3px 3px 3px 3px;border-radius:3px;")

            # change save btn
            card_children[3].setEnabled(True)
            card_children[3].setStyleSheet("")


        except Exception as error:
            # print(error)
            self.error_ui = errorWindow()
            self.error_ui.plainTextEdit.setPlainText("The KEY is Invalid! , If forgotten the KEY then DATA can't be recovered... Sorry!")
            self.error_ui.show()

        # # modify line edit
        # card_children[2].setReadOnly(False)
        # # set enabled linedit

        # card_children[3].setEnabled(True)
        # card_children[3].setStyleSheet("")

    def saveListItem(self):
        item = QApplication.focusWidget().objectName()
        item_id = item[-1:]
        # print(item_id)

        cardlist = self.returnCardList()
        carditem = self.returnCardItem(cardlist, item_id)
        card_children = carditem.children()[1].children()
        card_url_val = card_children[2].text()

        # self.keyInput_UI = None
        self.keyInput_UI = ValidateKey()
        # self.keyInput_UI.enterKeyLineEdit
        self.keyInput_UI.btnKeySubmit.clicked.connect(lambda: self.update_card(carditem,item_id))
        self.keyInput_UI.show()

    def update_card(self, carditem, item_id):

        key = self.keyInput_UI.enterKeyLineEdit.text()
        card_children = carditem.children()[1].children()
        card_bottom_children = carditem.children()[2].children()
        # print("url:", item_id)
        # print(card_children)
        # # make editbtn disabled and save btn enabled
        
        

        try:
            new_url_val = card_children[2].text()
            username = encrypted_str(key, card_bottom_children[1].children()[2].text())
            email = encrypted_str(key, card_bottom_children[2].children()[2].text())
            password = encrypted_str(key, card_bottom_children[3].children()[2].text())

            current_date = date.today()
            # Format the date as "Month day, year"
            formatted_date = current_date.strftime("%A | %B %d %Y")
            # first update data
            new_data = {
                'url':new_url_val,
                'username':username,
                'email':email,
                'password':password,
                'updated':formatted_date,
            } 

            update_item(new_data, item_id)


            # then enable url
            card_children[2].setText(new_url_val)
            card_children[2].setReadOnly(True)
            # then enable line edit
            card_bottom_children[1].children()[2].clear()
            card_bottom_children[2].children()[2].clear()
            card_bottom_children[3].children()[2].clear()
            card_bottom_children[1].children()[2].setEnabled(False)
            card_bottom_children[2].children()[2].setEnabled(False)
            card_bottom_children[3].children()[2].setEnabled(False)

            # set the new data to card

            # change the view to disabled
            card_children[4].setEnabled(True)
            card_children[4].setStyleSheet("")

            # change save btn
            card_children[3].setEnabled(False)
            card_children[3].setStyleSheet("border:1px solid grey; padding:3px 3px 3px 3px;border-radius:3px;")

            # then clear and close
            self.keyInput_UI.enterKeyLineEdit.clear()
            self.keyInput_UI.close()

        except Exception as error:
            print(error)
            self.error_ui = errorWindow()
            self.error_ui.plainTextEdit.setPlainText("The KEY is Invalid! , If forgotten the KEY then DATA can't be recovered... Sorry!")
            self.error_ui.show()
    
    def delListItem(self):
        item = QApplication.focusWidget().objectName()
        item_id = item[-1:]
        #check on which item it is clicked
        cardlist = self.returnCardList()
        carditem = self.returnCardItem(cardlist, item_id)

        # print(carditem.children()[1].children()[2].text())
        card_url = carditem.children()[1].children()[2].text()
        delete_single(card_url)
        self.scrollVerticalLayout.removeRow(carditem)

    ### add data
    def addData(self):
        key = self.add_data.keyLineEdit.text()
        url = self.add_data.urlNameLineEdit.text()
        username = encrypted_str(key,self.add_data.usernameLineEdit.text())
        email = encrypted_str(key, self.add_data.emailLineEdit.text())
        password = encrypted_str(key, self.add_data.passwordLineEdit.text())
        inputdata = None
        # add date
        current_date = date.today()
        # Format the date as "Month day, year"
        formatted_date = current_date.strftime("%A | %B %d %Y")
        if (len(key))>2 :
            inputdata = {
                'url':url,
                'username':username,
                'email':email,
                'password':password,
                'updated':formatted_date,
            }
            insert_data(inputdata)
        new_data = all_data()
        self.reloadList(new_datalist=new_data)
        # clear the lineEdit
        self.add_data.keyLineEdit.clear()
        self.add_data.urlNameLineEdit.clear()
        self.add_data.usernameLineEdit.clear()
        self.add_data.emailLineEdit.clear()
        self.add_data.passwordLineEdit.clear()
        # close the ui
        self.add_data.close()
    
    def reloadList(self, new_datalist):
        cardlist = self.returnCardList()
        for item in cardlist:
            self.scrollVerticalLayout.removeRow(item)
        self.load_cardList(new_datalist)
    
    def returnCardList(self)->list:
        verticalLayoutChildren = []
        for i in range(0, self.scrollVerticalLayout.count()):
            item = self.scrollVerticalLayout.itemAt(i)
            if item.widget() is not None:
                verticalLayoutChildren.append(item.widget())
        return verticalLayoutChildren
    
    def returnCardItem(self, cardList:list, id:str):
        cardItem = None
        for index, obj in enumerate(cardList):
            if id == obj.objectName()[-1:]:
                cardItem = obj
        return cardItem

    def sort_by_date(self):
        datalist = all_data()
        # updated_date_str = item['updated'].split('|')[-1].strip()
        sorted_data = sorted(datalist, key=get_updated_date)
        self.reloadList(sorted_data)
    def sort_by_url(self):
        datalist = all_data()
        # updated_date_str = item['updated'].split('|')[-1].strip()
        sorted_data = sorted(datalist, key=get_url)
        self.reloadList(sorted_data)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())