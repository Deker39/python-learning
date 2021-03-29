import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from win1 import  Ui_Win1
from win21 import  Ui_Win2
import json

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Win2()
ui.setupUi(Dialog)
Dialog.show()


def pushbutton_one():
    global Dialog1
    Dialog1 = QtWidgets.QDialog()
    ui = Ui_Win2()
    ui.setupUi(Dialog1)
    Dialog.close()
    Dialog1.show()


    def input_question():
        text = ui.textEdit.toPlainText()

        # quest = {"quests":question,
        #          "answer":answer,
        #          "true_answer":true_answer
        #          }
        #
        to_json = {'test': text}

        with open('tests2.json', 'w') as f:
            json.dump(to_json, f,sort_keys=True, indent=3,ensure_ascii=False )
        print(text)

    def pushbutton_return_one():
        input_question()
        Dialog1.close()
        Dialog.show()

    ui.pushButton.clicked.connect(pushbutton_return_one)

ui.pushButton.clicked.connect(pushbutton_one)
sys.exit(app.exec_())
