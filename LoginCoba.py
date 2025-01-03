# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 881, 671))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background-color:#CC95C0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(80, 20, 631, 121))
        self.frame_5.setStyleSheet("background-color:#DBD4B4;\n"
"border-radius:20px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(230, 20, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(160, 70, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 141, 121))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../Downloads/bg-transparent-bank.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(32, 170, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(331, 190, 241, 40))
        self.lineEdit_3.setStyleSheet("background-color:#DBD4B4;\n"
"border-radius:5px;\n"
"font-size:20px;")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 240, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(331, 240, 241, 40))
        self.lineEdit_4.setStyleSheet("background-color:#DBD4B4;\n"
"border-radius:5px;\n"
"font-size:20px;")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(32, 290, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(-10, 330, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 340, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_2.setStyleSheet("background-color:#DBD4B4;\n"
"\n"
"font-size:20px;")
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setCurrentText("Lainnya")
        self.comboBox_2.setDuplicatesEnabled(False)
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(330, 295, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_3.setStyleSheet("background-color:#DBD4B4;\n"
"\n"
"font-size:20px;")
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setCurrentText("Lainnya")
        self.comboBox_3.setDuplicatesEnabled(False)
        self.comboBox_3.setFrame(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Selamat Datang"))
        self.label_4.setText(_translate("MainWindow", "Rumah Kita Peduli Bersama"))
        self.label.setText(_translate("MainWindow", "Nama"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "masukkan username"))
        self.label_2.setText(_translate("MainWindow", "Nominal"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "masukkan username"))
        self.label_6.setText(_translate("MainWindow", "Kategori"))
        self.label_7.setText(_translate("MainWindow", "pembayaran"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Lainnya"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "BRI"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "BCA"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Mandiri"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Bank Jatim"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "BNI"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Lainnya"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Tunau"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Non Tunai"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
