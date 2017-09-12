import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QHBoxLayout, QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class gui_mp_meas(QDialog):
    

    def setupUi(self):
        self.setObjectName("gui_mp_meas")
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setAutoFillBackground(False)
        # Set the stylesheet
        self.setStyleSheet("background-color: white")
        self.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblDFMLogo = QtWidgets.QLabel(self)
        self.lblDFMLogo.setObjectName("lblDFMLogo")
        pixmap = QPixmap('C:\\ZNF\\Work\\Python\\DFMmeasurements\\DFMmeasurements\\app\\images\\logo.png')
        self.lblDFMLogo.setPixmap(pixmap)

        self.verticalLayout.addWidget(self.lblDFMLogo)
        self.lblMainTitle = QtWidgets.QLabel(self)
        self.lblMainTitle.setObjectName("lblMainTitle")
        self.verticalLayout.addWidget(self.lblMainTitle, 0, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.formSetup = QtWidgets.QFormLayout()
        self.formSetup.setContentsMargins(50, -1, -1, -1)
        self.formSetup.setVerticalSpacing(17)
        self.formSetup.setObjectName("formSetup")
        self.lblSytemSetup = QtWidgets.QLabel(self)
        self.lblSytemSetup.setObjectName("lblSytemSetup")
        self.formSetup.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblSytemSetup)
        self.radioBK = QtWidgets.QRadioButton(self)
        self.radioBK.setObjectName("radioBK")
        self.formSetup.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.radioBK)
        self.radioATCal = QtWidgets.QRadioButton(self)
        self.radioATCal.setObjectName("radioATCal")
        self.formSetup.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.radioATCal)
        self.btoCloseWindow = QtWidgets.QPushButton(self)
        self.btoCloseWindow.setMaximumSize(QtCore.QSize(100, 150))
        self.btoCloseWindow.setObjectName("btoCloseWindow")
        self.formSetup.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btoCloseWindow)
        self.verticalLayout.addLayout(self.formSetup)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lblDFMImg = QtWidgets.QLabel(self)
        pixmap = QPixmap('C:\\ZNF\\Work\\Python\\DFMmeasurements\\DFMmeasurements\\app\\images\\cover_mp_meas.jpg')
        self.lblDFMImg.setPixmap(pixmap)

        self.lblDFMImg.setObjectName("lblDFMImg")
        self.verticalLayout.addWidget(self.lblDFMImg)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        return 

    def retranslateUi(self, gui_mp_meas):
        _translate = QtCore.QCoreApplication.translate
        gui_mp_meas.setWindowTitle(_translate("gui_mp_meas", "Pressure Reciprocity Measurement"))
        self.lblMainTitle.setText(_translate("gui_mp_meas", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Pressure reciprocity measurement program</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Version 2.1 - 2017-09-12</span></p></body></html>"))
        self.lblSytemSetup.setText(_translate("gui_mp_meas", "<html><head/><body><p><span style=\" font-size:10pt;\">System Setup</span></p></body></html>"))
        self.radioBK.setText(_translate("gui_mp_meas", "BK 5998"))
        self.radioATCal.setText(_translate("gui_mp_meas", "AT Cal. App"))
        self.btoCloseWindow.setText(_translate("gui_mp_meas", "Close Window"))
        self.label_3.setText(_translate("gui_mp_meas", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\">Authors: Knud Rassmussen &amp; Salvador Barrera-Figueroa</p><p align=\"center\">Python version: Zoraya?</p></body></html>"))

    def __init__(self):
        super().__init__()
        self._new_window = None
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)
        # Add labels and buttons to layout
        self.setupUi()







if __name__ == '__main__':
    app = QApplication([])
    gui = NewWindow()
    gui.show()
    app.exec_()
