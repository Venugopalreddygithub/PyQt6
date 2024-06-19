from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import sys
from PyQt6.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Button & Label") # Adding the title Name
        self.setWindowIcon(QIcon("logo.png")) # Adding the logo 
        
        # self.setFixedHeight(300)
        # self.setFixedWidth(300)
        
        # self.setGeometry(300, 400, 300, 300)
        
        # self.setStyleSheet("background-color: green") #Adding the background-color to the window 
        
        self.create_qwidgets()
    
    def create_qwidgets(self):
        btn = QPushButton("Click Me", self)
        # btn.move(100, 200)
        btn.setGeometry(100, 100, 100, 100)
        btn.setStyleSheet("background-color: green; color: white")
        
        label = QLabel("My Label", self)
        label.move(100,200)
        label.setStyleSheet("color: red")
        label.setFont(QFont("Times New Roman", 15))
        

app = QApplication([])

window = Window()
window.show()

sys.exit(app.exec())