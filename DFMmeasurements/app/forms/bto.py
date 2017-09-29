import sys
#import PyQt5.QtWidgets
#from PyQt5.QtWidgets import  QWidget, QPushButton, QGroupBox, QDialog, QGridLayout, QLabel, QMenuBar 
#from PyQt5.QtGui import QIcon, QPixmap
#from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)
        self.setLayout(grid)

        self.setWindowTitle("Group Box")
        self.resize(480, 320)

    def createFirstExclusiveGroup(self):
        groupBox = QtWidgets.QGroupBox("Exclusive Radio Buttons")

        radio1 = QtWidgets.QRadioButton("&Radio button 1")
        radio2 = QtWidgets.QRadioButton("R&adio button 2")
        radio3 = QtWidgets.QRadioButton("Ra&dio button 3")

        radio1.setChecked(True)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def createSecondExclusiveGroup(self):
        groupBox = QtWidgets.QGroupBox("E&xclusive Radio Buttons")
        groupBox.setCheckable(True)
        groupBox.setChecked(False)

        radio1 = QtWidgets.QRadioButton("Rad&io button 1")
        radio2 = QtWidgets.QRadioButton("Radi&o button 2")
        radio3 = QtWidgets.QRadioButton("Radio &button 3")
        radio1.setChecked(True)
        checkBox = QtWidgets.QCheckBox("Ind&ependent checkbox")
        checkBox.setChecked(True)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkBox)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def createNonExclusiveGroup(self):
        groupBox = QtWidgets.QGroupBox("Non-Exclusive Checkboxes")
        groupBox.setFlat(True)

        checkBox1 = QtWidgets.QCheckBox("&Checkbox 1")
        checkBox2 = QtWidgets.QCheckBox("C&heckbox 2")
        checkBox2.setChecked(True)
        tristateBox = QtWidgets.QCheckBox("Tri-&state button")
        tristateBox.setTristate(True)
        tristateBox.setCheckState(QtCore.Qt.PartiallyChecked)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(checkBox1)
        vbox.addWidget(checkBox2)
        vbox.addWidget(tristateBox)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def createPushButtonGroup(self):
        groupBox = QtWidgets.QGroupBox("&Push Buttons")
        groupBox.setCheckable(True)
        groupBox.setChecked(True)

        pushButton = QtWidgets.QPushButton("&Normal Button")
        toggleButton = QtWidgets.QPushButton("&Toggle Button")
        toggleButton.setCheckable(True)
        toggleButton.setChecked(True)
        flatButton = QtWidgets.QPushButton("&Flat Button")
        flatButton.setFlat(True)

        popupButton = QtWidgets.QPushButton("Pop&up Button")
        menu = QtWidgets.QMenu(self)
        menu.addAction("&First Item")
        menu.addAction("&Second Item")
        menu.addAction("&Third Item")
        menu.addAction("F&ourth Item")
        popupButton.setMenu(menu)

        newAction = menu.addAction("Submenu")
        subMenu = QtWidgets.QMenu("Popup Submenu", self)
        subMenu.addAction("Item 1")
        subMenu.addAction("Item 2")
        subMenu.addAction("Item 3")
        newAction.setMenu(subMenu)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(pushButton)
        vbox.addWidget(toggleButton)
        vbox.addWidget(flatButton)
        vbox.addWidget(popupButton)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox


if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())