"""
module containg tools to work with Forms
"""
import app.config.global_settings as g
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
import os


def addImage(label, strImage):
    pathimg = os.path.join(g.IMAGE_PATH, strImage)
    pixmap = QPixmap(pathimg)
    label.setPixmap(pixmap)
    return

def addImageScaled(label, strImage,width,height):
    pathimg = os.path.join(g.IMAGE_PATH, strImage)
    pixmap = QPixmap(pathimg).scaled(width, height, QtCore.Qt.KeepAspectRatio)
    
    label.setPixmap(pixmap)
    return
