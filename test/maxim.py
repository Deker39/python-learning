# -*- coding: utf-8 -*-

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

x = 0
i = 0

app = QtWidgets.QApplication(sys.argv)
Dialog1 = QtWidgets.QDialog()
ui1 = Ui_Win1()
ui1.setupUi(Dialog1)
Dialog1.show()

def push_button_one():
    global Dialog2
    global Dialog4

    Dialog2 = QtWidgets.QDialog()
    ui2 = Ui_Win2()
    ui2.setupUi(Dialog2)

    Dialog4 = QtWidgets.QDialog()
    ui4 = Ui_Win4()
    ui4.setupUi(Dialog4)

    Dialog1.close()
    Dialog4.show()

    def push_button_ok ():
        # print(input_chois_name_test())
        Dialog4.close()
        Dialog2.show()

    def push_button_cancle ():
        Dialog4.close()
        Dialog1.show()

    def push_button_add():
        input_question()
        Dialog2.close()
        Dialog1.show()

    def input_chois_name_test():
        chois_name_test = ui4.edit_test.text()
        return chois_name_test

    def input_question():
        question = []
        answer = []
        true_answer =[]

        question.append(ui2.text_quest.toPlainText())
        answer.append(list(ui2.text_answer.toPlainText().split('\n')))
        true_answer.append(ui2.text_true_answer.toPlainText())

        # quest - value
        quest = {"quests":question,
                 "answer":answer,
                 "true_answer":true_answer
                 }
        # test - key
        # test:quest
        to_json = {'test': quest}

        json_file  = '{0}.json'.format(input_chois_name_test())

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

    ui2.button_add.clicked.connect(push_button_add)

    ui4.ok_button.clicked.connect(push_button_ok)
    ui4.cancel_button.clicked.connect(push_button_cancle)

def push_button_two():
    global Dialog3
    global Dialog4

    Dialog3 = QtWidgets.QDialog()
    ui3 = Ui_Win3()
    ui3.setupUi(Dialog3)

    Dialog4 = QtWidgets.QDialog()
    ui4 = Ui_Win4()
    ui4.setupUi(Dialog4)

    Dialog1.close()
    Dialog4.show()

    def input_chois_test():
        chois_test = ui4.edit_test.text()
        return  chois_test

    def push_button_ok ():
        Dialog4.close()
        Dialog3.show()
        output()

    def push_button_cancle ():
        Dialog4.close()
        Dialog1.show()

    def push_button_next():
        output()
        user_answer_radiobutton()


        # Dialog3.close()
        # Dialog1.show()

    def output():
        json_file = '{0}.json'.format(input_chois_test())
        with open(json_file) as f:
            templates = json.load(f)

        global x

        if x >= len(templates['test']['quests']):
            Dialog3.close()
            Dialog1.show()
        else:
            ui3.label_2.setText(templates['test']['quests'][x])
            answer = templates['test']['answer'][x]
            ui3.radioButton.setText(answer[0])
            ui3.radioButton_2.setText(answer[1])
            ui3.radioButton_3.setText(answer[2])

        x += 1
        if x == len(templates["test"]["quests"]):
            ui3.pushButton.setText("ЗАВЕРШИТЬ")

    def user_answer_radiobutton():
        json_file = '{0}.json'.format(input_chois_test())
        with open(json_file) as f:
            templates = json.load(f)

        global i

        answer = templates["test"]['answer'][i]
        user_answer = []
        if ui3.radioButton.isChecked():
            print(answer[0])
            user_answer.append(answer[0])
        elif ui3.radioButton_2.isChecked():
            print(answer[1])
            user_answer.append(answer[1])
        elif ui3.radioButton_3.isChecked():
            print(answer[2])
            user_answer.append(answer[2])
        i += 1

        to_json = {'user_answer': user_answer}

        json_file  = '{0}_answer.json'.format(input_chois_test())
        # каждый раз удалять файл
        #
        if os.path.isfile(json_file) and os.access(json_file,os.R_OK):
            with open(json_file) as f:
                data = json.load(f)

            data['user_answer'].extend(user_answer)
            print(data)

            with open(json_file, 'w') as f:
                json.dump(data, f,sort_keys=True, indent=3,ensure_ascii=False )
        else:
            with open(json_file, 'w') as f:
                json.dump(to_json, f,sort_keys=True, indent=3,ensure_ascii=False )

    ui4.ok_button.clicked.connect(push_button_ok)
    ui4.cancel_button.clicked.connect(push_button_cancle)


    ui3.pushButton.clicked.connect(push_button_next)


def push_button_three ():
    print("Нажал кнопу три")

ui1.add_button.clicked.connect(push_button_one)
ui1.decide_button.clicked.connect(push_button_two)
ui1.look_button.clicked.connect(push_button_three)


sys.exit(app.exec_())
