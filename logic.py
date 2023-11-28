from PyQt6.QtWidgets import *
from gui import *
import random


def add(values):
    num_sum = 0
    list = []
    for x in values:
        list.append(int(x))
    for num in list:
        if num > 0:
            num_sum += num
    return num_sum


def subtract(values):
    num_sum = 0
    list = []
    for x in values:
        list.append(int(x))
    for num in list:
        if num < 0:
            num_sum += num
    return num_sum


def multiply(values):
    product = 1
    list = []
    for x in values:
        list.append(int(x))
    for num in list:
        if num != 0:
            product *= num
        else:
            product = 0
    return product


def divide(values):
    list = []
    for x in values:
        list.append(int(x))
    if list[0] == 0:
        quotient = 0
    else:
        quotient = list[0]
        del list[0]
    for num in list:
        if num == 0:
            sys.exit('Cannot divide by 0')
        else:
            quotient = quotient / num
    return quotient


def choose(values):
    list = []
    for x in values:
        list.append(int(x))
    random_index = random.randint(0, len(list) - 1)
    random_num = list[random_index]
    return random_num


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clearButton.clicked.connect(self.clear_input)
        self.submitButton.clicked.connect(self.submit_button)
        self.setFixedSize(800, 600)
        self.inputList = []

    def clear_input(self):
        self.errorLabelOutput.setText('')
        self.lineEdit.clear()
        return

    def submit_button(self):
        try:
            userInput = self.lineEdit.text().strip().split()
            if self.addRadio.isChecked():
                output = add(userInput)
                self.errorLabelOutput.setText(f'The sum of those numbers is: {output}')
            elif self.subtractRadio.isChecked():
                output = subtract(userInput)
                self.errorLabelOutput.setText(f'The difference of those numbers is: {output}')
            elif self.multiplyRadio.isChecked():
                output = multiply(userInput)
                self.errorLabelOutput.setText(f'The product of those numbers is: {output}')
            elif self.divideRadio.isChecked():
                output = divide(userInput)
                self.errorLabelOutput.setText(f'The quotient of those answers is: {output}')
            elif self.chooseRadio.isChecked():
                output = choose(userInput)
                self.errorLabelOutput.setText(f'Your random number is: {output}')
            else:
                self.errorLabelOutput.setText(f'You need to select a operator')
        except ValueError:
            self.errorLabelOutput.setText(f'Your input should contain only numbers separated by spaces')

