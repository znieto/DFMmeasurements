from ..config import global_settings as gs
from PyQt5.QtWidgets import  QPushButton, QGroupBox, QDialog, QGridLayout

"""
Class containg tools to create and use the forms.
"""
class GUITool(object):

    def loadMainGUI(configfile, mainWindow): 
        """
        This method reads from the ini file and add dynamic buttons to the layout of the window.
        """

        mainWindow.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        #Get the buttons settings from the ini file.
        sections = configfile.sections()


        mainWindow.horizontalGroupBox.setLayout(layout)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        mainWindow.setLayout(windowLayout)
