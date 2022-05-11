import csv
import random
from tkinter import *

class GUI:



    def __init__(self, window):
        """
        - This sets up the labels and buttons in the window
        - Whle some labels are made here they will not appear until the button is prushed.
        """
        self.window = window

        self.l1 = Label(text='', font=('times', 150))
        self.roll_label=Label(text='', font=('times',20))
        self.add_label = Label(text='', font=('times', 20))
        self.sub_label = Label(text='', font=('times', 20))
        self.mul_label = Label(text='', font=('times', 20))
        self.div_label = Label(text='', font=('times', 20))


        self.label_mes = Label(text='Lets roll some dice and do some math press the button!!!', font=('times', 20))
        self.label_mes.pack()

        self.frame_b1 = Frame(self.window)
        self.b1 = Button(text="lets roll...", command=self.roll, height=2, width=8)
        self.b1.place(x=320, y=40)
        self.frame_b1.pack()

    def roll(self):
        """
        _ When the "lets roll button is pressed it will display 2 dice with numbers
        _ a text message will appear to tell which numbers you rolled
        _ then it will take those 2 numbers and do some math
        _ the math that it does is Addition Subtraction, multiple, and division.
        """
        self.number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.x = {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683': 4, '\u2684': 5, '\u2685': 6}
        self.dice1=random.choice(self.number)
        self.dice2=random.choice(self.number)
        self.l1.config(text=f'{self.dice1} {self.dice2}')
        self.l1.pack()
        self.roll_label.config(text=f'You rolled a {self.x[self.dice1]} and a {self.x[self.dice2]}')
        self.roll_label.pack()
        self.add_label.config(text=f'Addition: {self.x[self.dice1]} + {self.x[self.dice2]} = {self.x[self.dice1] + self.x[self.dice2]}')
        self.add_label.pack()
        self.sub_label.config(text=f'Subtraction: {self.x[self.dice1]} - {self.x[self.dice2]} = {self.x[self.dice1] - self.x[self.dice2]}')
        self.sub_label.pack()
        self.mul_label.config(text=f'Multiplication: {self.x[self.dice1]} x {self.x[self.dice2]} = {self.x[self.dice1] * self.x[self.dice2]}')
        self.mul_label.pack()
        self.div_label.config(text=f'Division {self.x[self.dice1]}/{self.x[self.dice2]} = {self.x[self.dice1] / self.x[self.dice2]}')
        self.div_label.pack()






