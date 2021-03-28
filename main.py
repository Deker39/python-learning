import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from view_course import  Ui_Dialog
import  nbu_api
import database
from datetime import datetime

name_table = ("nbu")
columns_table = ("r, txt, rate, cc, exchangedate")
column = 'cc'
column_data = 'exchangedate'
r1 = nbu_api.api_request_nbu()
request_api = r1.request_nbu_cours_today()
c1 = database



app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
ui.lineEdit.setMaxLength(3)

def pb():

    current_datetime = datetime.strftime(datetime.now(),('%d.%m.%Y'))
    print(current_datetime)
    data = c1.db().select_where(name_table,column_data,current_datetime)

    # for x in request_api:
    #     val = (x['r030'], x['txt'], x['rate'], x['cc'], x['exchangedate'])
    #     # sql = "INSERT INTO nbu ( r, txt, rate, cc, exchangedate) VALUES (%s,%s,%s,%s,%s)"
    #     c1.db().insert(name_table, columns_table, val)
    #     # c1.insert(name_table, columns_table, val)
    #     print(val)
    #
    # if current_datetime != data[0][5]:
    #
    #     pass
    # elif data[0][5] == current_datetime:
    currency_name = ui.lineEdit.text()
    j = c1.db().select_where(name_table, column, currency_name)
    ui.label.setText("Rate: " + j[0][3])

ui.pushButton.clicked.connect(pb)

sys.exit(app.exec_())
