import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGroupBox, QDialog, QGridLayout, QLabel, QMenuBar 
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import app.config.global_settings as g
import app.core.MeasurementTools as mt
import os

class gui_mp_meas(QDialog):
    def addImage(self,label, strImage):
        pathimg = os.path.join(g.IMAGE_PATH, strImage)
        pixmap = QPixmap(pathimg)
        label.setPixmap(pixmap)
        return
    
    def setupUi(self):
        self.setObjectName("gui_mp_meas")
        self.resize(822, 730)

        #set Icon Window
        pathimg = os.path.join(g.IMAGE_PATH, 'icon.png')
        self.setWindowIcon(QtGui.QIcon(pathimg))

        self.lblDFMLogo = QtWidgets.QLabel(self)
        self.lblDFMLogo.setObjectName("lblDFMLogo")        
        self.addImage(self.lblDFMLogo,"logo.png")

        self.lblMainTitle = QtWidgets.QLabel(self)
        self.lblMainTitle.setObjectName("lblMainTitle")

        # Set the stylesheet        
        self.setStyleSheet("""
        QDialog {
        background-color: white;
        }       
        """)
        # Set window flags: show button to min or max window, close, etc.
        self.setWindowFlags(Qt.Window
        | Qt.WindowCloseButtonHint
        | Qt.WindowMinimizeButtonHint 
        | Qt.WindowMaximizeButtonHint);

        #region Definition Main Vertical layout
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.addWidget(self.lblDFMLogo)
        self.verticalLayout_2.addWidget(self.lblMainTitle)
        #endregion

        #region System Setup Box
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setMinimumSize(QtCore.QSize(800, 250))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelAnalyzer = QtWidgets.QLabel(self.groupBox)
        self.labelAnalyzer.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelAnalyzer.setFont(font)
        self.labelAnalyzer.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAnalyzer.setObjectName("labelAnalyzer")
        self.verticalLayout.addWidget(self.labelAnalyzer)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxAnalyzer = QtWidgets.QGroupBox(self.frame)
        self.groupBoxAnalyzer.setObjectName("groupBoxAnalyzer")
        
        #region Radio Buttons Pulse
        self.radioPulse_1 = QtWidgets.QRadioButton(self.groupBoxAnalyzer)
        self.radioPulse_1.setGeometry(QtCore.QRect(90, 20, 121, 20))
        self.radioPulse_1.setObjectName("radioPulse_1")
        self.radioPulse_1.toggled.connect(self.radioPulseClicked)

        self.radioPulse_3 = QtWidgets.QRadioButton(self.groupBoxAnalyzer)
        self.radioPulse_3.setGeometry(QtCore.QRect(90, 60, 171, 20))
        self.radioPulse_3.setObjectName("radioPulse_3")
        self.radioPulse_3.toggled.connect(self.radioPulseClicked)

        self.radioPulse_2 = QtWidgets.QRadioButton(self.groupBoxAnalyzer)
        self.radioPulse_2.setGeometry(QtCore.QRect(90, 40, 111, 20))
        self.radioPulse_2.setObjectName("radioPulse_2")
        self.radioPulse_2.toggled.connect(self.radioPulseClicked)

        self.radioPulse_4 = QtWidgets.QRadioButton(self.groupBoxAnalyzer)
        self.radioPulse_4.setGeometry(QtCore.QRect(90, 80, 141, 20))
        self.radioPulse_4.setObjectName("radioPulse_4")
        self.radioPulse_4.toggled.connect(self.radioPulseClicked)
        #endregion

        self.horizontalLayout.addWidget(self.groupBoxAnalyzer)
        self.groupBoxSetup = QtWidgets.QGroupBox(self.frame)
        self.groupBoxSetup.setTitle("")
        self.groupBoxSetup.setObjectName("groupBoxSetup")
        self.radioBK = QtWidgets.QRadioButton(self.groupBoxSetup)
        self.radioBK.setGeometry(QtCore.QRect(50, 60, 181, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioBK.sizePolicy().hasHeightForWidth())
        self.radioBK.setSizePolicy(sizePolicy)
        self.radioBK.setObjectName("radioBK")
        self.radioBK.toggled.connect(self.radioSetupClicked)
        self.radioATCal = QtWidgets.QRadioButton(self.groupBoxSetup)
        self.radioATCal.setGeometry(QtCore.QRect(50, 40, 101, 20))
        self.radioATCal.setObjectName("radioATCal")
        self.radioATCal.toggled.connect(self.radioSetupClicked)
        self.horizontalLayout.addWidget(self.groupBoxSetup)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addWidget(self.groupBox)

        #endregion

        #region Bottom background image
        self.lblDFMImg = QtWidgets.QLabel(self)
        self.lblDFMImg.setObjectName("lblDFMImg")
        self.verticalLayout_2.addWidget(self.lblDFMImg)
        self.addImage(self.lblDFMImg,"cover_mp_meas.jpg")
        #endregion

        self.retranslateUi(self)

        self.buttonBox.clicked.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)        
        return

    def accept(self):
        self.Validation()
        self.close

    def buttonClicked(self):
         #partial( self.on_click, nameWindow=onClickWindow)
        self.close

    def radioPulseClicked(self):
        self.changeColor(False,self.groupBoxAnalyzer)
        self.labelAnalyzer.setText("")
        self.labelAnalyzer.setStyleSheet("")

    def radioSetupClicked(self):
        self.changeColor(False,self.groupBoxSetup)
        self.labelAnalyzer.setText("")
        self.labelAnalyzer.setStyleSheet("")


    def retranslateUi(self, gui_mp_meas):
        _translate = QtCore.QCoreApplication.translate
        gui_mp_meas.setWindowTitle(_translate("gui_mp_meas", "Dialog"))
        #self.lblDFMLogo.setText(_translate("gui_mp_meas", "Logo DFM"))
        self.lblMainTitle.setText(_translate("gui_mp_meas", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Pressure reciprocity measurement program</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Version 3.0 - 2017-09-22</span></p></body></html>"))
        self.groupBox.setTitle(_translate("gui_mp_meas", "System Setup"))
        #self.labelAnalyzer.setText(_translate("gui_mp_meas", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">NB! Select Analyzer first</span></p></body></html>"))
        self.groupBoxAnalyzer.setTitle(_translate("gui_mp_meas", "Pulse Analyzer"))
        self.radioPulse_1.setText(_translate("gui_mp_meas", "&3560C-25 kHz"))
        self.radioPulse_3.setText(_translate("gui_mp_meas", "&3560D-Slot3-100 kHz"))
        self.radioPulse_2.setText(_translate("gui_mp_meas", "&3560C-100 kHz"))
        self.radioPulse_4.setText(_translate("gui_mp_meas", "&3560D-Slot4 100 kHz"))
        self.radioBK.setText(_translate("gui_mp_meas", "BK 5998"))
        self.radioATCal.setText(_translate("gui_mp_meas", "AT Cal. App"))
        #self.lblDFMImg.setText(_translate("gui_mp_meas", "<html><head/><body><p align=\"center\">Authors: Knud Rassmussen &amp; Salvador Barrera-Figueroa</p><p align=\"center\">Python version: Zoraya?</p></body></html>"))

    def Validation(self):
        iScheck= False
        for radiobox in  self.findChildren(QtWidgets.QRadioButton):
            groupbox = radiobox.parent()

            if radiobox.isChecked() and (groupbox == self.groupBoxAnalyzer):
                 iScheck=True
                 break

        _translate = QtCore.QCoreApplication.translate
        if not iScheck:
            self.labelAnalyzer.setStyleSheet("""
                         background-color: yellow;
                        """)        
            self.labelAnalyzer.setText(_translate("gui_mp_meas", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">NB! Select Analyzer first</span></p></body></html>"))
            self.changeColor(True,self.groupBoxAnalyzer)

        if not (self.radioATCal.isChecked() or self.radioBK.isChecked()):
            self.labelAnalyzer.setStyleSheet("""
                         background-color: yellow;
                        """)        
            self.labelAnalyzer.setText(_translate("gui_mp_meas", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">NB! Select AT Cal or BK 5998 </span></p></body></html>"))
            self.changeColor(True,self.groupBoxSetup)

    def changeColor(self, changeColor, groupBox):
        if changeColor:                        
            groupBox.setStyleSheet("""
            QRadioButton::indicator::unchecked{ 
                border: 1px solid; 
                border-color: rgb(132,132,132);
                border-radius: 5px;
                background-color: red; 
                width: 11px; 
                height: 11px; 
            }""")
        else:
            groupBox.setStyleSheet("")     

    def helpMenu(self):
        self.myQMenuBar = QMenuBar(self)
        exitMenu = self.myQMenuBar.addMenu('File')
        exitAction = QtWidgets.QAction('Exit', self)        
        exitAction.triggered.connect(self.close)
        exitMenu.addAction(exitAction)


    def __init__(self):
        super().__init__()
        self._new_window = None
        # Add labels and buttons to layout
        self.setupUi()
        self.helpMenu()
       







if __name__ == '__main__':
    app = QApplication([])
    ex= gui_mp_meas()
    ex.show()