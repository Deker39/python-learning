import sys
import json
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)

x = 0

from win1 import  Ui_Win1
from win2 import  Ui_Win2
from  win3 import  Ui_Win3
from  win4 import  Ui_Win4

app = QtWidgets.QApplication(sys.argv)
Dialog1 = QtWidgets.QDialog()
ui1 = Ui_Win1()
ui1.setupUi(Dialog1)

Dialog1.show()



def pushbutton_one():
    #без этого окна не открываються, гы
    global Dialog2
    global Dialog4
    global chois_test

    # запуск вин2
    Dialog2 = QtWidgets.QDialog()
    ui2 = Ui_Win2()
    ui2.setupUi(Dialog2)

    #  запуск вин4
    Dialog4 = QtWidgets.QDialog()
    ui4 = Ui_Win4()
    ui4.setupUi(Dialog4)
    # закрытие первого окна открытие четвертого
    Dialog1.close()
    Dialog4.show()

    # запись и возрать название теста(json file)
    def input_chois_test():
        chois_test = ui4.edit_test.text()
        return  chois_test

    #  Нажатие "ok" , переход на второе окно
    def pushbutton_return_one_ok():
        # input_chois_test()
        Dialog4.close()
        Dialog2.show()

    # Нажатие "cancel" возрат на первое окно
    def pushbutton_return_one_cancle():
        Dialog4.close()
        Dialog1.show()

    # Подключение кнопок
    ui4.ok_button.clicked.connect(pushbutton_return_one_ok)
    ui4.cancel_button.clicked.connect(pushbutton_return_one_cancle)

    # Ввод вопроса и фооматирование его под json file
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

    # Нажатие "дабвить", сохранение json file и преход на первое окно
    def pushbutton_return_add():
        input_question()
        Dialog2.close()
        Dialog1.show()

    # Подключение кнопоки
    ui2.button_add.clicked.connect(pushbutton_return_add)

def pushbutton_two():
    global Dialog3
    global Dialog4
    global chois_test
    # global x

    #  запуск вин3
    Dialog3 = QtWidgets.QDialog()
    ui3 = Ui_Win3()
    ui3.setupUi(Dialog3)

    #  запуск вин4
    Dialog4 = QtWidgets.QDialog()
    ui4 = Ui_Win4()
    ui4.setupUi(Dialog4)
    # закрытие первого окна открытие четвертого
    Dialog1.close()
    Dialog4.show()

    # запись и возрать название теста(json file)
    def input_chois_test():
        chois_test = ui4.edit_test.text()
        return  chois_test

    #  Нажатие "ok" , переход на второе окно
    def pushbutton_return_one_ok():
        Dialog4.close()
        Dialog3.show()
        # output()

    # Нажатие "cancel" возрат на первое окно
    def pushbutton_return_one_cancle():
        # input_chois_test()
        Dialog4.close()
        Dialog1.show()

    # Подключение кнопок
    ui4.ok_button.clicked.connect(pushbutton_return_one_ok)
    ui4.cancel_button.clicked.connect(pushbutton_return_one_cancle)

    #Сделат так чтобы выводило с json
    # и все пустить через for
    # Здесь нихуя не работает
    #
    def output():
        json_file = '{0}.json'.format(input_chois_test())
        with open(json_file) as f:
            templates = json.load(f)

        global x
        x += 1
        print('x:',x )
        # print(on_click(x))
        quest = templates["test"]["quests"]
        # print(len(templates["test"]["quests"]))
        if x >= len(templates["test"]["quests"]):
            Dialog3.close()
            Dialog1.show()
        else:

            ui3.label_2.setText(quest[x])
            answer = templates["test"]['answer'][x]
            ui3.radioButton.setText(str(answer[0]))
            ui3.radioButton_2.setText(str(answer[1]))
            ui3.radioButton_3.setText(str(answer[2]))

    ui3.pushButton.clicked.connect(output)

def pushbutton_three():
    pass

ui1.add_button.clicked.connect(pushbutton_one)
ui1.decide_button.clicked.connect(pushbutton_two)
ui1.look_button.clicked.connect(pushbutton_three)

sys.exit(app.exec_())