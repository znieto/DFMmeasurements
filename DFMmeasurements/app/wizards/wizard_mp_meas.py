from PyQt5.QtWidgets import QApplication , QWizard , QWizardPage, QLineEdit, QGroupBox
from PyQt5.QtWidgets import QLabel , QVBoxLayout, QGridLayout, QPushButton, QWidget
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
  
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
  
  
def createRegistrationPage():
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
    gridlayout.addWidget(refernceDir, 0, 1)
    browseReference = QtWidgets.QPushButton(groupBox)
    browseReference.setDefault(True)
    browseReference.setObjectName("browseReference")
    browseReference.setText("Browse")
    gridlayout.addWidget(browseReference, 0, 2)
    #endregion

    #region database
    labelDatabase = QLabel(groupBox)
    labelDatabase.setText("Database:")
    gridlayout.addWidget(labelDatabase, 1, 0)
    databaseDir = QtWidgets.QLineEdit(groupBox)
    databaseDir.setObjectName("databaseDir")
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
  
def retranslateUi(page):
    _translate = QtCore.QCoreApplication.translate

    page.groupBox.setTitle(_translate("SetupDir", "Select the following directories"))
    #wizard.label_Output.setText(_translate("SetupDir", "Output"))
    #wizard.browseReference.setText(_translate("SetupDir", "Browse"))
    #wizard.label_6.setText(_translate("SetupDir", "Creator:"))
    #wizard.labelDatabase.setText(_translate("SetupDir", "Database "))
    #wizard.labelReference.setText(_translate("SetupDir", "Reference "))
    #wizard.browseDestination.setText(_translate("SetupDir", "Browse"))
    #wizard.announceUrl.setText(_translate("SetupDir", "<none>"))
    #wizard.creatorLabel.setText(_translate("SetupDir", "<none>"))

if __name__ == '__main__':
  
    import sys
  
    app = QApplication(sys.argv)
  
    wizard = QWizard()
    wizard.resize(640, 600)
    wizard.addPage(createIntroPage())
    wizard.addPage(createRegistrationPage())
    wizard.addPage(createConclusionPage())
  
    wizard.setWindowTitle("Trivial Wizard")
    wizard.show()
  
    sys.exit(wizard.exec_())
