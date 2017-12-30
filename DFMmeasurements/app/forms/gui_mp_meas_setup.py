from PyQt5 import QtCore, QtGui, QtWidgets
from app.core.CalibrationType import Calibration
from PyQt5.QtWidgets import QDialog, QApplication

class gui_mp_meas_setup(QDialog):

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(822, 730)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(640, 680, 156, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lblImage = QtWidgets.QLabel(self)
        self.lblImage.setGeometry(QtCore.QRect(5, 49, 781, 321))
        self.lblImage.setObjectName("lblImage")
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
        self._new_window = None
        # Add labels and buttons to layout
        self.setupUi()        
        self.lblImage.setText(calibration.name)

        


if __name__ == "__main__":
    app = QApplication([])
    ex= gui_mp_meas_setup()
    ex.show()
