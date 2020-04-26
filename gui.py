import sys
import os
from mondrian import make_art
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from tkinter import Tk
from PyQt5.QtSvg import *

class Window2(QWidget):
    
    def __init__(self,parent=None):
        super().__init__()
        color = QColor(128,128,128)
        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)
        self.svg = QSvgWidget()
        self.backbutton = QPushButton()
        self.saveButton = QPushButton()
        self.saveName = QLineEdit()
        self.label = QLabel("Unesite ime fajla u kom zelite da sacuvate sliku:")
        self.initUI()
       
    def initUI(self):
        self.setMaximumWidth(600)
        self.setMaximumHeight(600)
        self.setMinimumSize(300, 300)
        self.setWindowTitle("Preview")
        
        grid=QGridLayout()
        self.setLayout(grid)
        
        self.backbutton.setText("Back")
        self.backbutton.clicked.connect(lambda: self.b(self.backbutton))
        
        self.saveButton.setText("Save")
        self.saveButton.clicked.connect(lambda: self.savePush(self.saveButton))
        if rb_ind == False:
            grid.addWidget(self.svg,1,0,5,5)
        
            self.svg.load("art.svg")
        
            grid.addWidget(self.backbutton,7,4)
            
        
            grid.addWidget(self.saveName,7,0,1,3)
            grid.addWidget(self.saveButton,7,3,1,1)
            
    
        
            grid.addWidget(self.label,6,0,1,5)
        else:
            grid.addWidget(self.backbutton,2,4)
            grid.addWidget(self.saveName,2,0,1,3)
            grid.addWidget(self.saveButton,2,3,1,1)
            
    
        
            grid.addWidget(self.label,1,0,1,5)
            
        self.show()
    def savePush(self,state):
        if self.saveName.text() == "":
            QMessageBox.about(self,"Greska","Unesite ime fajla gde zelite da sacuvate sliku")
        else:
            ime = self.saveName.text()
            ime += ".svg"
            errind = 0
            if os.path.exists(ime):
                os.remove(ime)
            try:
                os.rename("art.svg",ime)
            except OSError:
                errind = 1   
           
            if errind == 1:
                QMessageBox.about(self,"Greska","Greska prilikom cuvanja. Pokusajte ponov.")
            else:
                QMessageBox.about(self,"Uspeh","Uspesno sacuvan")
                    
           
            

        
            
                
            
    def b(self,state):
        self.close()
        self.next = Window()

class Window(QWidget):
    
    def __init__(self,parent=None):
        super().__init__()
        color = QColor(128,128,128)
        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)
        self.edit1 = QLineEdit(self)
        self.edit2 = QLineEdit(self)
        self.button1 = QPushButton(self)
        self.seagreenCheck=QCheckBox("SEAGREEN")
        self.aquaCheck= QCheckBox("AQUA")
        self.indigoCheck = QCheckBox("INDIGO")
        self.turquoiseCheck = QCheckBox("TURQUOISE")
        self.limeCheck = QCheckBox("LIME")
        self.aquamarineCheck = QCheckBox("AQUAMARINE")
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
        self.rButton = QRadioButton(self)
        self.color = []
        self.initUI()
        self.show()
    
    def initUI(self):  
        self.setMaximumWidth(600)
        self.setMaximumHeight(600)
        self.setMinimumSize(300, 300)
        grid=QGridLayout()
        self.seagreenCheck.setStyleSheet('color: #2E8B57')
        self.aquaCheck.setStyleSheet('color: #00ffff')
        self.indigoCheck.setStyleSheet('color: #4b0082')
        self.turquoiseCheck.setStyleSheet('color: #40e0d0')
        self.limeCheck.setStyleSheet('color: #00ff00')
        self.aquamarineCheck.setStyleSheet('color: #7FFFD4')
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
        

    def createExampleGroup(self,ind):
        
        
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        groupBox= QGroupBox()
        label=QLabel(self)
    
        if ind==1:
            vbox.addWidget(self.seagreenCheck)
            vbox.addWidget(self.aquaCheck)
            vbox.addWidget(self.indigoCheck)
            vbox.addWidget(self.turquoiseCheck)
            vbox.addWidget(self.limeCheck)
              
        elif ind==2:
            vbox.addWidget(self.aquamarineCheck)
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
            
            label.setText('Width:')
            hbox.addWidget(label)
            hbox.addWidget(self.edit1)
            
        elif ind==6:
            
            label.setText('Height:')
            hbox.addWidget(label)
            hbox.addWidget(self.edit2)
           
        elif ind==7:
            self.button1.setText("Generate")
            self.button1.clicked.connect(lambda: self.color_list(self.button1))
           
            self.rButton.setText("Pattern Fill")
            
            
            vbox.addWidget(self.rButton)
            vbox.addWidget(self.button1)
        
        if not (ind ==5 or ind==6):
            groupBox.setLayout(vbox)
        else: 
            groupBox.setLayout(hbox)  
                        
        return groupBox

    def color_list(self,state):
        global rb_ind
        rb_ind = False
        self.color = []
        if self.seagreenCheck.isChecked():
            self.color.append('#2E8B57')
        if self.aquamarineCheck.isChecked():
            self.color.append('#7FFFD4')
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
        if len(self.color) > 2:
            if self.rButton.isChecked():
                rb_ind=True
            if self.edit1.text()  == "" or self.edit2.text() == "":
                root = Tk()
                w = root.winfo_screenwidth()
                h = root.winfo_screenheight()
                make_art(w,h,self.color, rb_ind)
                
                
            else: 
                print("Wat")
                make_art(float(self.edit1.text()),float(self.edit2.text()),self.color,rb_ind)  
            
            
            self.close()
            self.next = Window2()
        else:
            QMessageBox.about(self,"Greska","Morate oznaciti bar 3 boje")
        

if __name__ == "__main__":
    app=QApplication([])
    window=Window()
    app.exec_()
