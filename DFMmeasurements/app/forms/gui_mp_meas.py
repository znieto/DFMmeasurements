import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class gui_mp_meas(QDialog):
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        self._new_window = eval('gui_mp_meas')
        self._new_window.showdialog() 
        #gui_mp_meas.showdialog()

    def ft_button(self,theButton):
        theButton.setToolTip('This is an example button')
        theButton.clicked.connect(self.on_click)
        return theButton;
   
    def __init__(self):
        super().__init__()
        self.title = 'DFM Measurements Software'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createGridLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
        self.show()
 
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
 
        theButton = QPushButton('PyQt5', self)
        #https://stackoverflow.com/questions/29588732/qlayout-cannot-add-a-null-widget-to-qgridlayout

        layout.addWidget(self.ft_button(theButton),0,0) 
        layout.addWidget(QPushButton('2'),0,1) 
        layout.addWidget(QPushButton('3'),0,2) 
        layout.addWidget(QPushButton('4'),1,0) 
        layout.addWidget(QPushButton('5'),1,1) 
        layout.addWidget(QPushButton('6'),1,2) 
        layout.addWidget(QPushButton('7'),2,0) 
        layout.addWidget(QPushButton('8'),2,1) 
        layout.addWidget(QPushButton('9'),2,2) 
 
        self.horizontalGroupBox.setLayout(layout)
    def mainWindow():
        app = QApplication(sys.argv)
        ex= gui_mp_meas()
        sys.exit(app.exec_())
