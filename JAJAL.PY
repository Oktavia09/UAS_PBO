# -- coding: utf-8 --

# Form implementation generated from reading ui file 'pdonasi.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 420)
        MainWindow.setMinimumSize(QtCore.QSize(320, 420))
        MainWindow.setMaximumSize(QtCore.QSize(320, 420))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 321, 471))
        self.widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(243, 250, 255);\n"
"}")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 321, 61))
        self.widget_2.setStyleSheet("QWidget {\n"
"    background-color: #ADD8E6;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(70, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(180, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 110, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 170, 151, 20))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 110, 151, 20))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(150, 200, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 230, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 260, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(60, 330, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #ADD8E6;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 330, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #ADD8E6;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(20, 80, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 80, 151, 20))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(20, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(150, 140, 62, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(230, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 18))
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
        self.label_6.setText(_translate("MainWindow", "PENGELOLAAN"))
        self.label_7.setText(_translate("MainWindow", "DONASI"))
        self.label.setText(_translate("MainWindow", "Nama Donatur:"))
        self.label_2.setText(_translate("MainWindow", "Jumlah Donasi:"))
        self.label_3.setText(_translate("MainWindow", "Kategori Donasi:"))
        self.label_4.setText(_translate("MainWindow", "Metode Pembayaran:"))
        self.label_5.setText(_translate("MainWindow", "Pilih Transaksi:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Uang"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Barang"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Tunai"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Non Tunai"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "BRI"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "BNI"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "BCA"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Mandiri"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "ShoopePay"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Dana"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Qris"))
        self.pushButton.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_2.setText(_translate("MainWindow", "Konfirmasi"))
        self.label_8.setText(_translate("MainWindow", "ID Donatur:"))
        self.label_9.setText(_translate("MainWindow", "Jenis Kelamin:"))
        self.radioButton.setText(_translate("MainWindow", "Laki-Laki"))
        self.radioButton_2.setText(_translate("MainWindow", "Perempuan"))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())