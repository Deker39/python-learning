from PyQt5 import QtWidgets
from school_project.view_calculator import Ui_Calcalator
import sys

app = QtWidgets.QApplication(sys.argv)
Calcalator = QtWidgets.QDialog()
ui = Ui_Calcalator()
ui.setupUi(Calcalator)
Calcalator.show()

def click(num):
    display(text=num)
    print(num)

def clear():
    obj = ui.label_output
    obj.setText('0')

def dell():
    obj = ui.label_output
    text =  obj.text()
    obj.setText(text[:len(text)-1])

def display(text='0'):
    obj = ui.label_output
    text_old = obj.text()
    if text_old == "0":
        text_old =''
    text ="%s%s" % (text_old,text)
    obj.setText(str(text))


def equals():
    equation = ui.label_output.text()
    try:
        ans = eval(equation)

        ui.label_output.setText(str(ans))
    except:
        ui.label_output.setText("Wrong Input")




ui.pushButton_one.clicked.connect(lambda: click(num=1))
ui.pushButton_two.clicked.connect(lambda: click(num=2))
ui.pushButton_three.clicked.connect(lambda: click(num=3))
ui.pushButton_four.clicked.connect(lambda: click(num=4))
ui.pushButton_five.clicked.connect(lambda: click(num=5))
ui.pushButton_six.clicked.connect(lambda: click(num=6))
ui.pushButton_seven.clicked.connect(lambda: click(num=7))
ui.pushButton_eight.clicked.connect(lambda: click(num=8))
ui.pushButton_nine.clicked.connect(lambda: click(num=9))
ui.pushButton_zero.clicked.connect(lambda: click(num=0))
ui.pushButton_plus.clicked.connect(lambda: click(num="+"))
ui.pushButton_minus.clicked.connect(lambda: click(num="-"))
ui.pushButton_divided.clicked.connect(lambda: click(num="/"))
ui.pushButton_multiply.clicked.connect(lambda: click(num="*"))
ui.pushButton_dot.clicked.connect(lambda: click(num="."))
ui.pushButton_clear.clicked.connect(clear)
ui.pushButton_percent.clicked.connect(lambda: click(num="%"))
ui.pushButton_plus_minus.clicked.connect(lambda: click(num="-"))
ui.pushButton_equals.clicked.connect(equals)
ui.pushButton_del.clicked.connect(dell)

sys.exit(app.exec_())


