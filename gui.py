import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

colors = []

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Random Mondrian Art'
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(490,380)
        grid = QGridLayout()
        self.setLayout(grid)
        
        colorsLabel = QLabel("Chose minimum 3 colors:")
        grid.addWidget(colorsLabel,1,0, 3,1)

        ### first row of color checkbox
        
        # WHITE:
        whiteCheck = QCheckBox('WHITE')
        whiteCheck.setStyleSheet('color: #ffffff' )
        #whiteCheck.stateChange.connect(color_list)
        
        # BLACK:
        blackCheck = QCheckBox('BLACK')
        blackCheck.setStyleSheet('color: #000000' )
        #blackCheck.stateChange.connect(color_list)
        
        # RED:
        redCheck = QCheckBox('RED')
        redCheck.setStyleSheet('color: #ff0000' )
        #redCheck.stateChange.connect(color_list)

        # YELLOW:
        yellowCheck = QCheckBox('YELLOW')
        yellowCheck.setStyleSheet('color: #ffff00' )
        #yellowCheck.stateChange.connect(color_list)
        
        grid.addWidget(whiteCheck,2,0)
        grid.addWidget(blackCheck,2,1)
        grid.addWidget(redCheck,2,2)
        grid.addWidget(yellowCheck,2,3)
        

        ### second row of color checkboxes

        # AQUA:
        aquaCheck = QCheckBox("AQUA")
        aquaCheck.setStyleSheet('color: #00ffff' )
        #aquaCheck.stateChange.connect(color_list)
        
        # BLUE:
        blueCheck = QCheckBox("BLUE")
        blueCheck.setStyleSheet('color: #0000ff' )
        #blueCheck.stateChange.connect(color_list)

        # FUCHSIA:
        fuchsiaCheck = QCheckBox("FUCHSIA")
        fuchsiaCheck.setStyleSheet('color: #ff00ff' )
        #fuchsiaCheck.stateChange.connect(color_list)

        # PURPLE:
        purpleCheck = QCheckBox("PURPLE")
        purpleCheck.setStyleSheet('color: #800080' )
        #purpleCheck.stateChange.connect(color_list)

        grid.addWidget(aquaCheck,3,0)
        grid.addWidget(blueCheck,3,1)
        grid.addWidget(fuchsiaCheck,3,2)
        grid.addWidget(purpleCheck,3,3)

        ### third row of color checkboxes

        # INDIGO:
        indigoCheck = QCheckBox("INDIGO")
        indigoCheck.setStyleSheet('color: #4b0082' )
        #indigoCheck.stateChange.connect(color_list)
        
        # SEASHELL:
        seashellCheck = QCheckBox("SEASHELL")
        seashellCheck.setStyleSheet('color: #fff5ee' )
        #seashellCheck.stateChange.connect(color_list)
        
        # HONEYDEW:
        honeydewCheck = QCheckBox("HONEYDEW")
        honeydewCheck.setStyleSheet('color: #f0fff0' )
        #honeydewCheck.stateChange.connect(color_list)

        # SIENNA:
        siennaCheck = QCheckBox("SIENNA")
        siennaCheck.setStyleSheet('color: #a0522d' )
        #siennaCheck.stateChange.connect(color_list)
        
        grid.addWidget(indigoCheck,4,0)
        grid.addWidget(seashellCheck,4,1)
        grid.addWidget(honeydewCheck,4,2)
        #grid.addWidget(siennaCheck,4,3)

        ### fourth row of color checkboxes

        # TURQUOISE:
        turqouiseCheck = QCheckBox("TURQUOISE")
        turqouiseCheck.setStyleSheet('color: #40e0d0' )
        #turqouiseCheck.stateChange.connect(color_list)

        # NAVY:
        navyCheck = QCheckBox("NAVY")
        navyCheck.setStyleSheet('color: #000080' )
        #navyCheck.stateChange.connect(color_list)

        # HOTPINK:
        hotpinkCheck = QCheckBox("HOTPINK")
        hotpinkCheck.setStyleSheet('color: #ff69b4' )
        #hotpinkCheck.stateChange.connect(color_list)

        # SPRINGGREEN:
        springgreenCheck = QCheckBox("SPRINGGREEN")
        springgreenCheck.setStyleSheet('color: #00ff7f' )
        #springgreenCheck.stateChange.connect(color_list)

        grid.addWidget(turqouiseCheck,5,0)
        grid.addWidget(navyCheck,5,1)
        grid.addWidget(hotpinkCheck,5,2)
        grid.addWidget(springgreenCheck,5,3)
        
        ### fifth row of color checkboxes

        # LIME:
        limeCheck = QCheckBox("LIME")
        limeCheck.setStyleSheet('color: #00ff00' )
        #limeCheck.stateChange.connect(color_list)

        # CORAL:
        coralCheck = QCheckBox("CORAL")
        coralCheck.setStyleSheet('color: #ff7f50' )
        #coralCheck.stateChange.connect(color_list)

        # SKYBLUE:
        skyblueCheck = QCheckBox("SKYBLUE")
        skyblueCheck.setStyleSheet('color: #87ceeb' )
        #skyblueCheck.stateChange.connect(color_list)


        # KHAKI:
        khakiCheck = QCheckBox("KHAKI")
        khakiCheck.setStyleSheet('color: #f0e68c' )
        #khakiCheck.stateChange.connect(color_list)

        
        grid.addWidget(limeCheck,6,0)
        grid.addWidget(coralCheck,6,1)
        grid.addWidget(skyblueCheck,6,2)
        grid.addWidget(khakiCheck,6,3)
        
        # WIDTH:
        width = QLabel("Width :")
        edit1 = QLineEdit(self)
        grid.addWidget(width,7,0)
        grid.addWidget(edit1,7,1,1,2)

        # HEIGHT:
        height = QLabel("Height :")
        edit2 = QLineEdit(self)
        grid.addWidget(height,8,0)
        grid.addWidget(edit2,8,1,1,2)
    
        #if width and height left empty screen resolution will be used

        # BUTTON:
        button1 = QPushButton(self)
        button1.setText("Generate")
        grid.addWidget(button1,8,3)
        
        # PATTERN FILL:
        rButton = QRadioButton(self)
        rButton.setText("Pattern Fill")
        grid.addWidget(rButton,7,3)


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


        self.show()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = App()
    app.exec_()
