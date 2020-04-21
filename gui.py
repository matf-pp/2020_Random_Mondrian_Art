import sys
#from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
 #       QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import *

class Window(QWidget):
    
    def __init__(self,parent=None):
        super(Window,self).__init__(parent)
        self.whiteCheck=QCheckBox('WHITE')
        self.aquaCheck= QCheckBox("AQUA")
        self.indigoCheck = QCheckBox("INDIGO")
        self.turquoiseCheck = QCheckBox("TURQUOISE")
        self.limeCheck = QCheckBox("LIME")
        self.blackCheck = QCheckBox('BLACK')
        self.blueCheck = QCheckBox("BLUE")
        self.seashellCheck = QCheckBox("SEASHELL")
        self.navyCheck = QCheckBox("NAVY")
        self.coralCheck = QCheckBox("CORAL")
        self.redCheck = QCheckBox('RED')
        self.fuchsiaCheck = QCheckBox("FUCHSIA")
        self.honeydewCheck = QCheckBox("HONEYDEW")
        self.hotpinkCheck = QCheckBox("HOTPINK")
        self.skyblueCheck = QCheckBox("SKYBLUE")
        self.yellowCheck = QCheckBox('YELLOW')
        self.purpleCheck = QCheckBox("PURPLE")
        self.siennaCheck = QCheckBox("SIENNA")
        self.springgreenCheck = QCheckBox("SPRINGGREEN")
        self.khakiCheck = QCheckBox("KHAKI")
        self.color = []
        self.initUI()
        self.show()
    
    def initUI(self):    
        grid=QGridLayout()
        self.whiteCheck.setStyleSheet('color: #ffffff')
        self.aquaCheck.setStyleSheet('color: #00ffff')
        self.indigoCheck.setStyleSheet('color: #4b0082')
        self.turquoiseCheck.setStyleSheet('color: #40e0d0')
        self.limeCheck.setStyleSheet('color: #00ff00')
        self.blackCheck.setStyleSheet('color: #000000')
        self.blueCheck.setStyleSheet('color: #0000ff')
        self.seashellCheck.setStyleSheet('color: #fff5ee')
        self.navyCheck.setStyleSheet('color: #000080')
        self.coralCheck.setStyleSheet('color: #ff7f50' )
        self.redCheck.setStyleSheet('color: #ff0000' )
        self.fuchsiaCheck.setStyleSheet('color: #ff00ff' )
        self.honeydewCheck.setStyleSheet('color: #f0fff0' )
        self.hotpinkCheck.setStyleSheet('color: #ff69b4' )
        self.skyblueCheck.setStyleSheet('color: #87ceeb' )
        self.yellowCheck.setStyleSheet('color: #ffff00')
        self.purpleCheck.setStyleSheet('color: #800080')
        self.siennaCheck.setStyleSheet('color: #a0522d')
        self.springgreenCheck.setStyleSheet('color: #00ff7f')
        self.khakiCheck.setStyleSheet('color: #f0e68c')
        colorsLabel = QLabel("Chose minimum 3 colors:")
        grid.addWidget(colorsLabel,0,1,1,4)
        
        grid.addWidget(self.createExampleGroup(1),1,0)
        grid.addWidget(self.createExampleGroup(2),1,1)
        grid.addWidget(self.createExampleGroup(3),1,2)
        grid.addWidget(self.createExampleGroup(4),1,3)
        grid.addWidget(self.createExampleGroup(5),2,0,1,3)
        grid.addWidget(self.createExampleGroup(6),3,0,1,3)
        grid.addWidget(self.createExampleGroup(7),2,3,2,1)
        self.setLayout(grid)
        
        self.setWindowTitle("Random Mondrian art")        
        self.resize(490,300)
        
        
       
        
        ###
        self.whiteCheck.stateChanged.connect(lambda: self.color_list(self.whiteCheck))
        self.aquaCheck.stateChanged.connect(lambda:self.color_list(self.aquaCheck))
        self.indigoCheck.stateChanged.connect(lambda:self.color_list(self.indigoCheck))
        self.turquoiseCheck.stateChanged.connect(lambda:self.color_list(self.turquoiseCheck))
        self.limeCheck.stateChanged.connect(lambda:self.color_list(self.limeCheck))
        self.blackCheck.stateChanged.connect(lambda:self.color_list(self.blackCheck))
        self.blueCheck.stateChanged.connect(lambda:self.color_list(self.blueCheck))
        self.seashellCheck.stateChanged.connect(lambda:self.color_list(self.seashellCheck))
        self.navyCheck.stateChanged.connect(lambda:self.color_list(self.navyCheck))
        self.coralCheck.stateChanged.connect(lambda:self.color_list(self.coralCheck))
        self.redCheck.stateChanged.connect(lambda:self.color_list(self.redCheck))
        self.fuchsiaCheck.stateChanged.connect(lambda:self.color_list(self.fuchsiaCheck))
        self.honeydewCheck.stateChanged.connect(lambda:self.color_list(self.honeydewCheck))
        self.hotpinkCheck.stateChanged.connect(lambda:self.color_list(self.hotpinkCheck))
        self.skyblueCheck.stateChanged.connect(lambda:self.color_list(self.skyblueCheck))
        self.yellowCheck.stateChanged.connect(lambda:self.color_list(self.yellowCheck))
        self.purpleCheck.stateChanged.connect(lambda:self.color_list(self.purpleCheck))
        self.siennaCheck.stateChanged.connect(lambda:self.color_list(self.siennaCheck))
        self.springgreenCheck.stateChanged.connect(lambda:self.color_list(self.springgreenCheck))
        self.khakiCheck.stateChanged.connect(lambda:self.color_list(self.khakiCheck))
        ### kick uki

    def createExampleGroup(self,ind):
        
        
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        groupBox= QGroupBox()
        label=QLabel(self)
    
        if ind==1:
            vbox.addWidget(self.whiteCheck)
            vbox.addWidget(self.aquaCheck)
            vbox.addWidget(self.indigoCheck)
            vbox.addWidget(self.turquoiseCheck)
            vbox.addWidget(self.limeCheck)
              
        elif ind==2:
            vbox.addWidget(self.blackCheck)
            vbox.addWidget(self.blueCheck)
            vbox.addWidget(self.seashellCheck)
            vbox.addWidget(self.navyCheck)
            vbox.addWidget(self.coralCheck)
           
        elif ind ==3:
            vbox.addWidget(self.redCheck)
            vbox.addWidget(self.fuchsiaCheck)
            vbox.addWidget(self.honeydewCheck)
            vbox.addWidget(self.hotpinkCheck)
            vbox.addWidget(self.skyblueCheck)
            
        elif ind ==4:
            vbox.addWidget(self.yellowCheck)
            vbox.addWidget(self.purpleCheck)
            vbox.addWidget(self.siennaCheck)
            vbox.addWidget(self.springgreenCheck)
            vbox.addWidget(self.khakiCheck)
        
        elif ind==5:
            edit = QLineEdit(self)
            label.setText('Width:')
            hbox.addWidget(label)
            hbox.addWidget(edit)
            
        elif ind==6:
            edit = QLineEdit(self)
            label.setText('Height:')
            hbox.addWidget(label)
            hbox.addWidget(edit)
           
        elif ind==7:
            button1 = QPushButton(self)
            button1.setText("Generate")
            rButton = QRadioButton(self)
            rButton.setText("Pattern Fill")
            vbox.addWidget(rButton)
            vbox.addWidget(button1)
        
        if not (ind ==5 or ind==6):
            groupBox.setLayout(vbox)
        else: 
            groupBox.setLayout(hbox)  
                        
        return groupBox

    def color_list(self,state):
        if self.whiteCheck.isChecked():
            self.color.append('#ffffff')
            print(self.color)
        if self.blackCheck.isChecked():
            self.color.append('#000000')
        if self.redCheck.isChecked():
            self.color.append('#ff0000') 
        if self.yellowCheck.isChecked():
            self.color.append('#ffff00')
        if self.aquaCheck.isChecked():
            self.color.append('#00ffff')
        if self.blueCheck.isChecked():
            self.color.append('#0000ff')
        if self.fuchsiaCheck.isChecked():
            self.color.append('#ff00ff')
        if self.purpleCheck.isChecked():
            self.color.append('#800080')
        if self.indigoCheck.isChecked():
            self.color.append('#4b0082')
        if self.seashellCheck.isChecked():
            self.color.append('#fff5ee')
        if self.honeydewCheck.isChecked():
            self.color.append('#f0fff0')
        if self.siennaCheck.isChecked(): 
            self.color.append('#a0522d')
        if self.turquoiseCheck.isChecked():
            self.color.append('#40e0d0')
        if self.navyCheck.isChecked():
            self.color.append('#000080')
        if self.hotpinkCheck.isChecked():
            self.color.append('#ff69b4')
        if self.springgreenCheck.isChecked():
            self.color.append('#00ff7f')
        if self.limeCheck.isChecked():
            self.color.append('#00ff00')
        if self.coralCheck.isChecked():
            self.color.append('#ff7f50')
        if self.skyblueCheck.isChecked():
            self.color.append('#87ceeb')
        if self.khakiCheck.isChecked(): 
            self.color.append('#f0e68c')

if __name__== '__main__':
    app=QApplication([])
    window=Window()
    app.exec_()
