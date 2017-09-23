import sys
#import PyQt5.QtWidgets
from PyQt5.QtWidgets import  QWidget, QPushButton, QGroupBox, QDialog, QGridLayout, QLabel, QMenuBar 
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class gui_mp_meas(QDialog):
    def addImage(self,label, strImage):
        import app.config.global_settings as g
        import os
        pathimg = os.path.join(g.IMAGE_PATH, strImage)
        pixmap = QPixmap(pathimg)
        label.setPixmap(pixmap)
        return
    
    def setupUi(self):
        self.setObjectName("gui_mp_meas")
        self.resize(822, 730)

        self.lblDFMLogo = QtWidgets.QLabel(self)
        self.lblDFMLogo.setObjectName("lblDFMLogo")        
        self.addImage(self.lblDFMLogo,"logo.png")

        self.lblMainTitle = QtWidgets.QLabel(self)
        self.lblMainTitle.setObjectName("lblMainTitle")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.addWidget(self.lblDFMLogo)
        self.verticalLayout_2.addWidget(self.lblMainTitle)

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setMinimumSize(QtCore.QSize(800, 250))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioPulse = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioPulse.setGeometry(QtCore.QRect(90, 20, 121, 20))
        self.radioPulse.setObjectName("radioPulse")
        self.radioPulse_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioPulse_3.setGeometry(QtCore.QRect(90, 60, 171, 20))
        self.radioPulse_3.setObjectName("radioPulse_3")
        self.radioPulse_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioPulse_2.setGeometry(QtCore.QRect(90, 40, 111, 20))
        self.radioPulse_2.setObjectName("radioPulse_2")
        self.radioPulse_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioPulse_4.setGeometry(QtCore.QRect(90, 80, 141, 20))
        self.radioPulse_4.setObjectName("radioPulse_4")
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioBK = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioBK.setGeometry(QtCore.QRect(50, 60, 181, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioBK.sizePolicy().hasHeightForWidth())
        self.radioBK.setSizePolicy(sizePolicy)
        self.radioBK.setObjectName("radioBK")
        self.radioATCal = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioATCal.setGeometry(QtCore.QRect(50, 40, 101, 20))
        self.radioATCal.setObjectName("radioATCal")
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.lblDFMImg = QtWidgets.QLabel(self)
        self.lblDFMImg.setObjectName("lblDFMImg")
        self.verticalLayout_2.addWidget(self.lblDFMImg)
        self.addImage(self.lblDFMImg,"cover_mp_meas.jpg")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)        
        return

    def buttonClicked(self):
         #partial( self.on_click, nameWindow=onClickWindow)
        self.close

    def retranslateUi(self, gui_mp_meas):
        _translate = QtCore.QCoreApplication.translate
        gui_mp_meas.setWindowTitle(_translate("gui_mp_meas", "Dialog"))
        #self.lblDFMLogo.setText(_translate("gui_mp_meas", "Logo DFM"))
        self.lblMainTitle.setText(_translate("gui_mp_meas", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Pressure reciprocity measurement program</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Version 3.0 - 2017-09-22</span></p></body></html>"))
        self.groupBox.setTitle(_translate("gui_mp_meas", "System Setup"))
        self.textEdit.setHtml(_translate("gui_mp_meas", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">NB! Select Analyzer first</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("gui_mp_meas", "Pulse Analyzer"))
        self.radioPulse.setText(_translate("gui_mp_meas", "&3560C-25 kHz"))
        self.radioPulse_3.setText(_translate("gui_mp_meas", "&3560D-Slot3-100 kHz"))
        self.radioPulse_2.setText(_translate("gui_mp_meas", "&3560C-100 kHz"))
        self.radioPulse_4.setText(_translate("gui_mp_meas", "&3560D-Slot4 100 kHz"))
        self.radioBK.setText(_translate("gui_mp_meas", "BK 5998"))
        self.radioATCal.setText(_translate("gui_mp_meas", "AT Cal. App"))
        #self.lblDFMImg.setText(_translate("gui_mp_meas", "<html><head/><body><p align=\"center\">Authors: Knud Rassmussen &amp; Salvador Barrera-Figueroa</p><p align=\"center\">Python version: Zoraya?</p></body></html>"))


    def __init__(self):
        super().__init__()
        self._new_window = None
        self.setWindowFlags(Qt.Window
        | Qt.WindowCloseButtonHint
        | Qt.WindowMinimizeButtonHint 
        | Qt.WindowMaximizeButtonHint);
          # Set the stylesheet
        self.setStyleSheet("background-color: white")

        # Add labels and buttons to layout
        self.setupUi()
        # help menu
        self.myQMenuBar = QMenuBar(self)
        exitMenu = self.myQMenuBar.addMenu('File')
        exitAction = QtWidgets.QAction('Exit', self)        
        exitAction.triggered.connect(self.close)
        exitMenu.addAction(exitAction)







if __name__ == '__main__':
    app = QApplication([])
    gui = NewWindow()
    gui.show()
    app.exec_()
