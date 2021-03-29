import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from  win3 import  Ui_Win3

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Win3()
ui.setupUi(Dialog)

with open('tests2.json') as f:
    templates = json.load(f)

#Все закинуть в функцию и подлючить к кнопке
#когда кнопка клацает итератор увеличиваеться
# и переменные меняються и вопрос тоже
# когда вопросы закончаться поменять кнопку на закончить
# и результаты запистаь тоже в джисон

quest = templates["test"]["quests"]
ui.label_2.setText(str(quest[0]))

answer = templates["test"]['answer'][0]
ui.radioButton.setText(str(answer[1]))
ui.radioButton_2.setText(str(answer[0]))
ui.radioButton_3.setText(str(answer[2]))

for x in range(len(templates["test"]['answer'])):
    kek = templates["test"]['answer'][x]
    print(kek[0],kek[1],kek[2])

# for x in templates["quests"]['answer'][0]:
#     print(x)
    # text = str(x)

Dialog.show()





sys.exit(app.exec_())