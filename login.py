# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\dise├▒ofeliciaciones\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#import res_rc
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 539)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 30, 370, 480))
        self.frame.setStyleSheet("QPushButton#pushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 102, 206, 255), stop:0.55 rgba(235, 61, 61, 176), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgba(255,255,255,210);\n"
"padding: 10px;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(54, 68, 206, 255), stop:0.55 rgba(235, 61, 61, 176), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"backround-color: rgaba(105,118,132,200);\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_2,\n"
"QPushButton#pushButton_3,\n"
"QPushButton#pushButton_4,\n"
"QPushButton#pushButton_5 {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(117, 117, 117);\n"
"    border-radius: 15px; /* Agregado el border-radius para hacerlos circulares */\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover,\n"
"QPushButton#pushButton_3:hover,\n"
"QPushButton#pushButton_4:hover,\n"
"QPushButton#pushButton_5:hover {\n"
"    color: rgba(115, 168, 182, 220);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed,\n"
"QPushButton#pushButton_3:pressed,\n"
"QPushButton#pushButton_4:pressed,\n"
"QPushButton#pushButton_5:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    color: rgba(115, 129, 142, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setStyleSheet("border-image: url(:/image/imagen.jpg);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 311, 420))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 50));\n"
"border-radius:20px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 281, 390))
        self.label_3.setStyleSheet("background-color: rgba(0,0,0,100);\n"
"border-radius:20px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(135, 95, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255,255,255,210)")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(80, 165, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: transparent;\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105, 118, 132,255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: transparent;\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105, 118, 132,255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 102, 206, 255), stop:0.55 rgba(235, 61, 61, 176), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgba(255,255,255,210);\n"
"padding: 10px;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(54, 68, 206, 255), stop:0.55 rgba(235, 61, 61, 176), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"backround-color: rgaba(105,118,132,200);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 390, 30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(80, 360, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color: rgb(173, 173, 173);")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 390, 30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
"QPushButton#pushButton_2{\n"
"background-color: rgba(0,0,0,0);\n"
"color:rgb(117, 117, 117)\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"color: rgba(115,168,182,220);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"\n"
"color: rgba(115,129,142,,255);\n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 390, 30, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
"QPushButton#pushButton_2{\n"
"background-color: rgba(0,0,0,0);\n"
"color:rgb(117, 117, 117)\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"color: rgba(115,168,182,220);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"\n"
"color: rgba(115,129,142,,255);\n"
"\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 390, 30, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("\n"
"QPushButton#pushButton_2{\n"
"background-color: rgba(0,0,0,0);\n"
"color:rgb(117, 117, 117)\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"color: rgba(115,168,182,220);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"\n"
"color: rgba(115,129,142,,255);\n"
"\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "L o g I n"))
        self.pushButton_2.setText(_translate("Form", "+"))
        self.label_5.setText(_translate("Form", "Forgot your User Name or Password?"))
        self.pushButton_3.setText(_translate("Form", "M"))
        self.pushButton_4.setText(_translate("Form", "C"))
        self.pushButton_5.setText(_translate("Form", "E"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    From = QtWidgets.QWidget
    ui = Ui_Form()
    ui.setupUi(From)
    From.show()
    sys.exit(app.exec_())
    