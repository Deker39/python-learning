from PyQt5 import QtWidgets
import sys
from maksim_samuchenko.caclulator_Maksim_Samuchenko import Ui_Calculator

app = QtWidgets.QApplication(sys.argv)
Calculator = QtWidgets.QDialog()
ui = Ui_Calculator()
ui.setupUi(Calculator)
Calculator.show()

def action_plus():
    text=ui.label_output.text()
    ui.label_output.setText(text+"+")

def action_minus():
    text=ui.label_output.text()
    ui.label_output.setText(text+"-")

def action_dot():
    text=ui.label_output.text()
    ui.label_output.setText(text+".")

def action_equals():
    equation = ui.label_output.text()
    try:
        ans = eval(equation)

        ui.label_output.setText(str(ans))
    except:
        ui.label_output.setText("Wrong Input")


def action_clear():
    ui.label_output.setText(" ")

def action_del():
    text=ui.label_output.text()
    ui.label_output.setText(text[:len(text)-1])

def action_multyply():
    text=ui.label_output.text()
    ui.label_output.setText(text+"*")

def action_dividet():
    text=ui.label_output.text()
    ui.label_output.setText(text+"/")

def action_bracket_left():
    text=ui.label_output.text()
    ui.label_output.setText(text+"(")

def action_bracket_right():
    text=ui.label_output.text()
    ui.label_output.setText(text+")")

def action_root():
    text=ui.label_output.text()
    ui.label_output.setText(text+"**")

def action_square_root():
    text=ui.label_output.text()
    ui.label_output.setText(text +  "**0.5")



def pushbutton_one():
    text=ui.label_output.text()
    ui.label_output.setText(text+"1")


def pushbutton_two():
    text=ui.label_output.text()
    ui.label_output.setText(text+"2")


def pushbutton_three():
    text=ui.label_output.text()
    ui.label_output.setText(text+"3")

def pushbutton_four():
    text=ui.label_output.text()
    ui.label_output.setText(text+"4")

def pushbutton_five():
    text=ui.label_output.text()
    ui.label_output.setText(text+"5")

def pushbutton_six():
    text=ui.label_output.text()
    ui.label_output.setText(text+"6")

def pushbutton_seven():
    text=ui.label_output.text()
    ui.label_output.setText(text+"7")

def pushbutton_eight():
    text=ui.label_output.text()
    ui.label_output.setText(text+"8")

def pushbutton_nine():
    text=ui.label_output.text()
    ui.label_output.setText(text+"9")

def pushbutton_zero():
    text=ui.label_output.text()
    ui.label_output.setText(text+"0")


ui.pushButton_plus.clicked.connect(action_plus)
ui.pushButton_minus.clicked.connect(action_minus)
ui.pushButton_dot.clicked.connect(action_dot)
ui.pushButton_equals.clicked.connect(action_equals)
ui.pushButton_clear.clicked.connect(action_clear)
ui.pushButton_del.clicked.connect(action_del)
ui.pushButton_multiply.clicked.connect(action_multyply)
ui.pushButton_divided.clicked.connect(action_dividet)
ui.pushButton_divided.clicked.connect(action_dividet)
ui.pushButton_bracket_left.clicked.connect(action_bracket_left)
ui.pushButton_bracket_right.clicked.connect(action_bracket_right)
ui.pushButton_square_root.clicked.connect(action_square_root)
ui.pushButton_plus_minus.clicked.connect(action_root)
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
# ui.pushButton_root.clicked.connect(action_root))





sys.exit(app.exec_())