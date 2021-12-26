'''
Make a calculator using tkinter
It should do addition, subtraction, multiplication and division
It should remember the answer to the last operation to be used in the next operation
'''

from tkinter import *

global number_lst
global number_one
global number_two
global number_save
global button_toggle
global operation
number_one = ''
number_two = ''
operation = ''
number_save = True
button_toggle = True
number_lst = ''
calculator = Tk()

def add_number(number):
    global number_lst
    global number_one
    global number_two
    global operation
    global number_save
    if (operation==''):
        number_one = ''
        number_two = ''
        number_save = True
    if (len(number_lst) < 12):
        number_lst = number_lst + str(number)
        result_entry['text'] = number_lst

def add_operation(operation_symbol):
    global number_lst
    global number_save
    global operation
    operation = operation_symbol
    result_entry['text'] = result_entry['text'] + operation
    if (len(number_lst) > 0):
        if (number_save == True):
            global number_one
            number_one = number_lst
            number_lst = ''
            number_save = False
        else:
            print('test')
            equal_button()
            operation = operation_symbol
            result_entry['text'] = result_entry['text'] + operation


def add_one():
    add_number(1)


def add_two():
    add_number(2)


def add_three():
    add_number(3)


def add_four():
    add_number(4)


def add_five():
    add_number(5)


def add_six():
    add_number(6)


def add_seven():
    add_number(7)


def add_eight():
    add_number(8)


def add_nine():
    add_number(9)


def add_zero():
    add_number(0)


def plus_button():
    add_operation('+')


def minus_button():
    add_operation('-')


def times_button():
    add_operation('*')


def divide_button():
    add_operation('/')


def exp_button():
    add_operation('**')


def equal_button():
    global number_one
    global number_two
    global number_lst
    global operation
    number_two = number_lst
    if (number_one != '' and number_two != '' and operation != ''):
        number_two = number_lst
        number_lst = ''
        result = eval(number_one + operation + number_two)
        result_entry['text'] = str(result)
        number_one = str(result)
        number_two = ''
        operation = ''
    else:
        print(number_one)
        print(number_two)


def clear_button():
    global number_lst
    global number_one
    global number_two
    global number_save
    global operation
    global button_toggle
    number_lst = ''
    number_one = ''
    number_two = ''
    operation = ''
    number_save = True
    button_toggle = True
    result_entry['text'] = number_lst


def positive_toggle_button():
    global number_lst
    global button_toggle
    if (button_toggle == True):
        number_lst = '-' + number_lst
        result_entry['text'] = number_lst
        button_toggle = False
    else:
        number_lst = number_lst.replace('-', '')
        result_entry['text'] = number_lst
        button_toggle = True


# todo
#  backspace
#  pressing the equal button repeats the last operation
#  check for division by zero
#  make result label not affect buttons
#  add decimal

result_entry = Label(calculator)
one = Button(calculator, text='1', command=add_one)
two = Button(calculator, text='2', command=add_two)
three = Button(calculator, text='3', command=add_three)
four = Button(calculator, text='4', command=add_four)
five = Button(calculator, text='5', command=add_five)
six = Button(calculator, text='6', command=add_six)
seven = Button(calculator, text='7', command=add_seven)
eight = Button(calculator, text='8', command=add_eight)
nine = Button(calculator, text='9', command=add_nine)
zero = Button(calculator, text='0', command=add_zero)
decimal = Button(calculator, text='.')
clear = Button(calculator, text='C', command=clear_button)
plus = Button(calculator, text='+', command=plus_button)
minus = Button(calculator, text='-', command=minus_button)
times = Button(calculator, text='*', command=times_button)
divide = Button(calculator, text='/', command=divide_button)
exp = Button(calculator, text='exp', command=exp_button)
equal = Button(calculator, text='=', command=equal_button)
toggle = Button(calculator, text='+/-', command=positive_toggle_button)

result_entry.grid(row=0, column=0)
one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
divide.grid(row=1, column=3)
equal.grid(row=1, column=4)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
times.grid(row=2, column=3)
exp.grid(row=2, column=4)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
minus.grid(row=3, column=3)
toggle.grid(row=3, column=4)
clear.grid(row=4, column=0)
zero.grid(row=4, column=1)
decimal.grid(row=4, column=2)
plus.grid(row=4, column=3)

calculator.mainloop()
