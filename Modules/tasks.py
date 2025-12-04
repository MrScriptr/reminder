import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QInputDialog, QLineEdit
from PyQt6.QtGui import QKeySequence
from PyQt6.QtCore import Qt

tasks = []
labels = []
buttons = []

def updategui(window):
    for i in range(len(labels)):
        label = labels[i]
        task = ""
        
        if i > len(tasks) - 1:
            task = ""
        else:
            task = str(tasks[i])

        label.setText(task)
        label.adjustSize()

def removetask(window, buttonnum):
    num = (len(buttons) - 1) - buttonnum
    print(buttonnum)
    if buttonnum <= len(tasks) - 1:
       tasks.pop(buttonnum)
    updategui(window)

def addtask(window, input):
    text = input.text()
    input.setText("")
    
    if text != "":
        tasks.insert(0, text)
        updategui(window)

