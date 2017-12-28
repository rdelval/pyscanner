import sys
import scanner
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QLineEdit, QFileDialog, QLabel,QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("HP Envy Scanner")
        button = QPushButton("Scan", self)
        button.clicked.connect(self.onClick)
        button.resize(100, 32)
        button.move(0,20)

        self.ipAddrTextbox = QLineEdit(self)

    def onClick(self):
        ip = self.ipAddrTextbox.text()
        filename = QFileDialog.getSaveFileName(self, 'Save as', '~/', '*.pdf')
        stat = scanner.status(ip)
        if stat == "Idle":
            exit_code = scanner.scan(ip, filename[0])
        else:
            QMessageBox.information(self,"Unable to scan", "Sorry, scanner status is '{0}'".format(stat))
            return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

