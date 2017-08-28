import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class gui_mp_meas(QDialog):
    def __init__(self):
        super().__init__()
        self._new_window = None


if __name__ == '__main__':
    app = QApplication([])
    gui = NewWindow()
    gui.show()
    app.exec_()
