# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Win5(object):
    def setupUi(self, Win5):
        Win5.setObjectName("Win5")
        Win5.setFixedSize(480, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Win5.setWindowIcon(icon)
        Win5.setStyleSheet("background-color:    #e6ffff")
        self.label_2 = QtWidgets.QLabel(Win5)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 441, 39))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setToolTipDuration(-1)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color:#006080;")
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(Win5)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 440, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(Win5)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 346, 480, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Win5)
        QtCore.QMetaObject.connectSlotsByName(Win5)

    def retranslateUi(self, Win5):
        _translate = QtCore.QCoreApplication.translate
        Win5.setWindowTitle(_translate("Win5", "View"))
        self.label_2.setText(_translate("Win5", "??????????????????:"))
        self.pushButton_2.setText(_translate("Win5", "??????????????"))

