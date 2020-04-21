import sys
#from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
 #       QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self,parent=None):
        super(Window,self).__init__(parent)
        self.initUI()
        self.show()
    
    def initUI(self):    
        grid=QGridLayout()
        
        colorsLabel = QLabel("Chose minimum 3 colors:")
        grid.addWidget(colorsLabel,0,0)
        
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

    def createExampleGroup(self,ind):
        ####################################################
        whiteCheck=QCheckBox('WHITE')
        whiteCheck.setStyleSheet('color: #ffffff')
        
        aquaCheck = QCheckBox("AQUA")
        aquaCheck.setStyleSheet('color: #00ffff')
        
        indigoCheck = QCheckBox("INDIGO")
        indigoCheck.setStyleSheet('color: #4b0082')
        
        turqouiseCheck = QCheckBox("TURQUOISE")
        turqouiseCheck.setStyleSheet('color: #40e0d0')
        
        limeCheck = QCheckBox("LIME")
        limeCheck.setStyleSheet('color: #00ff00')
        
        blackCheck = QCheckBox('BLACK')
        blackCheck.setStyleSheet('color: #000000')
        
        blueCheck = QCheckBox("BLUE")
        blueCheck.setStyleSheet('color: #0000ff')
        
        seashellCheck = QCheckBox("SEASHELL")
        seashellCheck.setStyleSheet('color: #fff5ee')
        
        navyCheck = QCheckBox("NAVY")
        navyCheck.setStyleSheet('color: #000080')
        
        coralCheck = QCheckBox("CORAL")
        coralCheck.setStyleSheet('color: #ff7f50' )
        
        redCheck = QCheckBox('RED')
        redCheck.setStyleSheet('color: #ff0000' )
        
        fuchsiaCheck = QCheckBox("FUCHSIA")
        fuchsiaCheck.setStyleSheet('color: #ff00ff' )
 
        honeydewCheck = QCheckBox("HONEYDEW")
        honeydewCheck.setStyleSheet('color: #f0fff0' )

        hotpinkCheck = QCheckBox("HOTPINK")
        hotpinkCheck.setStyleSheet('color: #ff69b4' )
        
        skyblueCheck = QCheckBox("SKYBLUE")
        skyblueCheck.setStyleSheet('color: #87ceeb' )
        
        yellowCheck = QCheckBox('YELLOW')
        yellowCheck.setStyleSheet('color: #ffff00')
        
        purpleCheck = QCheckBox("PURPLE")
        purpleCheck.setStyleSheet('color: #800080')
        
        siennaCheck = QCheckBox("SIENNA")
        siennaCheck.setStyleSheet('color: #a0522d')
        
        springgreenCheck = QCheckBox("SPRINGGREEN")
        springgreenCheck.setStyleSheet('color: #00ff7f')
        
        khakiCheck = QCheckBox("KHAKI")
        khakiCheck.setStyleSheet('color: #f0e68c')
        ####################################################
        
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        groupBox= QGroupBox()
        label=QLabel(self)
    
        if ind==1:
            vbox.addWidget(whiteCheck)
            vbox.addWidget(aquaCheck)
            vbox.addWidget(indigoCheck)
            vbox.addWidget(turqouiseCheck)
            vbox.addWidget(limeCheck)
              
        elif ind==2:
            vbox.addWidget(blackCheck)
            vbox.addWidget(blueCheck)
            vbox.addWidget(seashellCheck)
            vbox.addWidget(navyCheck)
            vbox.addWidget(coralCheck)
           
        elif ind ==3:
            vbox.addWidget(redCheck)
            vbox.addWidget(fuchsiaCheck)
            vbox.addWidget(honeydewCheck)
            vbox.addWidget(hotpinkCheck)
            vbox.addWidget(skyblueCheck)
            
        elif ind ==4:
            vbox.addWidget(yellowCheck)
            vbox.addWidget(purpleCheck)
            vbox.addWidget(siennaCheck)
            vbox.addWidget(springgreenCheck)
            vbox.addWidget(khakiCheck)
        
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

    def color_list(state):
        if whiteCheck.isChecked():
            color.append('#ffffff')
        if blackCheck.isChecked():
            color.append('#000000')
        if redCheck.isChecked():
            color.append('#ff0000') 
        if yellowCheck.isChecked():
            color.append('#ffff00')
        if aquaCheck.isChecked():
            color.append('#00ffff')
        if blueCheck.isChecked():
            color.append('#0000ff')
        if fuchsiaCheck.isChecked():
            color.append('#ff00ff')
        if purpleCheck.isChecked():
            color.append('#800080')
        if indigoCheck.isChecked():
            color.append('#4b0082')
        if seashellCheck.isChecked():
            color.append('#fff5ee')
        if honeydewCheck.isChecked():
            color.append('#f0fff0')
        if siennaCheck.isChecked(): 
            color.append('#a0522d')
        if turquoiseCheck.isChecked():
            color.append('#40e0d0')
        if navyCheck.isChecked():
            color.append('#000080')
        if hotpinkCheck.isChecked():
            color.append('#ff69b4')
        if springgreenCheck.isChecked():
            color.append('#00ff7f')
        if limeCheck.isChecked():
            color.append('#00ff00')
        if coralCheck.isChecked():
            color.append('#ff7f50')
        if skyblueCheck.isChecked():
            color.append('#87ceeb')
        if khakiCheck.isChecked(): 
            color.append('#f0e68c')

if __name__== '__main__':
    app=QApplication([])
    window=Window()
    app.exec_()