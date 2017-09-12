import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QHBoxLayout, QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt

class gui_mp_meas_copy(QDialog):
    # Set the stylesheet
    def initStyle(self):
        self.setStyleSheet("background-color: white")
        return 

    def setupUi(self, gui_mp_meas):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        self.horizontalGroupBox.setLayout(layout)
        #start layout
                # Create widget
        label = QLabel(self)
        pixmap = QPixmap('C:\\ZNF\\Work\\Python\\DFMmeasurements\\DFMmeasurements\\app\\images\\logo.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())

        #self.resize(100,100)
        layout.addWidget(label,0,0)
        #end layout

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        
        return 

    def __init__(self):
        super().__init__()
        self._new_window = None
        #Start Windows look
        self.title = 'PyQt5 image - pythonspot.com'
        self.width = 640
        self.height = 480
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)

        # End window look

        #Center Window
        size=self.size()
        desktopSize=QDesktopWidget().screenGeometry()
        top=(desktopSize.height()/2)-(size.height()/2)
        left=(desktopSize.width()/2)-(size.width()/2)
        self.move(left, top)


        # Set the stylesheet
        self.initStyle();
        # Add labels and buttons to layout
        self.initUI()







if __name__ == '__main__':
    app = QApplication([])
    gui = NewWindow()
    gui.show()
    app.exec_()
