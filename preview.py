import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Window(QWidget):
    def __init__(self,parent=None):
        super(Window,self).__init__(parent)
        color = QColor(128,128,128)
        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)
        self.initUI()
        self.show()
    def initUI(self):
        self.setMaximumWidth(600)
        self.setMaximumHeight(600)
        self.setMinimumSize(300, 300)
        grid=QGridLayout()


app=QApplication([])
window=Window()
app.exec_()

