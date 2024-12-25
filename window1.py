

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
class Ui_MainWindow(object):
        
        def __init__(self):
                try:
                        self.db = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="",
                                database="jajal"
                        )
                        self.cursor = self.db.cursor()
                        print("Login Berhasil")
                except mysql.connector.Error as e:
                        print("Gagal Login: ", e)

                
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(598, 477)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(140, 0, 301, 141))
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap("ai-generated-8973925_640-removebg-preview.png"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(170, 150, 251, 51))
                font = QtGui.QFont()
                font.setFamily("Neue Haas Grotesk Text Pro Medi")
                font.setPointSize(12)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(7)
                self.label_2.setFont(font)
                self.label_2.setAutoFillBackground(False)
                self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
        "color: rgb(93, 255, 57);\n"
        "font: 57 12pt \"Neue Haas Grotesk Text Pro Medi\";")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(190, 210, 221, 16))
                self.label_3.setStyleSheet("font: 75 10pt \"News706 BT\";\n"
        "text-decoration: underline;\n"
        "background-color: rgb(202, 208, 202);\n"
        "color: rgb(170, 85, 255);")
                self.label_3.setObjectName("label_3")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(290, 240, 75, 31))
                self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
        "background-color: rgb(58, 255, 91);")
                self.pushButton.setObjectName("pushButton")
                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_2.setGeometry(QtCore.QRect(480, 320, 75, 23))
                self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);\n"
        "color: rgb(0, 0, 0);")
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_4.setGeometry(QtCore.QRect(90, 320, 75, 23))
                self.pushButton_4.setStyleSheet("background-color: rgb(255, 176, 64);\n"
        "color: rgb(0, 0, 0);")
                self.pushButton_4.setObjectName("pushButton_4")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(250, 240, 41, 31))
                self.label_4.setText("")
                self.label_4.setPixmap(QtGui.QPixmap("input.png"))
                self.label_4.setScaledContents(False)
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(450, 320, 31, 31))
                self.label_5.setText("")
                self.label_5.setPixmap(QtGui.QPixmap("search.png"))
                self.label_5.setScaledContents(False)
                self.label_5.setObjectName("label_5")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(50, 320, 47, 31))
                self.label_7.setText("")
                self.label_7.setPixmap(QtGui.QPixmap("write.png"))
                self.label_7.setObjectName("label_7")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(280, 280, 111, 16))
                self.label_6.setStyleSheet("color: rgb(0, 0, 255);")
                self.label_6.setObjectName("label_6")
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(80, 350, 111, 16))
                self.label_8.setStyleSheet("color: rgb(0, 0, 255);")
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(self.centralwidget)
                self.label_9.setGeometry(QtCore.QRect(470, 350, 121, 16))
                self.label_9.setStyleSheet("color: rgb(0, 0, 255);")
                self.label_9.setObjectName("label_9")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 21))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                
                self.pushButton.clicked.connect(self.show_window_input)
                self.pushButton_2.clicked.connect(self.show_window_search)
                
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_2.setText(_translate("MainWindow", "Selamat Datang Ibu Bapak Guru"))
                self.label_3.setText(_translate("MainWindow", "pilih apa yang akan kamu lakukan"))
                self.pushButton.setText(_translate("MainWindow", "INPUT"))
                self.pushButton_2.setText(_translate("MainWindow", "SEARCH"))
                self.pushButton_4.setText(_translate("MainWindow", "EDIT"))
                self.label_6.setText(_translate("MainWindow", "Klik Untuk Input Data"))
                self.label_8.setText(_translate("MainWindow", "Klik Untuk Edit Data"))
                self.label_9.setText(_translate("MainWindow", "Klik Untuk Search Data"))
                
        def show_window_input(self):
                print("Button Edit clicked.")
                # Create an instance of UI_input and open the window
                self.window = QtWidgets.QMainWindow()
                self.ui_input = UI_input()
                self.ui_input.setupUi(self.window)
                self.window.show()
        def show_window_search(self):
                print("Button Edit clicked.")
                # Create an instance of UI_input and open the window
                self.window = QtWidgets.QMainWindow()
                self.ui_input = Ui_Search()
                self.ui_input.setupUi(self.window)
                self.window.show()
                        
        def closeEvent(self, event):
        # Close the cursor and database connection when the application is closed
                if self.db.is_connected():
                        self.cursor.close()
                        self.db.close()
                        print("Database connection closed.")
                        event.accept()  # Ensure the event is accepted and the window closes
                                
                        
                
