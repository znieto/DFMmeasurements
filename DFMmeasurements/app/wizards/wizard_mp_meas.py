from PyQt5.QtWidgets import QApplication , QWizard , QWizardPage, QLineEdit, QGroupBox
from PyQt5.QtWidgets import QLabel , QVBoxLayout, QGridLayout, QPushButton, QWidget
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import app.config.configtools as ct
import app.config.global_settings as gs 
import logging

class Directories:
      ref_file_path = None
      temp_path = None
      db_calibrations_path = None
      output_path = None
      def toArray(self):
          return [this.ref_file_path,this.temp_path,this.db_calibrations_path,this.output_path]
      def toDictionary(self):
          dict1 =  {"ref_file_path" : self.ref_file_path, "temp_path" : self.temp_path, "db_calibrations_path" :self.db_calibrations_path,
            "output_path":self.output_path}
          return dict1


currentConfigSection = None
measureDirs = Directories()
#wizard = None


def createIntroPage():
    page = QWizardPage()
    page.setTitle("Introduction")
  
    label = QLabel("This wizard will help you register the directories need for"
            " Pressure reciprocity Software.")
    label.setWordWrap(True)
  
    layout = QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)
  
    return page
  
  
def createRegistrationPage(measureDirs, titleRegistrationPage):
    page = QWizardPage()
    page.setTitle(titleRegistrationPage)
    groupBox = QGroupBox(page)
    #groupBox.setGeometry(QRect(-10, 8, 631, 400))
    groupBox.setObjectName("groupBox")
    groupBox.setTitle("Select the following directories")
    gridlayout = QtWidgets.QGridLayout(groupBox)
    gridlayout.setContentsMargins(8, 8, 8, 8)
    gridlayout.setSpacing(6)
       
    #region Reference
    labelReference = QLabel(groupBox)
    labelReference.setText("Referece:")
    gridlayout.addWidget(labelReference, 0, 0)
    refernceDir = QtWidgets.QLineEdit(groupBox)
    refernceDir.setObjectName("refernceDir")
    refernceDir.setText(measureDirs.ref_file_path)
    gridlayout.addWidget(refernceDir, 0, 1)
    browseReference = QtWidgets.QPushButton(groupBox)
    browseReference.setDefault(True)
    browseReference.setObjectName("browseReference")
    browseReference.setText("Browse")
    browseReference.clicked.connect(lambda: openFileBrowser(textbox=refernceDir))
      
    gridlayout.addWidget(browseReference, 0, 2)
    #endregion

    #region database
    labelDatabase = QLabel(groupBox)
    labelDatabase.setText("Database:")
    gridlayout.addWidget(labelDatabase, 1, 0)
    databaseDir = QtWidgets.QLineEdit(groupBox)
    databaseDir.setObjectName("databaseDir")
    databaseDir.setText(measureDirs.db_calibrations_path)
    gridlayout.addWidget(databaseDir, 1, 1)
    browseDatabase = QtWidgets.QPushButton(groupBox)
    browseDatabase.setDefault(True)
    browseDatabase.setObjectName("browseReference")
    browseDatabase.setText("Browse")
    browseDatabase.clicked.connect(lambda: openFileBrowser(textbox=databaseDir))
    gridlayout.addWidget(browseDatabase, 1, 2)
    #endregion

    #region Output Results
    labelOutput = QtWidgets.QLabel(groupBox)
    labelOutput.setText("Output")
    gridlayout.addWidget(labelOutput, 2, 0)
    destinationFolder = QtWidgets.QLineEdit(groupBox)
    destinationFolder.setFocusPolicy(QtCore.Qt.StrongFocus)
    destinationFolder.setObjectName("destinationFolder")
    destinationFolder.setText(measureDirs.output_path)
    gridlayout.addWidget(destinationFolder, 2, 1)
    browseDestination = QtWidgets.QPushButton(groupBox)
    browseDestination.setObjectName("browseDestination")
    browseDestination.setText("Browse")
    browseDestination.clicked.connect(lambda: openFileBrowser(textbox=destinationFolder))
    gridlayout.addWidget(browseDestination, 2, 2)
    #endregion
    widget = QWidget(groupBox)
    widget.setGeometry(QRect(10, 40, 364, 33))
    widget.setObjectName("widget")
    return page
  
  
