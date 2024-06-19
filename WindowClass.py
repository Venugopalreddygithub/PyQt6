from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import sys
from PyQt6.QtGui import QIcon 


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Tutorials") # Adding the title Name
        self.setWindowIcon(QIcon("logo.png")) # Adding the logo 
        
        # self.setFixedHeight(300)
        # self.setFixedWidth(300)
        
        # self.setGeometry(300, 400, 300, 300)
        
        self.setStyleSheet("background-color: green") #Adding the background-color to the window 
        

app = QApplication([])

window = Window()
window.show()

sys.exit(app.exec())