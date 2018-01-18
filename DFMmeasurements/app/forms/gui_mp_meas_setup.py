from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QPixmap
from PyQt5.Qt import QSize
from app.core.CalibrationType import Calibration
from PyQt5.QtWidgets import QDialog, QApplication
import app.utils.guitools as guiutil

class gui_mp_meas_setup(QDialog):
    current_calibration =None
    def setupUi(self):
        width=1100
        height=730
        self.setObjectName("Dialog")
        self.resize(width, 730)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(640, 680, 156, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lblImage = QtWidgets.QLabel(self)
        self.lblImage.setObjectName("lblImage")

        if(self.current_calibration==Calibration.AT_CAL):
            #image cal     
            guiutil.addImageScaled(self.lblImage,"MpCal-AT.png",width-10,height-10)
        else:
            #image sjlfj
            guiutil.addImage(self.lblImage,"MpCal-BK.emf")
         
        self.lblTitle = QtWidgets.QLabel(self)
        self.lblTitle.setGeometry(QtCore.QRect(340, 0, 111, 20))
        self.lblTitle.setObjectName("lblTitle")        

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblTitle.setText(_translate("Dialog", "Calibration Setup"))

    def __init__(self, parent= None, calibration= None):
        super().__init__()
        self.current_calibration= calibration
        self._new_window = None
        # Add labels and buttons to layout
        self.setupUi()        
        


if __name__ == "__main__":
    app = QApplication([])
    ex= gui_mp_meas_setup()
    ex.show()
