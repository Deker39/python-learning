import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from win1 import  Ui_Win1
from win2 import  Ui_Win2

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Win2()
ui.setupUi(Dialog)
Dialog.show()


def pushbutton_one():
    pass

ui.pushButton.clicked.connect(pushbutton_one)



sys.exit(app.exec_())
