'''
Make a calculator using tkinter
It should do addition, subtraction, multiplication and division
It should remember the answer to the last operation to be used in the next operation
'''

from tkinter import *

global number_lst
global number_one
global number_two
global positive_toggle
global operation
global decimal_pressed
global last_button_pressed

number_one = ''
number_two = ''
operation = ''
number_lst = ''
positive_toggle = True
decimal_pressed = False
last_button_pressed = ''

calculator = Tk()
calculator.geometry('80x150')

def add_number(number):
    global number_lst
    global number_one
    global number_two
    global operation
    global positive_toggle
    global last_button_pressed

    if (last_button_pressed == 'num' or last_button_pressed == '' or last_button_pressed == 'back'):
        if (len(number_lst) < 12):
            if(number=='0.'):
                number_lst = number_lst + str(number)
                last_button_pressed = 'num'
            else:
                number_lst = number_lst + str(number)
                result_entry['text'] = number_lst
                last_button_pressed = 'num'
    elif (last_button_pressed == 'op'):
        print('test')
        if (len(number_lst) < 12):
            if (number=='0.'):
                number_lst = number_lst + str(number)
                last_button_pressed = 'num'
            else:
                number_lst = number_lst + str(number)
                result_entry['text'] = number_lst
                last_button_pressed = 'num'
    elif (last_button_pressed == 'eq'):
        number_one = ''
        number_two = ''
        operation = ''
        number_lst = ''
        positive_toggle = True
        number_lst = number_lst + str(number)
        result_entry['text'] = number_lst
        last_button_pressed = 'num'


def add_operation(operation_symbol):
    global number_lst
    global operation
    global decimal_pressed
    global positive_toggle
    global number_one
    global number_two
    global last_button_pressed

    if (last_button_pressed == 'num'):
        if (len(number_lst) > 0):
            if (number_lst[-1] == '.'):
                number_lst = number_lst[:-1]
            # if this is the first number
            if (number_one == ''):
                number_one = number_lst
            # if this is the second number
            elif(number_two==''):
                number_two = number_lst
                equal_button()
            else:
                number_two = number_lst
                equal_button()

            operation = operation_symbol
            if (operation_symbol == '**'):
                prev_operation['text'] = number_one + '^'
            else:
                prev_operation['text'] = number_one + operation
            number_lst = ''
            decimal_pressed = False
            positive_toggle = True
            last_button_pressed = 'op'

    elif (last_button_pressed == 'op' or last_button_pressed == 'back' and number_lst==''):
        operation = operation_symbol
        if (operation_symbol == '**'):
            prev_operation['text'] = number_one + '^'
        else:
            prev_operation['text'] = number_one + operation

    elif (last_button_pressed == 'eq'):
        operation = operation_symbol
        if (operation_symbol == '**'):
            prev_operation['text'] = number_one + '^'
        else:
            prev_operation['text'] = number_one + operation
        positive_toggle = True
        last_button_pressed = 'op'

    # if(number_lst!=''):
    #     number_two = ''
    #     if(operation=='' or equal_save==False):
    #         operation = operation_symbol
    #         if(operation_symbol=='**'):
    #             result_entry['text'] = result_entry['text'] + '^'
    #         else:
    #             result_entry['text'] = result_entry['text'] + operation
    #         equal_save=True
    #     else:
    #         operation = operation_symbol
    #         result_entry['text'] = result_entry['text'][0:-1] + operation
    #     if (number_save == True):
    #         global number_one
    #         number_one = number_lst
    #         number_lst = ''
    #         number_save = False
    #         decimal_save = True
    #     else:
    #         equal_button()
    #         operation = operation_symbol
    #         result_entry['text'] = result_entry['text'] + operation
    #         decimal_save = True

