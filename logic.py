from typing import Union, Any

from PyQt6.QtWidgets import *
from gui import *
import random


def add(values) -> int:
    """This just adds all positive numbers.
    If there is a negative number, it will ignore it and continue.
    It then returns the total sum of the numbers."""
    num_sum = 0
    num_list = []
    for x in values:
        num_list.append(int(x))
    for num in num_list:
        if num > 0:
            num_sum += num
    return num_sum


def subtract(values) -> int:
    """This only subtracts negative numbers from each other.
    If there is a positive number, it ignores the input and moves on to the next.
    It then returns the total difference"""
    num_sum = 0
    num_list = []
    for x in values:
        num_list.append(int(x))
    for num in num_list:
        if num < 0:
            num_sum += num
    return num_sum


def multiply(values) -> int:
    """This multiplies all the numbers in the input to become a single product"""
    product = 1
    num_list = []
    for x in values:
        num_list.append(int(x))
    for num in num_list:
        if num != 0:
            product *= num
        else:
            product = 0
    return product


def divide(values) -> Union[Union[str, int, float], Any]:
    """This divides the first number by the proceeding numbers in the input
    If the list contains a zero at all, it will return that you cannot divide by zero"""
    num_list = []
    for x in values:
        num_list.append(int(x))
    if num_list[0] == 0:
        quotient = 0
    else:
        quotient = num_list[0]
        del num_list[0]
    for num in num_list:
        if num != 0:
            quotient = quotient / num
        else:
            return 'Cannot divide by zero'
    return quotient


def choose(values) -> int:
    """This chooses a number at random from the list created in the input box"""
    num_list = []
    for x in values:
        num_list.append(int(x))
    random_index = random.randint(0, len(num_list) - 1)
    random_num = num_list[random_index]
    return random_num


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """All this code does is initialize the class for the logic to use the PyQT window that I
        created using PyQT Designer. It also fixes the size so that it is non-adjustable"""
        super().__init__()
        self.setupUi(self)
        self.clearButton.clicked.connect(self.clear_input)
        self.submitButton.clicked.connect(self.submit_button)
        self.setFixedSize(800, 600)

    def clear_input(self) -> None:
        """This just clears the output text box and input text box,
         there isn't anything else that needs to be cleared between uses"""
        self.errorLabelOutput.setText('')
        self.lineEdit.clear()
        return

    def submit_button(self) -> None:
        """This is where the fun happens: it checks to find which radiobutton
        is checked and then computes based on the list created from the input box"""
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
            """This only triggers if you input something that is not an integer"""
            self.errorLabelOutput.setText(f'Your input should contain only numbers separated by spaces')

    def setWindowTitle(self, param):
        pass

