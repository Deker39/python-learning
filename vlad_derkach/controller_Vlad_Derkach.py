import sys
from PyQt5 import QtWidgets
from  vlad_derkach.caclulator_Vlad_Derkach import Ui_Dialog



app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


def action_plus():
    text = ui.label_output.text()
    ui.label_output.setText(text + "+")

def action_minus():
    text = ui.label_output.text()
    ui.label_output.setText(text + "-")

def action_divided():
    text = ui.label_output.text()
    ui.label_output.setText(text + "/")

def action_multiply():
    text = ui.label_output.text()
    ui.label_output.setText(text + "*")

def action_dot():
    text = ui.label_output.text()
    ui.label_output.setText(text + ".")

def action_clear():
    ui.label_output.setText(" ")

def action_percent():
    text = ui.label_output.text()
    ui.label_output.setText(text + "%")

def action_plus_minus():
    pass
    # text = ui.label_output.text()
    #
    # # ui.label_output.setText(text + "-")
    # if text[:len(text)] == "+":
    #     ui.label_output.setText(text[:len(text)-1])
    #
    # # elif text[:len(text)] == "-" :
    #     ui.label_output.setText(text + "+")
    #     # ui.label_output.setText(text[:len(text) - 1])
    #     ui.label_output.setText(text + "-")
    # elif text[:len(text)] == "-":
    #     # ui.label_output.setText(text[:len(text) - 1])
    #     ui.label_output.setText(text + "+")
    # # Написта условие на минус и на плюс


def action_del():
    text = ui.label_output.text()
    ui.label_output.setText(text[:len(text)-1])

def action_equals():
    equation = ui.label_output.text()
    print(equation)
    try:
        ans = eval(equation)

        ui.label_output.setText(str(ans))
    except:
        ui.label_output.setText("Wrong Input")





def pushbutton_one():
    text = ui.label_output.text()
    ui.label_output.setText(text + "1")
def pushbutton_two():
    text = ui.label_output.text()
    ui.label_output.setText(text + "2")
def pushbutton_three():
    text = ui.label_output.text()
    ui.label_output.setText(text + "3")
def pushbutton_four():
    text = ui.label_output.text()
    ui.label_output.setText(text + "4")
def pushbutton_five():
    text = ui.label_output.text()
    ui.label_output.setText(text + "5")
def pushbutton_six():
    text = ui.label_output.text()
    ui.label_output.setText(text + "6")
def pushbutton_seven():
    text = ui.label_output.text()
    ui.label_output.setText(text + "7")
def pushbutton_eight():
    text = ui.label_output.text()
    ui.label_output.setText(text + "8")
def pushbutton_nine():
    text = ui.label_output.text()
    ui.label_output.setText(text + "9")
def pushbutton_zero():
    text = ui.label_output.text()
    ui.label_output.setText(text + "0")

if len(ui.label_output.text()) == 1:
    action_clear()
    ui.pushButton_one.clicked.connect(pushbutton_one)
    ui.pushButton_two.clicked.connect(pushbutton_two)
    ui.pushButton_three.clicked.connect(pushbutton_three)
    ui.pushButton_four.clicked.connect(pushbutton_four)
    ui.pushButton_five.clicked.connect(pushbutton_five)
    ui.pushButton_six.clicked.connect(pushbutton_six)
    ui.pushButton_seven.clicked.connect(pushbutton_seven)
    ui.pushButton_eight.clicked.connect(pushbutton_eight)
    ui.pushButton_nine.clicked.connect(pushbutton_nine)
    ui.pushButton_zero.clicked.connect(pushbutton_zero)

ui.pushButton_plus.clicked.connect(action_plus)
ui.pushButton_minus.clicked.connect(action_minus)
ui.pushButton_divided.clicked.connect(action_divided)
ui.pushButton_multiply.clicked.connect(action_multiply)
ui.pushButton_percent.clicked.connect(action_percent)
ui.pushButton_dot.clicked.connect(action_dot)
ui.pushButton_del.clicked.connect(action_del)
ui.pushButton_clear.clicked.connect(action_clear)
ui.pushButton_equals.clicked.connect(action_equals)
ui.pushButton_plus_minus.clicked.connect(action_plus_minus)

sys.exit(app.exec_())