def equal_button():
    global number_one
    global number_two
    global number_lst
    global operation
    global decimal_pressed
    global last_button_pressed
    global positive_toggle

    def evaluate_result(number1, op, number2):
        result = eval(number1 + op + number2)
        print(number1 + op + number2 + '=' + str(result))
        return result

    if (last_button_pressed == 'num'):
        if (number_one != '' and operation != ''):
            number_two = number_lst
            number_lst = ''
            result = evaluate_result(number_one, operation, number_two)
            prev_operation['text'] = number_one + operation + number_two + '='
            number_one = str(result)
            result_entry['text'] = str(result)
            positive_toggle = True
            last_button_pressed = 'eq'
    elif (last_button_pressed == 'op'):
        number_two=number_one
        result = evaluate_result(number_one, operation, number_two)
        prev_operation['text'] = number_one + operation + number_two + '='
        number_one = str(result)
        result_entry['text'] = str(result)
        positive_toggle = True
        last_button_pressed = 'eq'
    elif (last_button_pressed == 'eq'):
        result = evaluate_result(number_one, operation, number_two)
        prev_operation['text'] = number_one + operation + number_two + '='
        number_one = str(result)
        result_entry['text'] = str(result)
        positive_toggle = True
        last_button_pressed = 'eq'

    # if(equal_save==False):
    #     result = eval(number_one + operation + number_two)
    #     result_entry['text'] = str(result)
    #     number_one = str(result)
    # else:
    #     number_two = number_lst
    #     if(int(float(number_two)) == 0 and operation == '/'):
    #         clear_button()
    #         result_entry['text'] = 'Cannot divide by zero'
    #     else:
    #         if (number_one != '' and number_two != '' and operation != ''):
    #             number_lst = ''
    #             result = eval(number_one + operation + number_two)
    #             result_entry['text'] = str(result)
    #             number_one = str(result)
    #             decimal_save = True
    #             equal_save = False
    #         else:
    #             print(number_one)
    #             print(number_two)

def clear_button():
    global number_lst
    global number_one
    global number_two
    global operation
    global positive_toggle
    global decimal_pressed
    global last_button_pressed
    number_lst = ''
    number_one = ''
    number_two = ''
    operation = ''
    positive_toggle = True
    decimal_pressed = False
    last_button_pressed = ''
    result_entry['text'] = number_lst
    prev_operation['text'] = number_lst

def add_decimal():
    global decimal_pressed
    global last_button_pressed
    #if there is no numbers in the number_lst, add 0 before the decimal when you press a number
    if (decimal_pressed == False):
        if (number_lst == ''):
            add_number('0.')
            decimal_pressed = True
        else:
            add_number('.')
            decimal_pressed = True

def positive_toggle_button():
    global number_lst
    global positive_toggle
    if(number_lst!=''):
        if (positive_toggle == True):
            number_lst = '-' + number_lst
            result_entry['text'] = number_lst
            positive_toggle = False
        else:
            number_lst = number_lst[1:]
            result_entry['text'] = number_lst
            positive_toggle = True

def backspace_button():
    global number_lst
    global last_button_pressed
    if(last_button_pressed!='op'):
        number_lst = number_lst[0:-1]
        result_entry['text'] = number_lst
        last_button_pressed = 'back'

def add_one():    add_number(1)
def add_two():    add_number(2)
def add_three():    add_number(3)
def add_four():    add_number(4)
def add_five():    add_number(5)
def add_six():    add_number(6)
def add_seven():    add_number(7)
def add_eight():    add_number(8)
def add_nine():    add_number(9)
def add_zero():    add_number(0)

def plus_button():    add_operation('+')
def minus_button():    add_operation('-')
def times_button():    add_operation('*')
def divide_button():    add_operation('/')
def exp_button():    add_operation('**')

display_frame = Frame(calculator)
prev_operation = Label(display_frame)
result_entry = Label(display_frame)

button_frame = Frame(calculator)
one = Button(button_frame, text='1', command=add_one)
two = Button(button_frame, text='2', command=add_two)
three = Button(button_frame, text='3', command=add_three)
four = Button(button_frame, text='4', command=add_four)
five = Button(button_frame, text='5', command=add_five)
six = Button(button_frame, text='6', command=add_six)
seven = Button(button_frame, text='7', command=add_seven)
eight = Button(button_frame, text='8', command=add_eight)
nine = Button(button_frame, text='9', command=add_nine)
zero = Button(button_frame, text='0', command=add_zero)
decimal = Button(button_frame, text='.', command=add_decimal)
clear = Button(button_frame, text='C', command=clear_button)
plus = Button(button_frame, text='+', command=plus_button)
minus = Button(button_frame, text='-', command=minus_button)
times = Button(button_frame, text='*', command=times_button)
divide = Button(button_frame, text='/', command=divide_button)
exp = Button(button_frame, text='exp', command=exp_button)
equal = Button(button_frame, text='=', command=equal_button)
toggle = Button(button_frame, text='+/-', command=positive_toggle_button)
backspace = Button(button_frame, text='<-', command=backspace_button)

display_frame.grid(row=0, column=0)
prev_operation.grid(row=0, column=0)
result_entry.grid(row=1, column=0)

button_frame.grid(row=1, column=0)
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
backspace.grid(row=4, column=4)

calculator.mainloop()
