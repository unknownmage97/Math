from tkinter import *
from logic import Operations

class Gui:
    def __init__(self, window):
        self.window = window

        # Radio buttons
        self.frame_shape = Frame(self.window)
        self.label_operation = Label(self.frame_shape, text='Shape\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_add = Radiobutton(self.frame_shape, text='Add', variable=self.radio_1, value=1, command=self.formulas)
        self.radio_subtract = Radiobutton(self.frame_shape, text='Subtract', variable=self.radio_1, value=2, command=self.formulas)
        self.radio_multiply = Radiobutton(self.frame_shape, text='Multiply', variable=self.radio_1, value=3, command=self.formulas)
        self.radio_divide = Radiobutton(self.frame_shape, text='Divide', variable=self.radio_1, value=4, command=self.formulas)
        self.radio_triangular = Radiobutton(self.frame_shape, text='Triangular', variable=self.radio_1, value=5, command=self.formulas)
        self.radio_factorial = Radiobutton(self.frame_shape, text='Factorial', variable=self.radio_1, value=6, command=self.formulas)
        self.label_operation.pack(side='left', padx=5)
        self.radio_add.pack(side='left')
        self.radio_subtract.pack(side='left')
        self.radio_multiply.pack(side='left')
        self.radio_divide.pack(side='left')
        self.radio_triangular.pack(side='left')
        self.radio_factorial.pack(side='left')
        self.frame_shape.pack(anchor='w', pady=10)

        # First number
        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first)
        self.entry_first = Entry(self.frame_first, width=40)
        self.label_first.pack(padx=20, side='left')
        self.entry_first.pack(padx=20, side='left')
        self.frame_first.pack(anchor='w', pady=10)
        self.entry_first.pack_forget()

        # Second number
        self.frame_second = Frame(self.window)
        self.label_second = Label(self.frame_second)
        self.entry_second = Entry(self.frame_second, width=40)
        self.label_second.pack(padx=20, side='left')
        self.entry_second.pack(padx=20, side='left')
        self.frame_second.pack(anchor='w', pady=10)
        self.entry_second.pack_forget()

        # Results label
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        # Submit and Clear buttons
        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='Submit', command=self.compute)
        self.button_clear = Button(self.frame_button, text='Clear', command = self.clear)
        self.button_compute.pack(padx=50,side='left')
        self.button_clear.pack(padx=50, side='right')
        self.frame_button.pack()

    def formulas(self):
        self.entry_first.delete(0, END)
        self.entry_second.delete(0, END)
        self.label_result.config(text='')
        self.entry_first.pack()
        shape = self.radio_1.get()

        if shape == 1:
            self.label_first.config(text='Numbers')
            self.label_second.config(text='')
            self.entry_second.pack_forget()
        elif shape == 2:
            self.label_first.config(text='Numbers')
            self.label_second.config(text='')
            self.entry_second.pack_forget()
        elif shape == 3:
            self.label_first.config(text='Numbers')
            self.label_second.config(text='')
            self.entry_second.pack_forget()
        elif shape == 4:
            self.label_first.config(text='Numerator')
            self.label_second.config(text='Denominator')
            self.entry_second.pack()
        elif shape == 5:
            self.label_first.config(text='T(n)')
            self.label_second.config(text='')
            self.entry_second.pack_forget()
        elif shape == 6:
            self.label_first.config(text='F(n)')
            self.label_second.config(text='')
            self.entry_second.pack_forget()

    # compute button function
    def compute(self):
        first_num = self.entry_first.get()
        second_num = self.entry_second.get()
        shape = self.radio_1.get()

        if shape == 1:
            self.label_result.config(text=f'{Operations().add(first_num)}')
        elif shape == 2:
            self.label_result.config(text=f'{Operations().subtract(first_num)}')
        elif shape == 3:
            self.label_result.config(text=f'{Operations().multiply(first_num)}')
        elif shape == 4:
            self.label_result.config(text=f'{Operations().divide(first_num, second_num)}')
        elif shape == 5:
            self.label_result.config(text=f'{Operations().triangular(first_num)}')
        elif shape == 6:
            self.label_result.config(text=f'{Operations().factorial(first_num)}')
        else:
            self.label_result.config(text='No operation selected')

    # clear button function
    def clear(self):
        self.radio_1.set(1)
        self.formulas()
