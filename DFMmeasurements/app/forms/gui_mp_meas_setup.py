from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QPixmap
from PyQt5.Qt import QSize
from app.core.CalibrationType import Calibration
from PyQt5.QtWidgets import QDialog, QApplication
import app.utils.guitools as guiutil
import os
import app.config.global_settings as g

class gui_mp_meas_setup(QDialog):
    current_calibration =None
    def setupUi(self):
        width=1100
        height=730

        #set Icon Window
        pathimg = os.path.join(g.IMAGE_PATH, 'icon.png')
        self.setWindowIcon(QtGui.QIcon(pathimg))

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
            guiutil.addImageScaled(self.lblImage,"MpCal-BK.png",width-10,height-10)
        
               
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)



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
