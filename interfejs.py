from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from PySide6.QtGui import QPixmap
import string
import random

def paswordd(lenght, with_numbers, with_special):
    
    if with_numbers.lower() == "t":
        with_numbers = True
    else:
        with_numbers = False
    
    if with_special.lower() == "t":
        with_special = True
    else:
        with_special = False

    lenght = int(lenght)
    characters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation

    password = ''
    meets_expectations = False
    has_number = False
    has_special = False

    if with_numbers:
        characters = characters + numbers
    if with_special:
        characters = characters + special

    while not meets_expectations or len(password) < lenght:
        new_char = random.choice(characters)
        password = password + new_char
        
        if new_char in numbers:
            has_number = True
        elif new_char in special:
            has_special = True
            
        if with_numbers and with_special:
            meets_expectations = has_number and has_special
        elif with_numbers and not with_special:
            meets_expectations = has_number
        elif not with_numbers and with_special:
            meets_expectations = has_special
        else:
            meets_expectations = True

    return password 

class GeneratorHasel(QWidget):
    def __init__(self):
        super().__init__()
        
        self.lenght_line_edit = None
        self.with_numbers_line_edit = None
        self.with_special_line_edit = None
        
        self.setup()
    
    def setup(self): #do interfejsu
        
        pix_label = QLabel(self)
        pixmap = QPixmap("C:\\Users\\48602\\Desktop\\pierdoly\\f2d5976372_bezpieczny_internet.png").scaled(250,150)
        pix_label.setPixmap(pixmap)
        pix_label.move(125, 30)
        
        self.lenght_line_edit = QLineEdit("minimalna dlugosc hasla", self)
        self.lenght_line_edit.setFixedWidth(200)
        self.lenght_line_edit.move(150, 200)
        
        self.with_numbers_line_edit = QLineEdit("czy chcesz liczby t/n", self)
        self.with_numbers_line_edit.setFixedWidth(200)
        self.with_numbers_line_edit.move(150, 220)
        
        self.with_special_line_edit = QLineEdit("czy chcesz znaki specialne t/n", self)
        self.with_special_line_edit.setFixedWidth(200)
        self.with_special_line_edit.move(150, 240)
        
        submit_btn = QPushButton("Submit", self)
        submit_btn.move((500 - submit_btn.size().width()) / 2, 350)
        submit_btn.clicked.connect(self.submit) #submit bez nawiasu bo z nawiasami wykona sie od razu, bez submitu
        
        quit_btn = QPushButton("Quit", self)
        quit_btn.move(420, 370)
        quit_btn.clicked.connect(QApplication.instance().quit)#wywolanie zamkniecia, korzystajace z eventu
        
        self.setFixedSize(500, 400)
        self.setWindowTitle("generator hasel")
        
        self.show()
        
    def submit(self):
        generated_password = paswordd(self.lenght_line_edit.text(), self.with_numbers_line_edit.text(), self.with_special_line_edit.text())
        password_box = QMessageBox()
        password_box.setText("Twoje haselko to: " + generated_password)
        password_box.exec()

if __name__ == "__main__":
    app = QApplication([])
    
    generator = GeneratorHasel()
    
    app.exec()