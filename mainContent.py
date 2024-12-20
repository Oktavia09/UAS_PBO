from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 843, 660))
        self.frame.setStyleSheet("background-color:#CC95C0;")
        self.frame.setObjectName("frame")

        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(110, 20, 631, 121))
        self.frame_5.setStyleSheet("background-color:#DBD4B4; border-radius:20px;")
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
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEditSearch = QtWidgets.QLineEdit(self.frame)
        self.lineEditSearch.setGeometry(QtCore.QRect(110, 160, 250, 30))
        self.lineEditSearch.setPlaceholderText("Cari...")
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.lineEditSearch.setToolTip("Enter search query")
        self.lineEditSearch.setStyleSheet("border-radius: 5px; background-color: white;")

        self.btnSearch = QtWidgets.QPushButton(self.frame)
        self.btnSearch.setGeometry(QtCore.QRect(370, 160, 100, 30))  # Adjusted position
        self.btnSearch.setStyleSheet("background-color:white; border-radius:10px;")
        self.btnSearch.setObjectName("btnSearch")

        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(110, 200, 631, 280))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 278))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 631, 280))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)  # Added one column for checkboxes
        self.tableWidget.setHorizontalHeaderLabels(["Select", "No", "Nama", "Alamat", "Jenis Kelamin", "Usia"])

        # Update table styles for row selection and checkbox cell
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #45A0E6;
                color: white;
                gridline-color: white;
            }
            QTableWidget::item:selected {
                background-color: #2E8BC0;  /* Highlight color for selected rows */
            }
            QCheckBox {
                margin-left: 4px;  /* Adjust spacing for checkbox */
                background-color: transparent;
            }
        """)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        data = [
            ("1", "Andi", "Jakarta", "Laki-Laki", "20"),
            ("2", "Budi", "Bandung", "Perempuan", "22"),
            ("3", "Caca", "Bogor", "Laki-Laki", "25"),
            ("4", "Dodi", "Surabaya", "Perempuan", "28"),
            ("5", "Eko", "Yogyakarta", "Laki-Laki", "30"),
            ("5", "Eko", "Yogyakarta", "Laki-Laki", "30"),
            ("5", "Eko", "Yogyakarta", "Laki-Laki", "30"),
            ("5", "Eko", "Yogyakarta", "Laki-Laki", "30"),
        ]

        for row, (no, nama, alamat, jk, usia) in enumerate(data):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(no))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(nama))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(alamat))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(jk))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(usia))

            checkbox = QtWidgets.QCheckBox()
            cell_widget = QtWidgets.QWidget()
            layout = QtWidgets.QHBoxLayout(cell_widget)
            layout.addWidget(checkbox)
            layout.setAlignment(QtCore.Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(layout)
            cell_widget.setStyleSheet("background-color:#45A0E6;")
            self.tableWidget.setCellWidget(row, 0, cell_widget)
            

        self.btnEdit = QtWidgets.QPushButton(self.frame)
        self.btnEdit.setGeometry(QtCore.QRect(110, 550, 93, 28))
        self.btnEdit.setStyleSheet("background-color:#86C0F4; border-radius:10px;")
        self.btnEdit.setObjectName("btnEdit")

        self.btnDelete = QtWidgets.QPushButton(self.frame)
        self.btnDelete.setGeometry(QtCore.QRect(210, 550, 93, 28))
        self.btnDelete.setStyleSheet("background-color:#86C0F4; border-radius:10px;")
        self.btnDelete.setObjectName("btnDelete")

        self.btnDetail = QtWidgets.QPushButton(self.frame)
        self.btnDetail.setGeometry(QtCore.QRect(310, 550, 93, 28))
        self.btnDetail.setStyleSheet("background-color:#86C0F4; border-radius:10px;")
        self.btnDetail.setObjectName("btnDetail")

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
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.btnEdit.setText(_translate("MainWindow", "Edit"))
        self.btnDelete.setText(_translate("MainWindow", "Hapus"))
        self.btnDetail.setText(_translate("MainWindow", "Detail"))

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

