# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_add_quest.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Win2(object):
    def setupUi(self, Win2):
        Win2.setObjectName("Win2")
        Win2.setWindowModality(QtCore.Qt.NonModal)
        Win2.setEnabled(True)
        # Win2.resize(500, 400)
        Win2.setFixedSize(500, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Win2.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Win2.sizePolicy().hasHeightForWidth())
        Win2.setSizePolicy(sizePolicy)
        Win2.setToolTipDuration(0)
        Win2.setStyleSheet("QDialog{\n"
"background: #e6ffff;\n"
"\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(Win2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_quest = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_quest.setFont(font)
        self.label_quest.setStyleSheet("color:#006080;")
        self.label_quest.setObjectName("label_quest")
        self.verticalLayout.addWidget(self.label_quest)
        self.text_quest = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.text_quest.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_quest.sizePolicy().hasHeightForWidth())
        self.text_quest.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_quest.setFont(font)
        self.text_quest.setToolTipDuration(-1)
        self.text_quest.setStyleSheet("border:none;\n"
"color:#006080;")
        self.text_quest.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.text_quest.setObjectName("text_quest")
        self.verticalLayout.addWidget(self.text_quest)
        self.label_answer = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_answer.setFont(font)
        self.label_answer.setStyleSheet("color:#006080;")
        self.label_answer.setObjectName("label_answer")
        self.verticalLayout.addWidget(self.label_answer)
        self.text_answer = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_answer.sizePolicy().hasHeightForWidth())
        self.text_answer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_answer.setFont(font)
        self.text_answer.setToolTipDuration(-1)
        self.text_answer.setStyleSheet("border:none;\n"
"color:#006080;\n"
"")
        self.text_answer.setObjectName("text_answer")
        self.verticalLayout.addWidget(self.text_answer)
        self.label_true_answer = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_true_answer.setFont(font)
        self.label_true_answer.setStyleSheet("color:#006080;")
        self.label_true_answer.setObjectName("label_true_answer")
        self.verticalLayout.addWidget(self.label_true_answer)
        self.text_true_answer = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_true_answer.sizePolicy().hasHeightForWidth())
        self.text_true_answer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_true_answer.setFont(font)
        self.text_true_answer.setToolTipDuration(-1)
        self.text_true_answer.setStyleSheet("border:none;\n"
"color:#006080;")
        self.text_true_answer.setObjectName("text_true_answer")
        self.verticalLayout.addWidget(self.text_true_answer)
        self.button_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_add.setFont(font)
        self.button_add.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.button_add.setStyleSheet("QPushButton{\n"
"    font: 12pt \"Gadugi\";\n"
"    color:#006080;\n"
"    background-color:#ccf2ff;\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    color:#ffd9b3;\n"
"    background-color:#006080;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:#ff9933;\n"
"    background-color:#006080;\n"
"}")
        self.button_add.setDefault(False)
        self.button_add.setFlat(False)
        self.button_add.setObjectName("button_add")
        self.verticalLayout.addWidget(self.button_add)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)

        self.retranslateUi(Win2)
        QtCore.QMetaObject.connectSlotsByName(Win2)

    def retranslateUi(self, Win2):
        _translate = QtCore.QCoreApplication.translate
        Win2.setWindowTitle(_translate("Win2", "Add_a_question"))
        self.label_quest.setText(_translate("Win2", "????????????:"))
        self.label_answer.setText(_translate("Win2", "????????????:"))
        self.label_true_answer.setText(_translate("Win2", "???????????????????? ??????????:"))
        self.button_add.setText(_translate("Win2", "????????????????"))



