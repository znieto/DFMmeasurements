import sys
import importlib
import app.config.configtools as ct
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QVBoxLayout, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from functools import partial
from app.utils import stringtools   

class gui_main(QWidget):
    
    @pyqtSlot()
    def on_click(self, nameWindow, newSetup,wizard):
        #check whether is a new installation
        #if new installation run wizzard
        #else run as usual.

        if newSetup:
            #run wizard
            print('wizard')
        else:
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
        self.width = 620
        self.height = 200
        self.showMaximized()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: white")
 
    def createButton(self,buttonSettings, aLayout, row, column):
        Title = buttonSettings['title']
        onClickWindow= buttonSettings['windowname']
        ToolTip = buttonSettings['tooltip']
        newSetup = stringtools.str_to_bool(buttonSettings['newsetup'])
        wizard = buttonSettings['wizard'] if 'wizard' in buttonSettings else None
        theButton = QPushButton(Title, self)
        theButton.setToolTip(ToolTip)
        theButton.clicked.connect( partial( self.on_click, nameWindow=onClickWindow,newSetup=newSetup,wizard= wizard))
        
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