def createConclusionPage():
    page = QWizardPage()
    page.setTitle("Conclusion")  
    label = QLabel("You are now successfully registered. Have a nice day!")
    label.setWordWrap(True)
    layout = QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)
  
    return page


def loadWorkingDirectories(config,section, filesdirectory, measureDirs):
    measureDirs.ref_file_path = getAbsoluteDir(config.getOption(section,'REF_FILE_PATH'),filesdirectory)
    measureDirs.temp_path = getAbsoluteDir(config.getOption(section,'TEMP_PATH'),filesdirectory)
    measureDirs.db_calibrations_path = getAbsoluteDir(config.getOption(section,'DB_CALIBRATIONS_PATH'),filesdirectory)
    measureDirs.output_path = getAbsoluteDir(config.getOption(section,'OUTPUT_PATH'),filesdirectory)

def createDirectories():
    import app.utils.oitools as iotools
    success= iotools.createDir(measureDirs.ref_file_path) and iotools.createDir(measureDirs.db_calibrations_path) and iotools.createDir(measureDirs.output_path)
    return success

def updateIniDir(config,section,dirDictionary):
    for k, v in dirDictionary.items():
        config.save_option(section,k,v)


def next(section,config,wizard):
    if wizard.currentPage().isFinalPage():
       #Create directories
       if createDirectories():
           #if not error, update ini
           updateIniDir(config,section,measureDirs.toDictionary())
           #update newsetup option on ini file
           config.save_option(section,"NewSetup","False")
       else:
           logging.warning("can update ini file")

#def finish(section,config):
#    import importlib
#    nameWindow = config.getOption(section, "windowname")
#    #import dynamic a window class
#    mWindow=importlib.import_module('app.forms.'+nameWindow)
#    #create an object of type nameWindow
#    _new_window = eval('mWindow.'+nameWindow+'()')
#    #show the window
#    _new_window.show()



def openFileBrowser(textbox):
    import app.wizards.openfile_dir as od

    newWindow = od.browserfile()
    newWindow.openFolderDialog()
    newWindow.show()
    textbox.setText(newWindow.currentdir)
    


def getAbsoluteDir(directory, rootdirectory):
        import os

        #check that directory string is not empty.
        if directory:
            #is abasulte path?  if not add root dir
            isabs = os.path.isabs(directory)
            if not isabs:                
                directory = os.path.join(rootdirectory, directory)

        return directory  

if __name__ == '__main__':
  
    
  
    #region Debug
    import logging
    #logging.basicConfig(filename='myapp.log', level=logging.INFO)
    #logging.info('Started')
    #gs.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    ##to delete gs.DEFAULT_MEASUREMENT_PATH = os.path.join(gs.ROOT_DIR,gs.DEFAULT_MEASUREMENT_PATH)
    #currentConfigSection = "PressureReciprocity"
    #endregion

def show():
    measurement_path = os.path.join(gs.DEFAULT_MEASUREMENT_PATH, currentConfigSection)
    config = ct.AppConfig(gs.DEFAULT_CONFIG_PATH)    
    loadWorkingDirectories(config,currentConfigSection, measurement_path,measureDirs)
    wizard = QWizard()
    wizard.resize(640, 600)
    wizard.addPage(createIntroPage())
    wizard.addPage(createRegistrationPage(measureDirs, currentConfigSection))
    wizard.addPage(createConclusionPage())
  
    wizard.button(QWizard.NextButton).clicked.connect(lambda: next(currentConfigSection,config,wizard))
    #wizard.button(QWizard.FinishButton).clicked.connect(lambda: finish(currentConfigSection,config))

    wizard.setWindowTitle("Trivial Wizard")
    wizard.show()
  
    wizard.exec_()
