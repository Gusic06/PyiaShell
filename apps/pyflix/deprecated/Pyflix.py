from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


def Main():

    APP = QApplication([])
    WINDOW = QWidget()
    WINDOW.setWindowTitle("Pyflix")

    label = QLabel(WINDOW)
    label.setText("Hello World!")
    label.setFont(QFont("Arial", 16))

    WINDOW.show()
    APP.exec_()

if __name__ == "__main__":
    Main()