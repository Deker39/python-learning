import sys
import json
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)

from win1 import  Ui_Win1
from win2 import  Ui_Win2
from  win3 import  Ui_Win3
from  win4 import  Ui_Win4

app = QtWidgets.QApplication(sys.argv)
Dialog2 = QtWidgets.QDialog()
ui = Ui_Win1()
ui.setupUi(Dialog2)
Dialog2.show()

def push_button_one ():
    global Dialog2
    global Dialog4
    global Dialog2
    Dialog4 = QtWidgets.QDialog()
    ui4 = Ui_Win4()
    ui4.setupUi(Dialog4)
    Dialog1.close()
    Dialog4.show()

    def push_button_ok ():
        Dialog4.close()
        Dialog2.show()

    Dialog2 = QtWidgets.QDialog()
    ui2 = Ui_Win2()
    ui2.setupUi(Dialog2)

    ui4.ok_button.clicked.connect(push_button_ok)
def push_button_two ():
    print("Нажал кнопку два")
def push_button_three ():
    print("Нажал кнопу три")

ui.add_button.clicked.connect(push_button_one)
ui.decide_button.clicked.connect(push_button_two)
ui.look_button.clicked.connect(push_button_three)


sys.exit(app.exec_())
