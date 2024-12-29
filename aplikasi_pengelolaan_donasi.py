from PyQt5 import QtWidgets, QtCore, QtGui
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget

import sys
from datetime import datetime

class Ui_MainWindow(object):
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.create_connection()

    # mengoneksi ke database
    def create_connection(self):
        """Create a database connection to a MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',  # Replace with your MySQL username
                password='',  # Replace with your MySQL password
                database='aplikasi_pengelolaan_donasi'  # Database name
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Connection to database successful")
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")

    def setupUi(self, MainWindow):
        self.current_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create Frame for UI
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 881, 671))
        self.frame.setStyleSheet("background-color:#CC95C0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(80, 20, 631, 121))
        self.frame_5.setStyleSheet("background-color:#DBD4B4;\nborder-radius:20px;")
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
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 243, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 350, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 280, 461, 40))
        self.lineEdit_3.setStyleSheet("background-color:#DBD4B4;\nborder-radius:5px;\nfont-size:20px;")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 380, 461, 41))
        self.lineEdit_2.setStyleSheet("background-color:#DBD4B4;\nborder-radius:5px;\nfont-size:20px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(301, 532, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#DBD4B4;\nborder-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        
        
        # event tombol login
        self.pushButton.clicked.connect(self.handle_login )  # Update to connect to handle_login method 
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Selamat Datang"))
        self.label_4.setText(_translate("MainWindow", "Rumah Kita Peduli Bersama"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Masukkan password"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Masukkan username"))
    
    # fungsi handle login (menangani proses login)
    # di dalam fungsi handle login terdapat 2 role, yaitu admin dan superadmin
    def handle_login(self):
        """Handle the login process."""
        username = self.lineEdit_3.text()
        password = self.lineEdit_2.text()

        role = self.check_login(username, password)  # Periksa login dan dapatkan role
        if role:
            if role == "SuperAdmin": #selain superadmin tidak bisa login
                self.show_superadmin_window()
                QtWidgets.QMessageBox.information(None, "Login Success", "Login berhasil sebagai Super Admin!")
            else:
                self.show_new_window()
                QtWidgets.QMessageBox.information(None, "Login Success", "Login berhasil!")
            
            self.current_window.close()
        else:
            QtWidgets.QMessageBox.warning(None, "Login Failed", "Username atau password salah.")


    # fungsi untuk masuk ke form donatur / admin              
    def show_new_window(self):
        """Show the UI for form donatur."""
        self.new_window = QtWidgets.QMainWindow()
        self.ui = UI_form_donatur(self.connection)  # Pass the database connection
        self.ui.setupUi(self.new_window)
        self.new_window.show()

    #menyambungkan ke database
    def check_login(self, username, password):
        """Check login credentials and fetch user role."""
        query = "SELECT password, role FROM users WHERE username = %s OR email = %s"
        self.cursor.execute(query, (username, username))
        result = self.cursor.fetchone()
        
        if result and result[0] == password:  # Compare plaintext passwords
            return result[1]  # Return role of the user
        return None

    # fungsi untuk masuk ke form dasboard / superadmin  
    def show_superadmin_window(self):
        """Show the UI for SuperAdmin."""
        self.new_window = QtWidgets.QMainWindow()
        self.ui = UI_SuperAdmin()  # Create instance of SuperAdmin UI
        self.ui.setupUi(self.new_window)
        self.new_window.show()




    
# masuk form donatur    
class UI_form_donatur(QWidget):  # Turunan dari QWidget
    def __init__(self, db_connection, login_window=None, parent=None):
        super().__init__(parent)  # Panggil konstruktor QWidget
        self.setupUi(Mainwindow)  # Inisialisasi UI
        self.db_connection = db_connection
        self.login_window = login_window
        self.cursor = db_connection.cursor()
        self.current_donor_data = None
        

    def setupUi(self, MainWindow):
        self.current_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        MainWindow.setMaximumSize(QtCore.QSize(800, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 908, 671))
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
        self.label.setGeometry(QtCore.QRect(94, 222, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(371, 245, 241, 40))
        self.lineEdit_3.setStyleSheet("background-color:#DBD4B4;\n"
"border-radius:5px;\n"
"font-size:20px;")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(75, 287, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(369, 298, 241, 40))
        self.lineEdit_4.setStyleSheet("background-color:#DBD4B4;\n"
"border-radius:5px;\n"
"font-size:20px;")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(95, 343, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(370, 359, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("backgroun-color::#DBD4B4;")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(475, 350, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        
        # button 
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(60, 500, 120, 50))
        self.pushButton.setStyleSheet("background-color:#DBD4B4;\n"
                                            "border-radius:10px;\n"
                                            "font-size:14px;\n"
                                            "margin:7px;")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 500, 120, 50))
        self.pushButton_2.setStyleSheet("background-color:#DBD4B4;\n"
                                            "border-radius:7px;\n"
                                            "font-size:14px;\n"
                                            "margin:7px;")
        self.pushButton_2.setObjectName("pushButton_2")
        
        
        # button masuk
        self.pushButton_masuk = QtWidgets.QPushButton(self.frame)
        self.pushButton_masuk.setGeometry(QtCore.QRect(370, 500, 120, 50))
        self.pushButton_masuk.setStyleSheet("background-color:#DBD4B4;\n"
                                            "border-radius:7px;\n"
                                            "font-size:14px;\n"
                                            "margin:7px;")
        self.pushButton_masuk.setObjectName("pushButton_masuk")
        
        
        # button refresh
        self.refreshButton = QtWidgets.QPushButton("Refresh", self.frame)
        self.refreshButton.setGeometry(QtCore.QRect(520, 500, 120, 50))
        self.refreshButton.setStyleSheet("background-color:#DBD4B4;\n"
                                            "border-radius:7px;\n"
                                            "font-size:14px;\n"
                                            "margin:7px;")
        self.refreshButton.setObjectName("refreshButton")
        
        # button keluar
        
        self.pushButtonLogout = QtWidgets.QPushButton(self.frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(670, 500, 120, 50))
        self.pushButtonLogout.setStyleSheet("background-color:#DBD4B4;\n"
                                            "border-radius:7px;\n"
                                            "font-size:14px;\n"
                                            "margin:7px;")
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar) 
        self.pushButton.clicked.connect(self.save_data)
        # self.pushButton_2.clicked.connect(self.show_window_update)
        # self.pushButton_2.clicked.connect(self.load_data)
        
        
        
        # event click 
        self.pushButton_masuk.clicked.connect(self.on_masuk_clicked) #tombol masuk 
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        self.refreshButton.clicked.connect(self.refresh_data) #tombol refresh
        self.pushButtonLogout.clicked.connect(self.on_pushButton_3_clicked) 

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def load_data(self):
        """
        Load existing donor data from the database
        """
        try:
            # Get data from input fields
            nama = self.lineEdit_3.text().strip()
            email = self.lineEdit_4.text().strip()

            # Validate input
            if not nama or not email:
                QMessageBox.warning(None, "Peringatan", "Nama dan Email harus diisi untuk mencari data!")
                return False

            # Execute query to find donor
            sql = "SELECT * FROM donatur WHERE LOWER(nama_donatur) = LOWER(%s) AND LOWER(email_donatur) = LOWER(%s)"
            self.cursor.execute(sql, (nama, email))
            result = self.cursor.fetchone()

            # Check if data is found
            if result:
                # Store the current donor data for update process
                self.current_donor_data = {
                    'id': result[0],  # Assuming first column is ID
                    'nama': result[1],
                    'email': result[2],
                    'kategori': result[3]
                }

                # Populate form with existing data
                self.lineEdit_3.setText(result[1])  # Nama
                self.lineEdit_4.setText(result[2])  # Email
                
                # Set radio button based on category
                if result[3] == "Individu":
                    self.radioButton.setChecked(True)
                elif result[3] == "Organisasi":
                    self.radioButton_2.setChecked(True)
                
                QMessageBox.information(None, "Data Ditemukan", "Data berhasil dimuat!")
                return True
            else:
                QMessageBox.warning(None, "Peringatan", "Data tidak ditemukan di database!")
                return False

        except mysql.connector.Error as e:
            QMessageBox.critical(None, "Kesalahan Database", f"Terjadi kesalahan: {e}")
            return False
  
    def on_pushButton_2_clicked(self): #tombol update
        """
        Handle the update process when Update1 button is clicked
        """
        if self.load_data():
            # Show update window with existing data
            self.show_window_update()       # Memperbarui data
    
    def on_pushButton_3_clicked(self):
        # Kembali ke UI_MainWindow
        self.current_window.close()
        self.redirect_to_main_window()
        
            
    def redirect_to_main_window(self):
        # Membuka UI_MainWindow
        self.main_window = QtWidgets.QMainWindow()
        self.ui_main = Ui_MainWindow()  # Pastikan Ui_MainWindow didefinisikan
        self.ui_main.setupUi(self.main_window)
        self.main_window.show()

    def update_data(self):
        nama_baru = self.lineEdit_3.text()
        email_baru = self.lineEdit_4.text()
        kategori_baru = "Individu" if self.radioButton.isChecked() else "Organisasi" if self.radioButton_2.isChecked() else None

        if not nama_baru or not email_baru or not kategori_baru:
            QMessageBox.warning(None, "Peringatan", "Semua kolom harus diisi untuk memperbarui data!")
            return
        try:
            # Update hanya jika data ditemukan, berdasarkan nama dan email
            sql = "UPDATE donatur SET nama = %s, email = %s, kategori = %s WHERE nama = %s AND email = %s"
            self.cursor.execute(sql, (nama_baru, email_baru, kategori_baru, nama_baru, email_baru))
            self.db_connection.commit()
            QMessageBox.information(None, "Berhasil", "Data berhasil diperbarui!")
        except mysql.connector.Error as e:
            QMessageBox.critical(None, "Gagal", f"Terjadi kesalahan: {e}")
    
    def show_update_form(self):
        """Menampilkan form untuk memperbarui data setelah data ditemukan"""
        self.lineEdit_3.setEnabled(True)  # Mengaktifkan input nama
        self.lineEdit_4.setEnabled(True)  # Mengaktifkan input email
        self.radioButton.setEnabled(True)  # Mengaktifkan radio button individu
        self.radioButton_2.setEnabled(True)  # Mengaktifkan radio button organisasi
        self.pushButton_2.setEnabled(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Selamat Datang"))
        self.label_4.setText(_translate("MainWindow", "Rumah Kita Peduli Bersama"))
        self.label.setText(_translate("MainWindow", "Nama"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "masukkan nama"))
        self.label_2.setText(_translate("MainWindow", "email"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "masukkan email"))
        self.label_6.setText(_translate("MainWindow", "Kategori"))
        self.radioButton.setText(_translate("MainWindow", "Individu"))
        self.radioButton_2.setText(_translate("MainWindow", "Organisasi"))
        self.pushButton.setText(_translate("MainWindow", "Tambah"))
        self.pushButton_2.setText(_translate("MainWindow", "Update1"))
        self.pushButton_masuk.setText(_translate("MainWindow", "Masuk"))
        self.pushButtonLogout.setText(_translate("MainWindow", "logout"))

        
    def save_data(self):
        nama = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        kategori = "Individu" if self.radioButton.isChecked() else "Organisasi" if self.radioButton_2.isChecked() else None

        if not nama or not email or not kategori:
            QMessageBox.warning(None, "Peringatan", "Semua kolom harus diisi!")
            return

        try:
            # Check if the data already exists
            check_sql = "SELECT * FROM donatur WHERE nama_donatur = %s AND email_donatur = %s AND kategori_donatur = %s"
            self.cursor.execute(check_sql, (nama, email, kategori))
            result = self.cursor.fetchone()

            if result:
                QMessageBox.information(None, "Info", "Data telah ada, tidak ada duplikasi.")
            else:
                # Insert new data if not exists
                sql = "INSERT INTO donatur (nama_donatur, email_donatur, kategori_donatur) VALUES (%s, %s, %s)"
                self.cursor.execute(sql, (nama, email , kategori))
                self.db_connection.commit()
                QMessageBox.information(None, "Berhasil", "Data berhasil disimpan!")

        except mysql.connector.Error as e:
            QMessageBox.critical(None, "Gagal", f"Terjadi kesalahan: {e}")

    def on_masuk_clicked(self):
        """
        Validate donor credentials and open the UI_Transaksi window.
        
        This method:
        1. Checks if nama (name) and email are provided
        2. Queries the database to find matching donor
        3. Opens UI_Transaksi window with donor data if found
        4. Displays appropriate error messages if validation fails
        """
        # Get input values
        nama = self.lineEdit_3.text().strip()
        email = self.lineEdit_4.text().strip()
        
        # Validate input fields
        if not nama or not email:
            QMessageBox.warning(
                None, 
                "Peringatan", 
                "Nama dan Email harus diisi!"
            )
            return
        
        try:
            # Prepare SQL query with case-insensitive matching
            sql = """
            SELECT * FROM donatur 
            WHERE LOWER(nama_donatur) = LOWER(%s) AND LOWER(email_donatur) = LOWER(%s)
            """
            
            # Execute query
            self.cursor.execute(sql, (nama, email))
            result = self.cursor.fetchone()
            
            # Check if donor exists
            if result:
                # Store the current donor data 
                # Adjust index based on your actual database schema
                self.current_donor_data = {
                    'id': result[0],          # Donor ID
                    'nama': result[1],        # Donor Name
                    'email': result[2],       # Donor Email
                    'kategori': result[3]     # Donor Category
                }
                
                # Open UI_Transaksi window
                self.new_window = QtWidgets.QMainWindow()
                self.ui = Ui_Transaksi(
                    db_connection=self.db_connection
                    
                )
                self.ui.setupUi(self.new_window)
                self.new_window.show()
            
            else:
                # No matching donor found
                QMessageBox.warning(
                    None, 
                    "Peringatan", 
                    "Data tidak ditemukan di database!"
                )
        
        except mysql.connector.Error as e:
            # Handle database connection or query errors
            QMessageBox.critical(
                None, 
                "Kesalahan Database", 
                f"Terjadi kesalahan: {e}"
            )

    
    def redirect_to_transaksi(self):
        """Redirect ke UI_Transaksi setelah berhasil menyimpan data."""
        self.new_window = QtWidgets.QMainWindow()
        self.ui = Ui_Transaksi(self.db_connection )  # Pastikan database connection diteruskan
        self.ui.setupUi(self.new_window)
        self.new_window.show()


    def show_window_update(self):
        """
        Open the UI_Edit window for updating donor information
        """
        self.new_window = QtWidgets.QMainWindow()
        self.ui = UI_Edit(self.db_connection, self.current_donor_data)
        self.ui.setupUi(self.new_window)
        self.new_window.show()
    

    def refresh_data(self):
        """
        Mengembalikan form ke kondisi awal (reset form)
        """
        self.lineEdit_3.clear()  # Bersihkan input nama
        self.lineEdit_4.clear()  # Bersihkan input email
        self.radioButton.setAutoExclusive(False)  # Matikan eksklusivitas sementara untuk reset radio button
        self.radioButton.setChecked(False)  # Reset radio button individu
        self.radioButton_2.setChecked(False)  # Reset radio button organisasi
        self.radioButton.setAutoExclusive(True)  # Aktifkan kembali eksklusivitas
        self.current_donor_data = None  # Reset data donatur yang sedang diakses
        QMessageBox.information(None, "Refresh", "Form berhasil di-refresh!")


class UI_Edit(object):

    def __init__(self, db_connection , current_donor_data=None):
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()
        self.current_donor_data = current_donor_data
         # Email awal untuk identifikasi

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.frame.setStyleSheet("background-color:#CC95C0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setObjectName("frame")

        self.label_nama = QtWidgets.QLabel(self.frame)
        self.label_nama.setGeometry(QtCore.QRect(50, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_nama.setFont(font)
        self.label_nama.setText("Nama")
        self.label_nama.setObjectName("label_nama")

        self.lineEdit_nama = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_nama.setGeometry(QtCore.QRect(200, 50, 300, 31))
        self.lineEdit_nama.setStyleSheet("background-color:#DBD4B4; font-size:16px; border-radius:5px;")
        self.lineEdit_nama.setObjectName("lineEdit_nama")

        self.label_email = QtWidgets.QLabel(self.frame)
        self.label_email.setGeometry(QtCore.QRect(50, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_email.setFont(font)
        self.label_email.setText("Email")
        self.label_email.setObjectName("label_email")

        self.lineEdit_email = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_email.setGeometry(QtCore.QRect(200, 100, 300, 31))
        self.lineEdit_email.setStyleSheet("background-color:#DBD4B4; font-size:16px; border-radius:5px;")
        self.lineEdit_email.setObjectName("lineEdit_email")

        self.label_kategori = QtWidgets.QLabel(self.frame)
        self.label_kategori.setGeometry(QtCore.QRect(50, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_kategori.setFont(font)
        self.label_kategori.setText("Kategori")
        self.label_kategori.setObjectName("label_kategori")

        self.radioButton_individu = QtWidgets.QRadioButton(self.frame)
        self.radioButton_individu.setGeometry(QtCore.QRect(200, 150, 121, 31))
        self.radioButton_individu.setText("Individu")
        self.radioButton_individu.setObjectName("radioButton_individu")

        self.radioButton_organisasi = QtWidgets.QRadioButton(self.frame)
        self.radioButton_organisasi.setGeometry(QtCore.QRect(350, 150, 121, 31))
        self.radioButton_organisasi.setText("Organisasi")
        self.radioButton_organisasi.setObjectName("radioButton_organisasi")

        self.pushButton_update = QtWidgets.QPushButton(self.frame)
        self.pushButton_update.setGeometry(QtCore.QRect(200, 250, 150, 40))
        self.pushButton_update.setText("Update2")
        self.pushButton_update.setStyleSheet("background-color:#DBD4B4; font-size:16px; border-radius:10px;")
        self.pushButton_update.setObjectName("pushButton_update")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Load data to form fields
        
        
        if self.current_donor_data:
            self.populate_form()
        
        self.pushButton_update.clicked.connect(self.update_data)  # Panggil load_data saat tombol update ditekan

        # Connect update button
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edit Donatur"))

      # Menutup aplikasi jika terjadi error
    
  # Menutup aplikasi jika terjadi error
    

    def populate_form(self):
        """
        Populate form fields with existing donor data
        """
        if self.current_donor_data:
            self.lineEdit_nama.setText(self.current_donor_data['nama'])
            self.lineEdit_email.setText(self.current_donor_data['email'])
            
            if self.current_donor_data['kategori'] == 'Individu':
                self.radioButton_individu.setChecked(True)
            else:
                self.radioButton_organisasi.setChecked(True)


  # Menutup aplikasi jika terjadi error
    def load_old_data(self):
        """
        Method to load the existing data of the donor before update
        """
        try:
            # Assuming we want to load data based on some identifier (in this case, a hardcoded name)
            sql = "SELECT nama_donatur , email_donatur, kategori_donatur FROM donatur WHERE nama_donatur = %s"
            self.cursor.execute(sql, ('khn',))  # Replace 'khn' with a dynamic way to identify the donor
            result = self.cursor.fetchone()
            
            if result:
                # Unpack the retrieved data
                nama_lama, email_lama, kategori_lama = result
                
                # Populate the form with existing data
                self.lineEdit_nama.setText(nama_lama)
                self.lineEdit_email.setText(email_lama)
                
                # Set the correct radio button based on kategori
                if kategori_lama == 'Individu':
                    self.radioButton_individu.setChecked(True)
                else:
                    self.radioButton_organisasi.setChecked(True)
                
                return nama_lama, email_lama, kategori_lama
            else:
                QMessageBox.warning(None, "Peringatan", "Data tidak ditemukan!")
                return None
        
        except mysql.connector.Error as e:
            QMessageBox.critical(None, "Kesalahan", f"Gagal mengambil data: {e}")
            return None

    def update_data(self):
        """
        Update donor data in the database
        """
        # Validate input
        nama_baru = self.lineEdit_nama.text().strip()
        email_baru = self.lineEdit_email.text().strip()
        kategori_baru = "Individu" if self.radioButton_individu.isChecked() else "Organisasi"

        # Validate inputs
        if not nama_baru or not email_baru:
            QMessageBox.warning(None, "Peringatan", "Semua kolom harus diisi!")
            return

        # Ensure we have the original donor data
        if not self.current_donor_data:
            QMessageBox.warning(None, "Kesalahan", "Data donor asli tidak ditemukan!")
            return

        try:
            # Prepare update query
            sql = """
            UPDATE donatur 
            SET nama_donatur = %s, email_donatur = %s, kategori_donatur = %s 
            WHERE id_donatur = %s
            """
            self.cursor.execute(sql, (
                nama_baru, 
                email_baru, 
                kategori_baru, 
                self.current_donor_data['id']
            ))
            
            # Commit the transaction
            self.db_connection.commit()
            
            # Check if update was successful
            if self.cursor.rowcount > 0:
                QMessageBox.information(None, "Berhasil", "Data berhasil diperbarui!")
                # Optionally, close the update window or redirect
                self.centralwidget.window().close()
            else:
                QMessageBox.warning(None, "Peringatan", "Tidak ada data yang diperbarui!")
        
        except mysql.connector.Error as e:
            # Rollback in case of error
            self.db_connection.rollback()
            QMessageBox.critical(None, "Kesalahan", f"Gagal memperbarui data: {e}")



    def show_update_form(self):
        """Menampilkan form untuk memperbarui data setelah data ditemukan"""
        self.lineEdit_nama.setEnabled(True)  # Mengaktifkan input nama
        self.lineEdit_email.setEnabled(True)  # Mengaktifkan input email
        self.radioButton_individu.setEnabled(True)  # Mengaktifkan radio button individu
        self.radioButton_organisasi.setEnabled(True)  # Mengaktifkan radio button organisasi
        self.pushButton_update.setEnabled(True)

    def redirect_to_ui_form_donatur(self):
        """
        Fungsi untuk kembali ke form `ui_form_donatur`.
        """
          # Import form donatur jika diperlukan
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_form_donatur(self.db_connection)  # Pastikan form menerima parameter yang sesuai
        self.ui.setupUi(self.window)
        self.window.show()
        self.current_window.close()
    
    
    
        
# form transaksi            
class Ui_Transaksi(object):
    def __init__(self, db_connection, login_window=None):
        self.db_connection = db_connection
        self.login_window = login_window
        self.cursor = db_connection.cursor()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        MainWindow.setMaximumSize(QtCore.QSize(800, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 700))
        self.frame.setStyleSheet("background-color:#CC95C0;")
        self.frame.setObjectName("frame")

        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(81, 20, 631, 121))
        self.frame_5.setStyleSheet("background-color:#DBD4B4;\n"
                                   "border-radius:20px;")
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
        self.label_5.setPixmap(QtGui.QPixmap("path/to/your/image.png"))  # Ganti dengan path yang benar
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 236, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.lineEdit_donatur = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_donatur.setGeometry(QtCore.QRect(371, 245, 241, 40))
        self.lineEdit_donatur.setStyleSheet("background-color:#DBD4B4;\n"
                                           "border-radius:5px;\n"
                                           "font-size:20px;")
        self.lineEdit_donatur.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_donatur.setObjectName("lineEdit_donatur")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 290, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.lineEdit_nominal = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_nominal.setGeometry(QtCore.QRect(370, 298, 241, 40))
        self.lineEdit_nominal.setStyleSheet("background-color:#DBD4B4;\n"
                                           "border-radius:5px;\n"
                                           "font-size:20px;")
        self.lineEdit_nominal.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_nominal.setObjectName("lineEdit_nominal")

        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(100, 350, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.comboBox_payment = QtWidgets.QComboBox(self.frame)
        self.comboBox_payment.setGeometry(QtCore.QRect(370, 350, 241, 41))
        self.comboBox_payment.setStyleSheet("background-color:#DBD4B4;\n"
                                           "border-radius:5px;\n"
                                           "font-size:20px;")
        self.comboBox_payment.setObjectName("comboBox_payment")
        self.comboBox_payment.addItems(["BNI", "BRI", "BCA", "BSI", "Mandiri", "Lainnya"])

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(286, 499, 241, 51))
        self.pushButton.setStyleSheet("background-color:#DBD4B4;\n"
                                      "border-radius:5px;\n"
                                      "font-size:20px;")
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.save_transaction)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transaksi"))
        self.label_3.setText(_translate("MainWindow", "Selamat Datang"))
        self.label_4.setText(_translate("MainWindow", "Rumah Kita Peduli Bersama"))
        self.label.setText(_translate("MainWindow", "Donatur"))
        self.lineEdit_donatur.setPlaceholderText(_translate("MainWindow", "Masukkan nama donatur"))
        self.label_2.setText(_translate("MainWindow", "Nominal"))
        self.lineEdit_nominal.setPlaceholderText(_translate("MainWindow", "Masukkan nominal"))
        self.label_6.setText(_translate("MainWindow", "Pembayaran"))
        self.pushButton.setText(_translate("MainWindow", "Simpan"))

    def save_transaction(self):
        donatur = self.lineEdit_donatur.text()
        nominal = self.lineEdit_nominal.text()
        pembayaran = self.comboBox_payment.currentText()

        if not donatur or not nominal:
            self.show_message("Gagal", "Semua field harus diisi.")
            return

        try:
            # Ambil data donatur sebelumnya
            query_get_data = """
            SELECT d.id_donatur, COALESCE(SUM(t.jumlah_donasi), 0) AS jumlah_donasi
            FROM donatur d
            LEFT JOIN transaksi t ON t.id_donatur = d.id_donatur
            WHERE d.nama_donatur = %s
            GROUP BY d.id_donatur
            """
            self.cursor.execute(query_get_data, (donatur,))
            result = self.cursor.fetchone()  # Ambil hasil query

            nominal = float(nominal)  # Konversi nominal ke float
            tanggal_transaksi = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Format tanggal dan waktu

            if result:
                # Data donatur ditemukan, tambahkan transaksi baru
                id_donatur = result[0]
                jumlah_donasi_baru = float(result[1]) + nominal  # Hitung jumlah donasi baru

                # Tambahkan transaksi baru (tidak menimpa data lama)
                query_insert = """
                INSERT INTO transaksi (id_donatur, jumlah_donasi, jenis_pembayaran, tanggal_transaksi)
                VALUES (%s, %s, %s, %s)
                """
                self.cursor.execute(query_insert, (id_donatur, nominal, pembayaran, tanggal_transaksi))
            else:
                # Data donatur tidak ditemukan
                self.show_message("Gagal", "Donatur tidak ditemukan.")
                return

            self.db_connection.commit()  # Simpan perubahan
            self.show_message("Berhasil", "Data transaksi berhasil diperbarui.")
            self.clear_fields()  # Bersihkan input
            self.centralwidget.parent().close()
        except Exception as e:
            self.show_message("Gagal", f"Terjadi kesalahan: {str(e)}")

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def clear_fields(self):
        self.lineEdit_donatur.clear()
        self.lineEdit_nominal.clear()
        self.comboBox_payment.setCurrentIndex(0)

    
class DetailDialog(QDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detail Donatur")
        self.setModal(True)
        self.resize(400, 300)
        
        layout = QVBoxLayout()
        
        # Create labels for each field
        fields = [
            ("ID Donatur:", str(data[0])),
            ("Nama:", data[1]),
            ("Email:", data[2]),
            ("Kategori:", data[3]),
            ("ID Transaksi:", str(data[4])),
            ("Nominal:", f"Rp {data[5]:,.2f}"),
            ("Pembayaran:", data[6]),
            ("Tanggal Pembayaran:", data[7])  # Added new field
        ]
        
        for label, value in fields:
            layout.addWidget(QLabel(f"{label} {value}"))
        
        close_button = QPushButton("Tutup")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        
        self.setLayout(layout)

class EditDialog(QDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Data")
        self.setModal(True)
        self.resize(400, 400)
        self.data = data
        
        layout = QVBoxLayout()
        
        # Create input fields
        self.fields = {}
        # In the EditDialog class, modify the field names and initial values:
        field_names = ["Nama", "Email", "Kategori", "Nominal", "Pembayaran", "Tanggal Pembayaran"]  # Added new 
        initial_values = [data[1], data[2], data[3], str(data[5]), data[6], data[7]]  # Added new value
        
        for name, value in zip(field_names, initial_values):
            layout.addWidget(QLabel(name))
            line_edit = QLineEdit(value)
            self.fields[name] = line_edit
            layout.addWidget(line_edit)
        
        # Buttons
        save_button = QPushButton("Simpan")
        save_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Batal")
        cancel_button.clicked.connect(self.reject)
        
        layout.addWidget(save_button)
        layout.addWidget(cancel_button)
        
        self.setLayout(layout)
    
    def get_updated_data(self):
        return {name: field.text() for name, field in self.fields.items()}

# form dasboard super admin
class UI_SuperAdmin(object):
    def __init__(self):
        self.setup_database_connection()

    # fungsi untuk menyambungkan ke database
    def setup_database_connection(self):
        try:
            self.db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="aplikasi_pengelolaan_donasi"
            )
            self.cursor = self.db_connection.cursor()
        except Error as e:
            QMessageBox.critical(None, "Database Error", f"Tidak dapat terhubung ke database: {str(e)}")
            sys.exit(1)
    
    def setupUi(self, MainWindow):
        self.current_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 881, 671))
        self.frame.setStyleSheet("background-color:#CC95C0;")                       
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Header frame
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(80, 20, 631, 121))
        self.frame_5.setStyleSheet("background-color:#DBD4B4;\nborder-radius:20px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        # Welcome text
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(230, 20, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Selamat Datang")  # Set text directly

        # Organization name
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(160, 70, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Rumah Kita Peduli Bersama")  # Set text directly

        # Logo
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 141, 121))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../Downloads/bg-transparent-bank.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
                
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 243, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(21)
        
        
        
        # Search components
        self.lineEditSearch = QtWidgets.QLineEdit(self.frame)
        self.lineEditSearch.setGeometry(QtCore.QRect(110, 160, 250, 30))
        self.lineEditSearch.setPlaceholderText("Cari...")
        self.lineEditSearch.setStyleSheet("border-radius: 5px; background-color: white;")
        self.lineEditSearch.setObjectName("lineEditSearch")

        self.btnSearch = QtWidgets.QPushButton(self.frame)
        self.btnSearch.setGeometry(QtCore.QRect(370, 160, 100, 30))
        self.btnSearch.setStyleSheet("background-color:white; border-radius:10px;")
        self.btnSearch.setText("Search")
        self.btnSearch.setObjectName("btnSearch")

        # Table setup
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(110, 200, 631, 280))
        self.tableWidget.setColumnCount(8)  # Changed from 7 to 8
        self.tableWidget.setHorizontalHeaderLabels([
            "Donatur ID", "Nama", "Email", "Kategori", 
            "Transaksi ID", "Nominal", "Pembayaran", "Tanggal Pembayaran"  # Added new column
        ])
        self.tableWidget.setObjectName("tableWidget")

        # Action buttons
        button_width = 137
        button_height = 28
        button_style = "background-color:#DBD4B4; border-radius:10px;"
        button_margin_left = 20

        self.btnRefresh = QtWidgets.QPushButton(self.frame)
        self.btnRefresh.setGeometry(QtCore.QRect(110, 500, button_width, button_height))
        self.btnRefresh.setStyleSheet(button_style)
        self.btnRefresh.setText("Refresh")
        self.btnRefresh.setObjectName("btnRefresh")

        self.btnEdit = QtWidgets.QPushButton(self.frame)
        self.btnEdit.setGeometry(QtCore.QRect(110 + button_width + button_margin_left, 500, button_width, button_height))
        self.btnEdit.setStyleSheet(button_style)
        self.btnEdit.setText("Edit")
        self.btnEdit.setObjectName("btnEdit")

        self.btnDelete = QtWidgets.QPushButton(self.frame)
        self.btnDelete.setGeometry(QtCore.QRect(110 + 2 * (button_width + button_margin_left), 500, button_width, button_height))
        self.btnDelete.setStyleSheet(button_style)
        self.btnDelete.setText("Hapus")
        self.btnDelete.setObjectName("btnDelete")

        self.btnDetail = QtWidgets.QPushButton(self.frame)
        self.btnDetail.setGeometry(QtCore.QRect(110 + 3 * (button_width + button_margin_left), 500, button_width, button_height))
        self.btnDetail.setStyleSheet(button_style)
        self.btnDetail.setText("Detail")
        self.btnDetail.setObjectName("btnDetail")

        # Adjust button position to align with table
        self.btnRefresh.move(110, 500)
        self.btnEdit.move(110 + button_width + button_margin_left, 500)
        self.btnDelete.move(110 + 2 * (button_width + button_margin_left), 500)
        self.btnDetail.move(110 + 3 * (button_width + button_margin_left), 500)
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Menu and status bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Connect button signals to slots
        self.btnSearch.clicked.connect(self.search_data)
        self.btnEdit.clicked.connect(self.edit_data)
        self.btnDelete.clicked.connect(self.delete_data)
        self.btnDetail.clicked.connect(self.show_detail)
        self.btnRefresh.clicked.connect(self.load_data)
        
        # Connect search box enter key
        self.lineEditSearch.returnPressed.connect(self.search_data)
        
        # Setup table selection
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        
        # Adjust column widths
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        
        # Load initial data
        self.load_data()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Selamat Datang"))
        self.label_4.setText(_translate("MainWindow", "Rumah Kita Peduli Bersama"))

    def search_data(self):
        search_text = self.lineEditSearch.text().strip()
        if not search_text:
            self.load_data()
            return
            
        query = """
            SELECT 
                d.id_donatur,
                d.nama_donatur,
                d.email_donatur,
                d.kategori_donatur,
                t.id_transaksi,
                t.jumlah_donasi,
                t.jenis_pembayaran,
                t.tanggal_transaksi  
            FROM 
                donatur d
            LEFT JOIN 
                transaksi t ON d.id_donatur = t.id_donatur
            WHERE 
                d.nama_donatur LIKE %s OR
                d.email_donatur LIKE %s OR
                d.kategori_donatur LIKE %s OR
                t.jenis_pembayaran LIKE %s
            ORDER BY 
                d.id_donatur DESC
            """
        search_pattern = f"%{search_text}%"
        try:
            self.cursor.execute(query, (search_pattern, search_pattern, search_pattern, search_pattern))
            self.display_results(self.cursor.fetchall())
        except Error as e:
            QMessageBox.warning(None, "Search Error", f"Error dalam pencarian: {str(e)}")

    def edit_data(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(None, "Warning", "Pilih data yang akan diedit")
            return
        
        # Ambil data dari baris yang dipilih
        row_data = self.get_row_data(selected_row)  # Ambil data yang ada di tabel
        dialog = EditDialog(row_data, self.centralwidget)  # Buka dialog dengan data yang sudah ada
        
        if dialog.exec_() == QDialog.Accepted:
            # Ambil data yang diperbarui dari dialog
            updated_data = dialog.get_updated_data()

            try:
                # Bersihkan dan konversi nilai nominal
                nominal_str = updated_data.get('Nominal', '').replace('Rp ', '').replace(',', '')
                try:
                    nominal_value = float(nominal_str)
                except ValueError:
                    QMessageBox.critical(None, "Error", "Format nominal tidak valid. Harap periksa kembali.")
                    return

                # Validasi tanggal pembayaran
                tanggal_pembayaran = updated_data.get('Tanggal Pembayaran', '')
                if not tanggal_pembayaran:
                    QMessageBox.critical(None, "Error", "Tanggal pembayaran tidak boleh kosong.")
                    return

                # Periksa apakah data benar-benar berubah sebelum update
                if (updated_data['Nama'] != row_data[1] or
                    updated_data['Email'] != row_data[2] or
                    updated_data['Kategori'] != row_data[3] or
                    nominal_value != row_data[5] or
                    updated_data['Pembayaran'] != row_data[6]):

                    # Pastikan bahwa ID yang digunakan untuk update benar dan valid
                    donatur_id = row_data[0]  # ID Donatur
                    transaksi_id = row_data[4]  # ID Transaksi
                    
                    if not donatur_id or not transaksi_id:
                        QMessageBox.critical(None, "Error", "ID donatur atau transaksi tidak valid.")
                        return

                    # Update data donatur (nama, email, kategori donatur)
                    donatur_query = """
                    UPDATE donatur 
                    SET nama_donatur = %s, 
                        email_donatur = %s, 
                        kategori_donatur = %s 
                    WHERE id_donatur = %s
                    """
                    self.cursor.execute(donatur_query, (
                        updated_data['Nama'],
                        updated_data['Email'],
                        updated_data['Kategori'],
                        donatur_id  # ID Donatur
                    ))

                    # Update transaksi (nominal dan pembayaran)
                    transaksi_query = """
                    UPDATE transaksi 
                    SET jumlah_donasi = %s, 
                        jenis_pembayaran = %s,
                        tanggal_transaksi = %s 
                    WHERE id_transaksi = %s
                    """
                    self.cursor.execute(transaksi_query, (
                        nominal_value,  # Nominal yang sudah dikonversi
                        updated_data['Pembayaran'],
                        tanggal_pembayaran,
                        transaksi_id  # ID Transaksi
                    ))

                    # Commit perubahan ke database
                    self.db_connection.commit()
                    self.load_data()  # Muat ulang data setelah perubahan
                    QMessageBox.information(None, "Success", "Data berhasil diperbarui")
                else:
                    QMessageBox.information(None, "No Change", "Tidak ada perubahan data yang dilakukan.")

            except Error as e:
                # Rollback jika ada kesalahan
                self.db_connection.rollback()
                QMessageBox.critical(None, "Error", f"Gagal mengupdate data: {str(e)}")
                
    def show_detail(self):
        selected_row = self.tableWidget.currentRow()
        
        if selected_row < 0:
            QMessageBox.warning(None, "Warning", "Pilih data yang akan ditampilkan")
            return

        try:
            row_data = self.get_row_data(selected_row)

            try:
                nominal = float(row_data[5].replace('Rp ', '').replace(',', ''))
                formatted_nominal = f"Rp {nominal:,.2f}"
            except ValueError:
                formatted_nominal = "Nilai tidak valid"

            message = (
                f"ID Donatur: {row_data[0]}\n"
                f"Nama: {row_data[1]}\n"
                f"Email: {row_data[2]}\n"
                f"Kategori: {row_data[3]}\n"
                f"ID Transaksi: {row_data[4]}\n"
                f"Nominal: {formatted_nominal}\n"
                f"Pembayaran: {row_data[6]}\n"
                f"Tanggal Pembayaran: {row_data[7]}"
            )
            
            QMessageBox.information(None, "Detail Donatur", message)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Terjadi kesalahan: {str(e)}")

    def delete_data(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(None, "Warning", "Pilih data yang akan dihapus")
            return

        reply = QMessageBox.question(None, "Konfirmasi", 
                                    "Anda yakin ingin menghapus data ini?",
                                    QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                # Ambil data baris yang dipilih dari tabel
                row_data = self.get_row_data(selected_row)

                # Validasi ID donatur dan ID transaksi
                id_donatur = row_data[0]  # Pastikan ini adalah ID Donatur yang valid
                id_transaksi = row_data[4]  # Pastikan ini adalah ID Transaksi yang valid

                if not id_donatur or not id_transaksi:
                    QMessageBox.critical(None, "Error", "ID donatur atau transaksi tidak valid.")
                    return

                # Hapus data dari tabel transaksi terlebih dahulu
                delete_transaksi_query = "DELETE FROM transaksi WHERE id_transaksi = %s"
                self.cursor.execute(delete_transaksi_query, (id_transaksi,))

                # Hapus data dari tabel donatur
                delete_donatur_query = "DELETE FROM donatur WHERE id_donatur = %s"
                self.cursor.execute(delete_donatur_query, (id_donatur,))

                # Commit perubahan ke database
                self.db_connection.commit()

                # Muat ulang data di tabel
                self.load_data()

                QMessageBox.information(None, "Success", "Data berhasil dihapus")
            except Error as e:
                # Rollback jika ada kesalahan
                self.db_connection.rollback()
                QMessageBox.critical(None, "Error", f"Gagal menghapus data: {str(e)}")

    def get_row_data(self, row):
        return [self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())]

    def load_data(self):
        try:
            # Gunakan query dengan MAX untuk tanggal terakhir transaksi
            query = """
            SELECT 
                d.id_donatur,
                d.nama_donatur,
                d.email_donatur,
                d.kategori_donatur,
                COUNT(t.id_transaksi) AS jumlah_transaksi,
                SUM(t.jumlah_donasi) AS total_donasi,
                GROUP_CONCAT(t.jenis_pembayaran SEPARATOR ', ') AS metode_pembayaran,
                MAX(t.tanggal_transaksi) AS tanggal_terakhir
            FROM 
                donatur d
            LEFT JOIN 
                transaksi t ON d.id_donatur = t.id_donatur
            GROUP BY 
                d.id_donatur
            ORDER BY 
                d.id_donatur DESC
            """
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            
            # Reset tabel
            self.tableWidget.setRowCount(0)
            
            # Tampilkan data
            for row_number, row_data in enumerate(results):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if data is None:
                        data = ""  # Handle NULL values
                    if column_number == 5 and data:  # Format total donasi
                        data = f"Rp {float(data):,.2f}"
                    if column_number == 7 and data:  # Format tanggal
                        data = str(data)  # Konversi tanggal ke string
                    item = QtWidgets.QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_number, column_number, item)
                    
        except Error as e:
            QMessageBox.critical(None, "Database Error", f"Error mengambil data: {str(e)}")


    def display_results(self, results):
        self.tableWidget.setRowCount(0)
        for row, data in enumerate(results):
            self.tableWidget.insertRow(row)
            for col, value in enumerate(data):
                item = QtWidgets.QTableWidgetItem(
                    f"{value:,.2f}" if col == 5 else str(value)
                )
                if col in [0, 4]:  # ID columns
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.tableWidget.setItem(row, col, item)
                

    def closeEvent(self, event):
        try:
            self.cursor.close()
            self.db_connection.close()
        except Exception as e:
            print(f"Error closing database connection: {str(e)}")
    
    
    
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Create Login Form
    Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())
    
    
