import sys
import importlib
import app.config.configtools as ct
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from . import gui_mp_meas
from functools import partial
    
class gui_main(QDialog):
    
    @pyqtSlot()
    def on_click(self, nameWindow):
        #import dynamic a window class
        mWindow=importlib.import_module('app.forms.'+nameWindow)
        #create an object of type nameWindow
        self._new_window = eval('mWindow.'+nameWindow+'()')
        #show the window
        self._new_window.show()
        return;
 
    def __init__(self):
        super().__init__()
        self._new_window = None
        self.title = 'DFM Measurements Software'
        self.left = 150
        self.top = 150
        self.width = 320
        self.height = 100
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
    def createButton(self,buttonSettings, aLayout, row, column):
        Title = buttonSettings['title']
        onClickWindow= buttonSettings['windowname']
        ToolTip = buttonSettings['tooltip']
        theButton = QPushButton(Title, self)
        theButton.setToolTip('This is an example button')
        theButton.clicked.connect( partial( self.on_click, nameWindow=onClickWindow))
        
        aLayout.addWidget(theButton,row,column) 

        return theButton

    def createGridLayout(self, configfile):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)        

        # Get the buttons settings from the ini file.
        sections = configfile.sections()        
        i=0
        for section in sections:
            self.createButton(ct.AppConfig.configSectionMap(section,configfile),layout,0,i)
            i+=1
 
        self.horizontalGroupBox.setLayout(layout)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

    def mainWindow(configfile):
            app = QApplication(sys.argv)
            ex= gui_main()
            ex.createGridLayout(configfile)
            ex.show();
            sys.exit(app.exec_())


