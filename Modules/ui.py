import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QInputDialog, QLineEdit
from PyQt6.QtGui import QKeySequence
from PyQt6.QtCore import Qt
import Modules.tasks as tasks

def openui():
    #setting up pyqt
    app = QApplication(sys.argv)
    window = QWidget()

    window.setWindowTitle("Reminder")
    window.setGeometry(100, 50, 300, 600)

    #title text
    title = QLabel("Reminder", parent=window)
    title.move(60, 10)

    #title text font
    titlefont = title.font()
    
    titlefont.setBold(True)
    titlefont.setPointSize(30)
    titlefont.setFamily("Cascadia Code")

    title.setFont(titlefont)

    return window, app

def setupinput(window):
    input = QLineEdit(parent=window)
    input.move(25, 550)
    input.setFixedSize(250, 40)

    # font slop
    font = input.font()
    font.setPointSize(18)
    font.setFamily("Cascadia Code")

    input.setFont(font)

    return input
    
def setuptasks(window):
    labels = []
    buttons = []

    for i in range(11):
        label = QLabel(parent=window)
        button = QPushButton(parent=window)
    
        #moving
        label.move(100, 60 + (i * 40))
        button.move(40, 60 + (i * 40))

        # font
        font = label.font()
        font.setPointSize(14)
        font.setFamily("Cascadia Code")
        label.setFont(font)

        #adding to table
        labels.insert(len(labels), label)
        buttons.insert(len(buttons), button)
        
        #adding button functionality
        button.clicked.connect(lambda _, idx=i: tasks.removetask(window, idx))

    return buttons, labels 
