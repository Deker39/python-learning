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
Dialog = QtWidgets.QDialog()
ui = Ui_Win1()
ui.setupUi(Dialog)
Dialog.show()

def pushbutton_one():
    global Dialog1
    global Dialog4
    global chois_test
    Dialog4 = QtWidgets.QDialog()
    ui1 = Ui_Win4()
    ui1.setupUi(Dialog4)
    Dialog.close()
    Dialog4.show()

    def input_chois_test():
        chois_test = ui1.edit_test.text()
        print(chois_test)
        return  chois_test

    def pushbutton_ok():
        input_chois_test()
        Dialog4.close()
        Dialog.show()


    def pushbutton_return_one_ok():
        pushbutton_ok()
        Dialog4.close()
        Dialog1.show()

    def pushbutton_return_one_cancle():
        # pushbutton_ok()
        Dialog4.close()
        Dialog.show()

    Dialog1 = QtWidgets.QDialog()
    ui = Ui_Win2()
    ui.setupUi(Dialog1)

    ui1.ok_button.clicked.connect(pushbutton_return_one_ok)
    ui1.cancel_button.clicked.connect(pushbutton_return_one_cancle)


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

        json_file = '{0}.json'.format(input_chois_test())
        print(json_file)


        if os.path.isfile(json_file) and os.access(json_file,os.R_OK):
            with open(json_file) as f:
                data = json.load(f)

            data['test']['quests'].extend(question)
            data['test']['answer'].extend(answer)
            data['test']['true_answer'].extend(true_answer)
            print(data)

            with open(json_file, 'w') as f:
                json.dump(data, f,sort_keys=True, indent=3,ensure_ascii=False )

        else:
            with open(json_file, 'w') as f:
                json.dump(to_json, f,sort_keys=True, indent=3,ensure_ascii=False )

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


ui.add_button.clicked.connect(pushbutton_one)
ui.decide_button.clicked.connect(pushbutton_two)
# ui.look_button.clicked.connect(pushbutton_three)

sys.exit(app.exec_())