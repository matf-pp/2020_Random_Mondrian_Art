import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Random Mondrian Art'
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        #self.resize(490,380)
        grid = QGridLayout()
        self.setLayout(grid)
        #tutorial
        label = QLabel("Choose 3 collors and do something: ")
        grid.addWidget(label,0,1,1,4)
        #
        label1 = QLabel("Colors")
        grid.addWidget(label1,1,0)
        #definisanje prvih klikajucih kvadratica != kockica
        whiteCheck = QCheckBox("White")
        blackCheck = QCheckBox("Black")
        redCheck = QCheckBox("Red")
        yellowCheck = QCheckBox("Yellow")
        #prvi klikajuci kvadratici
        grid.addWidget(whiteCheck,2,0)
        grid.addWidget(blackCheck,2,1)
        grid.addWidget(redCheck,2,2)
        grid.addWidget(yellowCheck,2,3)
        #definisanje prvih klikajucih kvadratica != kockica
        whiteCheck = QCheckBox("White")
        blackCheck = QCheckBox("Black")
        redCheck = QCheckBox("Red")
        yellowCheck = QCheckBox("Yellow")
        #prvi klikajuci kvadratici
        grid.addWidget(whiteCheck,3,0)
        grid.addWidget(blackCheck,3,1)
        grid.addWidget(redCheck,3,2)
        grid.addWidget(yellowCheck,3,3)#definisanje prvih klikajucih kvadratica != kockica
        #
        whiteCheck = QCheckBox("White")
        blackCheck = QCheckBox("Black")
        redCheck = QCheckBox("Red")
        yellowCheck = QCheckBox("Yellow")
        #prvi klikajuci kvadratici
        grid.addWidget(whiteCheck,4,0)
        grid.addWidget(blackCheck,4,1)
        grid.addWidget(redCheck,4,2)
        grid.addWidget(yellowCheck,4,3)#definisanje prvih klikajucih kvadratica != kockica
        #
        whiteCheck = QCheckBox("White")
        blackCheck = QCheckBox("Black")
        redCheck = QCheckBox("Red")
        yellowCheck = QCheckBox("Yellow")
        #prvi klikajuci kvadratici
        grid.addWidget(whiteCheck,5,0)
        grid.addWidget(blackCheck,5,1)
        grid.addWidget(redCheck,5,2)
        grid.addWidget(yellowCheck,5,3)#definisanje prvih klikajucih kvadratica != kockica
        #
        whiteCheck = QCheckBox("White")
        blackCheck = QCheckBox("Black")
        redCheck = QCheckBox("Red")
        yellowCheck = QCheckBox("Yellow")
        #prvi klikajuci kvadratici
        grid.addWidget(whiteCheck,6,0)
        grid.addWidget(blackCheck,6,1)
        grid.addWidget(redCheck,6,2)
        grid.addWidget(yellowCheck,6,3)
        #
        width = QLabel("Width :")
        edit1 = QLineEdit(self)
        grid.addWidget(width,7,0)
        grid.addWidget(edit1,7,1,1,2)
        #
        height = QLabel("Height :")
        edit2 = QLineEdit(self)
        grid.addWidget(height,8,0)
        grid.addWidget(edit2,8,1,1,2)
        #
        button1 = QPushButton(self)
        button1.setText("GamaDelux")
        grid.addWidget(button1,8,3)
        
        button2 = QRadioButton(self)
        button2.setText("GamaPro")
        grid.addWidget(button2,7,3)
        self.show()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = App()
    app.exec_()