class UI_input(object):
        def __init__(self):
        # Inisialisasi koneksi dan cursor
                self.connection = mysql.connector.connect(
                host="localhost",        # Alamat server MySQL
                user="root",             # Username MySQL
                password="",             # Password MySQL
                database="jajal"       # Nama database
                )
                self.cursor = self.connection.cursor()

                
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(824, 586)
                MainWindow.setDockNestingEnabled(False)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(30, 20, 751, 511))
                self.frame.setStyleSheet("")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(180, 90, 111, 20))
                self.label_2.setStyleSheet("background-color: rgb(143, 255, 239);\n"
        "font: 57 10pt \"Neue Haas Grotesk Text Pro Medi\";")
                self.label_2.setObjectName("label_2")
                self.lineEdit = QtWidgets.QLineEdit(self.frame)
                self.lineEdit.setGeometry(QtCore.QRect(320, 90, 321, 20))
                self.lineEdit.setText("")
                self.lineEdit.setObjectName("lineEdit")
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(180, 150, 111, 21))
                self.label_3.setStyleSheet("background-color: rgb(143, 255, 239);\n"
        "font: 57 10pt \"Neue Haas Grotesk Text Pro Medi\";")
                self.label_3.setObjectName("label_3")
                self.radioButton = QtWidgets.QRadioButton(self.frame)
                self.radioButton.setGeometry(QtCore.QRect(320, 150, 82, 17))
                self.radioButton.setStyleSheet("color: rgb(255, 255, 0);\n"
        "background-color: rgb(0, 0, 0);")
                self.radioButton.setObjectName("radioButton")
                self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
                self.radioButton_2.setGeometry(QtCore.QRect(320, 200, 82, 17))
                self.radioButton_2.setStyleSheet("color: rgb(255, 255, 0);\n"
        "background-color: rgb(0, 0, 0);")
                self.radioButton_2.setObjectName("radioButton_2")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(150, 350, 141, 20))
                self.label_4.setStyleSheet("\n"
        "color: rgb(0, 0, 0);\n"
        "font: 87 12pt \"Neue Haas Grotesk Text Pro Blac\";\n"
        "text-decoration: underline;")
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.frame)
                self.label_5.setGeometry(QtCore.QRect(150, 250, 181, 16))
                self.label_5.setStyleSheet("\n"
        "color: rgb(0, 0, 0);\n"
        "font: 87 12pt \"Neue Haas Grotesk Text Pro Blac\";\n"
        "text-decoration: underline;")
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.frame)
                self.label_6.setGeometry(QtCore.QRect(150, 400, 71, 16))
                self.label_6.setStyleSheet("\n"
        "color: rgb(0, 0, 0);\n"
        "font: 87 12pt \"Neue Haas Grotesk Text Pro Blac\";\n"
        "text-decoration: underline;")
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.frame)
                self.label_7.setGeometry(QtCore.QRect(150, 300, 161, 16))
                self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
        "font: 87 12pt \"Neue Haas Grotesk Text Pro Blac\";\n"
        "text-decoration: underline;")
                self.label_7.setObjectName("label_7")
                self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
                self.lineEdit_2.setGeometry(QtCore.QRect(360, 350, 113, 20))
                self.lineEdit_2.setText("")
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
                self.lineEdit_3.setGeometry(QtCore.QRect(360, 300, 113, 20))
                self.lineEdit_3.setText("")
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
                self.lineEdit_4.setGeometry(QtCore.QRect(360, 250, 113, 20))
                self.lineEdit_4.setText("")
                self.lineEdit_4.setObjectName("lineEdit_4")
                self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
                self.lineEdit_5.setGeometry(QtCore.QRect(360, 400, 113, 20))
                self.lineEdit_5.setText("")
                self.lineEdit_5.setObjectName("lineEdit_5")
                self.pushButton = QtWidgets.QPushButton(self.frame)
                self.pushButton.setGeometry(QtCore.QRect(650, 470, 75, 23))
                self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
        "font: 75 9pt \"MS Shell Dlg 2\";\n"
        "color: rgb(0, 0, 0);")
                self.pushButton.setObjectName("pushButton")
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setGeometry(QtCore.QRect(420, 190, 47, 31))
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap("graduating-student2.png"))
                self.label.setObjectName("label")
                self.label_8 = QtWidgets.QLabel(self.frame)
                self.label_8.setGeometry(QtCore.QRect(420, 130, 47, 41))
                self.label_8.setText("")
                self.label_8.setPixmap(QtGui.QPixmap("graduating-student1.png"))
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(self.frame)
                self.label_9.setGeometry(QtCore.QRect(610, 430, 131, 20))
                self.label_9.setStyleSheet("color: rgb(52, 34, 255);")
                self.label_9.setObjectName("label_9")
                self.label_10 = QtWidgets.QLabel(self.frame)
                self.label_10.setGeometry(QtCore.QRect(610, 460, 47, 41))
                self.label_10.setText("")
                self.label_10.setPixmap(QtGui.QPixmap("save.png"))
                self.label_10.setObjectName("label_10")
                self.label_11 = QtWidgets.QLabel(self.frame)
                self.label_11.setGeometry(QtCore.QRect(500, 150, 81, 16))
                self.label_11.setStyleSheet("background-color: rgb(143, 255, 239);\n"
        "font: 57 10pt \"Neue Haas Grotesk Text Pro Medi\";")
                self.label_11.setObjectName("label_11")
                self.comboBox = QtWidgets.QComboBox(self.frame)
                self.comboBox.setGeometry(QtCore.QRect(600, 150, 69, 22))
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.lineEdit.raise_()
                self.label_3.raise_()
                self.radioButton.raise_()
                self.radioButton_2.raise_()
                self.label_4.raise_()
                self.label_5.raise_()
                self.label_6.raise_()
                self.label_7.raise_()
                self.lineEdit_2.raise_()
                self.lineEdit_3.raise_()
                self.lineEdit_4.raise_()
                self.lineEdit_5.raise_()
                self.pushButton.raise_()
                self.label.raise_()
                self.label_8.raise_()
                self.label_9.raise_()
                self.label_10.raise_()
                self.label_2.raise_()
                self.label_11.raise_()
                self.comboBox.raise_()
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 21))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                
                
                self.pushButton.clicked.connect(self.save)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_2.setText(_translate("MainWindow", "   Nama Lengkap"))
                self.label_3.setText(_translate("MainWindow", "    Jenis Kelamin"))
                self.radioButton.setText(_translate("MainWindow", "Laki-laki"))
                self.radioButton_2.setText(_translate("MainWindow", "Perempuan"))
                self.label_4.setText(_translate("MainWindow", "Nilai Matematika"))
                self.label_5.setText(_translate("MainWindow", "Nilai Bahasa Indonesia"))
                self.label_6.setText(_translate("MainWindow", "Nilai IPA"))
                self.label_7.setText(_translate("MainWindow", "Nilai Bahasa Inggris"))
                self.pushButton.setText(_translate("MainWindow", "SAVE"))
                self.label_9.setText(_translate("MainWindow", "Klik Untuk Menyimpan Data"))
                self.label_11.setText(_translate("MainWindow", "Nama Kelas"))
                self.comboBox.setItemText(0, _translate("MainWindow", "2 A"))
                self.comboBox.setItemText(1, _translate("MainWindow", "2 B"))
        def save(self):
                # Ambil nilai dari input field
                nama_lengkap = self.lineEdit.text()
                jenis_kelamin = 'Laki-laki' if self.radioButton.isChecked() else 'Perempuan'
                kelas = self.comboBox.currentText()
                bahasa_indonesia = float(self.lineEdit_4.text())
                bahasa_inggris = float(self.lineEdit_3.text())
                matematika = float(self.lineEdit_2.text())
                ipa = float(self.lineEdit_5.text())

                # SQL query untuk menyimpan data ke tabel "siswa"
                query = """
                INSERT INTO siswa (nama_lengkap, jenis_kelamin, kelas, bahasa_indonesia, bahasa_inggris, matematika, ipa)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

                values = (nama_lengkap, jenis_kelamin, kelas, bahasa_indonesia, bahasa_inggris, matematika, ipa)

                try:
                # Eksekusi query dan commit transaksi
                        self.cursor.execute(query, values)
                        self.connection.commit()
                        print("Data berhasil disimpan!")
                except Exception as e:
                # Jika terjadi error, tampilkan pesan error
                        print(f"Terjadi error saat menyimpan data: {e}")


class Ui_Search(object):
        def __init__(self):
                # Inisialisasi koneksi dan cursor
                self.connection = mysql.connector.connect(
                host="localhost",        # Alamat server MySQL
                user="root",             # Username MySQL
                password="",             # Password MySQL
                database="jajal"         # Nama database
                )
                self.cursor = self.connection.cursor()

        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(586, 546)
                self.frame = QtWidgets.QFrame(Form)
                self.frame.setGeometry(QtCore.QRect(10, 10, 561, 521))
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(20, 30, 47, 41))
                self.label_4.setText("")
                self.label_4.setPixmap(QtGui.QPixmap("id-card1.png"))
                self.label_4.setObjectName("label_4")
                self.lineEdit = QtWidgets.QLineEdit(self.frame)
                self.lineEdit.setGeometry(QtCore.QRect(170, 40, 211, 20))
                self.lineEdit.setObjectName("lineEdit")
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setGeometry(QtCore.QRect(70, 40, 91, 16))
                self.label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
                self.label.setObjectName("label")
                self.label_5 = QtWidgets.QLabel(self.frame)
                self.label_5.setGeometry(QtCore.QRect(20, 90, 47, 41))
                self.label_5.setText("")
                self.label_5.setPixmap(QtGui.QPixmap("learning-support.png"))
                self.label_5.setObjectName("label_5")
                self.comboBox = QtWidgets.QComboBox(self.frame)
                self.comboBox.setGeometry(QtCore.QRect(170, 110, 69, 22))
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(70, 110, 47, 16))
                self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
                self.label_2.setObjectName("label_2")
                self.label_6 = QtWidgets.QLabel(self.frame)
                self.label_6.setGeometry(QtCore.QRect(350, 230, 111, 20))
                self.label_6.setStyleSheet("color: rgb(106, 80, 255);")
                self.label_6.setObjectName("label_6")
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(480, 180, 51, 41))
                self.label_3.setText("")
                self.label_3.setPixmap(QtGui.QPixmap("people.png"))
                self.label_3.setScaledContents(True)
                self.label_3.setObjectName("label_3")
                self.pushButton = QtWidgets.QPushButton(self.frame)
                self.pushButton.setGeometry(QtCore.QRect(470, 230, 75, 23))
                self.pushButton.setStyleSheet("background-color: rgb(176, 181, 185);\n"
                                        "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                        "text-decoration: underline;")
                self.pushButton.setObjectName("pushButton")
                self.label_7 = QtWidgets.QLabel(self.frame)
                self.label_7.setGeometry(QtCore.QRect(210, 390, 71, 21))
                self.label_7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
                self.label_7.setObjectName("label_7")
                self.comboBox_2 = QtWidgets.QComboBox(self.frame)
                self.comboBox_2.setGeometry(QtCore.QRect(300, 390, 69, 22))
                self.comboBox_2.setObjectName("comboBox_2")
                self.comboBox_2.addItem("")
                self.comboBox_2.addItem("")
                self.label_8 = QtWidgets.QLabel(self.frame)
                self.label_8.setGeometry(QtCore.QRect(80, 340, 411, 16))
                self.label_8.setStyleSheet("font: 87 10pt \"Neue Haas Grotesk Text Pro Blac\";\n"
                                        "color: rgb(0, 0, 255);")
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(self.frame)
                self.label_9.setGeometry(QtCore.QRect(160, 370, 47, 61))
                self.label_9.setText("")
                self.label_9.setPixmap(QtGui.QPixmap("live-streaming.png"))
                self.label_9.setObjectName("label_9")
                self.pushButton_2 = QtWidgets.QPushButton(self.frame)
                self.pushButton_2.setGeometry(QtCore.QRect(470, 470, 75, 23))
                self.pushButton_2.setStyleSheet("background-color: rgb(176, 181, 185);\n"
                                                "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                                "text-decoration: underline;")
                self.pushButton_2.setObjectName("pushButton_2")
                self.label_10 = QtWidgets.QLabel(self.frame)
                self.label_10.setGeometry(QtCore.QRect(350, 470, 121, 20))
                self.label_10.setStyleSheet("color: rgb(106, 80, 255);")
                self.label_10.setObjectName("label_10")
                self.label_11 = QtWidgets.QLabel(self.frame)
                self.label_11.setGeometry(QtCore.QRect(480, 420, 51, 41))
                self.label_11.setText("")
                self.label_11.setPixmap(QtGui.QPixmap("people.png"))
                self.label_11.setObjectName("label_11")
                self.label_12 = QtWidgets.QLabel(self.frame)
                self.label_12.setGeometry(QtCore.QRect(480, 420, 51, 41))
                self.label_12.setText("")
                self.label_12.setPixmap(QtGui.QPixmap("people.png"))
                self.label_12.setScaledContents(True)
                self.label_12.setObjectName("label_12")
                
                self.pushButton.clicked.connect(self.search1)
                self.pushButton_2.clicked.connect(self.search2)

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.label.setText(_translate("Form", "Nama Lengkap"))
                self.comboBox.setItemText(0, _translate("Form", "2 A"))
                self.comboBox.setItemText(1, _translate("Form", "2 B"))
                self.label_2.setText(_translate("Form", "Kelas"))
                self.label_6.setText(_translate("Form", "Klik Untuk Mencari Data"))
                self.pushButton.setText(_translate("Form", "SEARCH1"))
                self.label_7.setText(_translate("Form", "Nama Kelas"))
                self.comboBox_2.setItemText(0, _translate("Form", "2 A"))
                self.comboBox_2.setItemText(1, _translate("Form", "2 B"))
                self.label_8.setText(_translate("Form", "PILIH KELAS UNTUK MENCARI DATA KESELURUHAN"))
                self.pushButton_2.setText(_translate("Form", "SEARCH2"))
                self.label_10.setText(_translate("Form", "Klik Untuk Mencari Data"))
        
        def search1(self):
                # Get user input
                nama = self.lineEdit.text()
                kelas = self.comboBox.currentText()

                # Create query for fetching one record based on the input
                query = f"SELECT * FROM siswa WHERE nama_lengkap LIKE '%{nama}%' AND kelas = '{kelas}' LIMIT 1"
                
                # Execute query
                self.cursor.execute(query)
                result = self.cursor.fetchone()

                # Display result in a message box
                if result:
                        # Assuming result[1] is 'nama_lengkap', result[2] is 'kelas', and result[3] is 'alamat',
                        # and result[4] is 'no_hp', while result[5], result[6], result[7], and result[8] are the values
                        message = f"Data Ditemukan:\nNama: {result[1]}\nKelas: {result[2]}\nAlamat: {result[3]}\nNo. HP: {result[4]}\n"
                        message += f"Bahasa Indonesia: {result[5]}\nBahasa Inggris: {result[6]}\nMatematika: {result[7]}\nIPA: {result[8]}"
                        QtWidgets.QMessageBox.information(None, "Hasil Pencarian", message)
                else:
                        QtWidgets.QMessageBox.warning(None, "Data Tidak Ditemukan", "Data tidak ditemukan!")




        def search2(self):
                # Get user input
                kelas = self.comboBox_2.currentText()

                # Create query for fetching all records based on the input
                query = f"SELECT * FROM siswa WHERE kelas = '{kelas}'" 

                # Execute query
                self.cursor.execute(query)
                results = self.cursor.fetchall()

                # Display results
                if results:
                        message = "Data Ditemukan:\n"
                        for result in results:
                        # Assuming result[1] is 'nama_lengkap', result[2] is 'kelas', and result[3] is 'alamat',
                        # and result[4] is 'no_hp', while result[5], result[6], result[7], and result[8] are the values
                                message += f"Nama: {result[1]}\nKelas: {result[2]}\nAlamat: {result[3]}\nNo. HP: {result[4]}\n"
                                message += f"Bahasa Indonesia: {result[5]}\nBahasa Inggris: {result[6]}\nMatematika: {result[7]}\nIPA: {result[8]}\n\n"
                        QtWidgets.QMessageBox.information(None, "Hasil Pencarian", message)
                else:
                        QtWidgets.QMessageBox.warning(None, "Data Tidak Ditemukan", "Data tidak ditemukan!")






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())