from PyQt5.QtWidgets import QApplication , QWizard , QWizardPage, QLineEdit, QGroupBox
from PyQt5.QtWidgets import QLabel , QVBoxLayout, QGridLayout, QPushButton, QWidget
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import app.config.configtools as ct
import app.config.global_settings as gs 

class Directories:
      ref_file_path=None
      temp_path= None
      db_calibrations_path= None
      output_path = None

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
  
  
def createRegistrationPage(measureDirs):
    page = QWizardPage()
    page.setTitle("Setup Directories")
  
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
    browseReference.clicked.connect(lambda: openFileBrowser(textbox=browseReference))
      
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

def openFileBrowser(textbox):
    import app.wizards.openfile_dir as od

    newWindow = od.browserfile()
    newWindow.show()
    print('here')
    


def getAbsoluteDir(directory, rootdirectory):
        import os

        #check that directory string is not empty.
        if directory:
            #is abasulte path? if not add root dir
            isabs= os.path.isabs(directory)
            if not isabs:                
                directory =  os.path.join(rootdirectory, directory)

        return directory  

if __name__ == '__main__':
  
    
  
    #region Debug
    gs.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    gs.DEFAULT_MEASUREMENT_PATH = os.path.join(gs.ROOT_DIR,gs.DEFAULT_MEASUREMENT_PATH)
    section= "PressureReciprocity"
    #endregion

    measureDirs= Directories()
    measurement_path= os.path.join(gs.DEFAULT_MEASUREMENT_PATH, section)
    app = QApplication(sys.argv)
    config= ct.AppConfig(gs.DEFAULT_CONFIG_PATH)    
    loadWorkingDirectories(config,section, measurement_path,measureDirs)
    wizard = QWizard()
    wizard.resize(640, 600)
    wizard.addPage(createIntroPage())
    wizard.addPage(createRegistrationPage(measureDirs))
    wizard.addPage(createConclusionPage())
  
    wizard.setWindowTitle("Trivial Wizard")
    wizard.show()
  
    sys.exit(wizard.exec_())
