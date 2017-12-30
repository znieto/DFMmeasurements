"""
module containg tools to work with Forms
"""
import app.config.global_settings as g
from PyQt5.QtGui import  QPixmap
import os


def addImage(label, strImage):
    pathimg = os.path.join(g.IMAGE_PATH, strImage)
    pixmap = QPixmap(pathimg)
    label.setPixmap(pixmap)
    return

