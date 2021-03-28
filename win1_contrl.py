import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from win1 import  Ui_Win1
from win2 import  Ui_Win2
from  win3 import  Ui_Win3

global text
# f = open("example.txt","r")

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Win1()
ui.setupUi(Dialog)
Dialog.show()

def pushbutton_one():
    global Dialog1
    Dialog1 = QtWidgets.QDialog()
    ui = Ui_Win2()
    ui.setupUi(Dialog1)
    Dialog.close()
    Dialog1.show()


    def input():
        text = ui.textEdit.toPlainText()
        f = open("example.txt", "w")
        f.write(text)
        f.close()
        print(text)

    def pushbutton_return_one():
        input()
        Dialog1.close()
        Dialog.show()

    ui.pushButton.clicked.connect(pushbutton_return_one)






















def pushbutton_two():
    global Dialog2
    Dialog2 = QtWidgets.QDialog()
    ui = Ui_Win3()
    ui.setupUi(Dialog2)
    Dialog.close()

    def output():
        f = open("example.txt","r")
        text1 = f.read()
        # x =
        f.close()
        ui.label_2.setText(text1)
        print(text1)
        # ui.label_2.setText(text)

    Dialog2.show()
    output()
    #закинуть текс в функцию оутпут

    def pushbutton_return_one():
        Dialog2.close()
        Dialog.show()

    ui.pushButton.clicked.connect(pushbutton_return_one)


ui.pushButton_1.clicked.connect(pushbutton_one)
ui.pushButton_2.clicked.connect(pushbutton_two)
# ui.pushButton_3.clicked.connect(pushbutton_three)

sys.exit(app.exec_())