# -*- coding: utf-8 -*-

import sys
import json
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from termcolor import colored

x = 0
i = 0
user_answer = []

from win1 import  Ui_Win1
from win2 import  Ui_Win2
from win3 import  Ui_Win3
from win4 import  Ui_Win4
from win5 import  Ui_Win5


app = QtWidgets.QApplication(sys.argv)
Dialog1 = QtWidgets.QDialog()
ui1 = Ui_Win1()
ui1.setupUi(Dialog1)
Dialog1.show()

def pushbutton_one():
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

    def input_chois_test():
        chois_test = ui4.edit_test.text()
        return  chois_test

    def pushbutton_return_one_ok():
        # input_chois_test()
        Dialog4.close()
        Dialog2.show()

    def pushbutton_return_one_cancle():
        Dialog4.close()
        Dialog1.show()



    def input_question():
        question = []
        answer = []
        true_answer =[]
        # запись в перменные
        question.append(ui2.text_quest.toPlainText())
        answer.append(list(ui2.text_answer.toPlainText().split('\n')))
        true_answer.append(ui2.text_true_answer.toPlainText())

        quest = {"quests":question,
                 "answer":answer,
                 "true_answer":true_answer
                 }

        to_json = {'test': quest}
        # использование фунцкии input_chois_test, для ввода
        # названия теста
        json_file = '{0}.json'.format(input_chois_test())
        print(json_file)

        # если тест есть и к нему есть доступ то,
        # скачиваем и добавляем к нему инфу и сохраныяем,
        # а если нету создаем новый
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

    def pushbutton_return():
        Dialog2.close()
        Dialog1.show()
        input_question()

    ui2.button_add.clicked.connect(pushbutton_return)

    ui4.ok_button.clicked.connect(pushbutton_return_one_ok)
    ui4.cancel_button.clicked.connect(pushbutton_return_one_cancle)

def pushbutton_two():
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

    def pushbutton_return_one_ok():
        Dialog4.close()
        Dialog3.show()
        output()

    def pushbutton_return_one_cancle():
        Dialog4.close()
        Dialog1.show()

    def pushbutton_return():
        radio_answer_user()
        output()

    def output():
        json_file = '{0}.json'.format(input_chois_test())
        with open(json_file) as f:
            templates = json.load(f)

        global x

        if x >= len(templates["test"]["quests"]):
            Dialog3.close()
            Dialog1.show()
        else:
            ui3.label_2.setText(templates['test']['quests'][x])
            # answer = templates["test"]['answer'][x]
            ui3.radioButton.setText(str(templates["test"]['answer'][x][0]))
            ui3.radioButton_2.setText(str(templates["test"]['answer'][x][1]))
            ui3.radioButton_3.setText(str(templates["test"]['answer'][x][2]))

        x += 1
        if x == len(templates["test"]["quests"]):
            ui3.pushButton.setText("ЗАВЕРШИТЬ")

    def radio_answer_user():
        json_file = '{0}.json'.format(input_chois_test())
        with open(json_file) as f:
            templates = json.load(f)
        global i
        answer = templates["test"]['answer'][i]
        global user_answer

        if ui3.radioButton.isChecked():
            print(answer[0])
            user_answer.append(answer[0])
        elif ui3.radioButton_2.isChecked():
            print(answer[1])
            user_answer.append(answer[1])
        elif ui3.radioButton_3.isChecked():
            print(answer[2])
            user_answer.append(answer[2])
        print('i:',i )
        i += 1
        to_json = {'user_answer': user_answer}
        json_file  = '{0}_answer.json'.format(input_chois_test())

        with open(json_file, 'w') as f:
            json.dump(to_json, f,sort_keys=True, indent=3,ensure_ascii=False )

    ui3.pushButton.clicked.connect(pushbutton_return)

    ui4.ok_button.clicked.connect(pushbutton_return_one_ok)
    ui4.cancel_button.clicked.connect(pushbutton_return_one_cancle)

def pushbutton_three():
    global Dialog5
    global Dialog4

    Dialog5 = QtWidgets.QDialog()
    ui5 = Ui_Win5()
    ui5.setupUi(Dialog5)

    Dialog4 = QtWidgets.QDialog()
    ui4 = Ui_Win4()
    ui4.setupUi(Dialog4)

    Dialog1.close()
    Dialog4.show()

    def input_chois_test():
        chois_test = ui4.edit_test.text()
        return  chois_test

    def pushbutton_return_one_ok():
        Dialog4.close()
        Dialog5.show()
        decision()

    def pushbutton_return_one_cancle():
        Dialog4.close()
        Dialog1.show()

    def pushbutton_return():
        Dialog5.close()
        Dialog1.show()

    def decision():

        new_x = []
        numbers_user_true_answer = 0

        json_file  = '{0}.json'.format(input_chois_test())
        with open(json_file) as f:
            templates_one = json.load(f)
        json_file_answer  = '{0}_answer.json'.format(input_chois_test())
        with open(json_file_answer) as f:
            templates_two = json.load(f)

        print(json_file,"\n",json_file_answer)

        for y in range(len(templates_one['test']['quests'])):
            if templates_two['user_answer'][y] == templates_one['test']['true_answer'][y]:
                new_x.append(templates_two['user_answer'][y])
                numbers_user_true_answer +=1
        print(new_x)
        # вывод названия теста
        ui5.listWidget.addItem(input_chois_test())
        ui5.listWidget.item(0).setTextAlignment(QtCore.Qt.AlignCenter)
        #  вывод вопросов зеленый красный
        for y in range(0,len(templates_one['test']['quests'])):
            if templates_two['user_answer'][y] == templates_one['test']['true_answer'][y]:
                ui5.listWidget.addItem(str(templates_one['test']['quests'][y]))
                ui5.listWidget.item(y+1).setForeground(QtGui.QColor("green"))
            else:
                ui5.listWidget.addItem(str(templates_one['test']['quests'][y]))
                ui5.listWidget.item(y+1).setForeground(QtGui.QColor("red"))

        # правильные ответы
        for y in range(0,len(templates_one['test']['true_answer'])):
            if templates_two['user_answer'][y] == templates_one['test']['true_answer'][y]:
                ui5.listWidget.addItem(str("Правильный ответ: {0}".format(templates_two['user_answer'][y])))
            else:
                ui5.listWidget.addItem(str("Не правильный ответ: {0}".format(templates_two['user_answer'][y])))

        # вывод количества правильных ответов
        ui5.listWidget.addItem(str("Правильных ответов {0}/{1}")
                               .format(numbers_user_true_answer,len(templates_one['test']['answer'])))



    ui5.pushButton_2.clicked.connect(pushbutton_return)

    ui4.ok_button.clicked.connect(pushbutton_return_one_ok)
    ui4.cancel_button.clicked.connect(pushbutton_return_one_cancle)

ui1.add_button.clicked.connect(pushbutton_one)
ui1.decide_button.clicked.connect(pushbutton_two)
ui1.look_button.clicked.connect(pushbutton_three)

sys.exit(app.exec_())





























