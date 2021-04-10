# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(331, 373)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("test/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color:    #e6ffff")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 80, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#006080;")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 190, 311, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("QPushButton{\n"
"    color:#006080;\n"
"    background-color:#ccf2ff;\n"
"    border: none;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    color:#ffd9b3;\n"
"    background-color:#006080;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:#ff9933;\n"
"    background-color:#006080;\n"
"}")
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)
        self.decide_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decide_button.sizePolicy().hasHeightForWidth())
        self.decide_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.decide_button.setFont(font)
        self.decide_button.setStyleSheet("QPushButton{\n"
"    color:#006080;\n"
"    background-color:#ccf2ff;\n"
"    border: none;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    color:#ffd9b3;\n"
"    background-color:#006080;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:#ff9933;\n"
"    background-color:#006080;\n"
"}")
        self.decide_button.setObjectName("decide_button")
        self.verticalLayout.addWidget(self.decide_button)
        self.look_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.look_button.sizePolicy().hasHeightForWidth())
        self.look_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.look_button.setFont(font)
        self.look_button.setStyleSheet("QPushButton{\n"
"    color:#006080;\n"
"    background-color:#ccf2ff;\n"
"    border: none;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    color:#ffd9b3;\n"
"    background-color:#006080;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:#ff9933;\n"
"    background-color:#006080;\n"
"}")
        self.look_button.setObjectName("look_button")
        self.verticalLayout.addWidget(self.look_button)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.add_button, self.decide_button)
        Dialog.setTabOrder(self.decide_button, self.look_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Test"))
        self.label.setText(_translate("Dialog", "Тесты"))
        self.add_button.setText(_translate("Dialog", "ДОБАВИТЬ"))
        self.decide_button.setText(_translate("Dialog", "РЕШИТЬ"))
        self.look_button.setText(_translate("Dialog", "ПРОСМОТРЕТЬ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())