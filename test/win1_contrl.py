import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from win1 import  Ui_Win1
from win2 import  Ui_Win2
from  win3 import  Ui_Win3

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


    def input_question():
        question = []
        answer = []
        true_answer =[]
        question.append(ui.text_quest.toPlainText())
        answer.append(list(ui.text_answer.toPlainText().split('\n')))
        true_answer.append(ui.text_true_answer.toPlainText())

        quest = {"quests":question,
                 "answer":answer,
                 "true_answer":true_answer
                 }

        to_json = {'test': quest}

        with open('tests2.json', 'w') as f:
            json.dump(to_json, f,sort_keys=True, indent=3,ensure_ascii=False )
        print(quest)

    def pushbutton_return_one():
        input_question()
        Dialog1.close()
        Dialog.show()

    ui.button_add.clicked.connect(pushbutton_return_one)

def pushbutton_two():
    global Dialog2
    Dialog2 = QtWidgets.QDialog()
    ui = Ui_Win3()
    ui.setupUi(Dialog2)
    Dialog.close()

    def output():
        with open('tests2.json') as f:
            templates = json.load(f)
        quest = templates["test"]["quests"]
        ui.label_2.setText(quest[0])
        print(quest[0])
        answer = templates["test"]['answer'][0]
        ui.radioButton.setText(str(answer[1]))
        ui.radioButton_2.setText(str(answer[0]))
        ui.radioButton_3.setText(str(answer[2]))
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