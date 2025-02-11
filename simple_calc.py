# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# simple_calc.py
 
 
# Purpose: A simple GUI calculator which reflect all basic functions of calculator
 
from tkinter import *
import math

# Tkinter initialization
root = Tk()
root.title('Simple Calculator CS+ 115U') # Our program title

# Entry field styling
entry_value = Entry(root, width=35, borderwidth=5, justify=RIGHT, font=('Arial', 18))
entry_value.grid(row=0, column=0, columnspan=4, padx=10, pady=20)


############################################################################################
##################################  CALCULATIONS LOGIC  ####################################
############################################################################################

# Global variables
f_num = None
math_operation = ''
error = False  # Flag to indicate if an error has occurred

# Function to update the entry field
def update_entry(value):
    entry_value.delete(0, END)
    entry_value.insert(0, value)

# Function to handle number and decimal point button clicks
def button_click(number):
    global error
    if error:
        # If an error has occurred, clear it when a number is pressed
        button_clear()
        error = False
    current = entry_value.get()
    update_entry(current + str(number))

# Function to clear the entry field and reset variables
def button_clear():
    global f_num, math_operation, error
    entry_value.delete(0, END)
    f_num = None
    math_operation = ''
    error = False

# Function to handle operator buttons (+, -, *, /, ^)
def button_operation(operation):
    global f_num, math_operation, error
    if error:
        button_clear()
        error = False
    first_number = entry_value.get()
    try:
        f_num = float(first_number)
        math_operation = operation
        entry_value.delete(0, END)
    except ValueError:
        update_entry('Error')
        error = True

# Function to calculate and display the result
def button_equal():
    global f_num, math_operation, error
    second_number = entry_value.get()
    try:
        if math_operation == 'addition': # Addition button
            result = f_num + float(second_number)
        elif math_operation == 'subtraction': # Substraction button
            result = f_num - float(second_number)
        elif math_operation == 'multiplication': # Multiplication button
            result = f_num * float(second_number)
        elif math_operation == 'division': # Division button
            if float(second_number) == 0:
                update_entry('Cannot divide by zero') # Error handling for division by 0 (zero)
                error = True
                return
            result = f_num / float(second_number)
        elif math_operation == 'power': # Power button
            result = f_num ** float(second_number)
        else:
            update_entry('Error')
            error = True
            return

        # Hide decimals if the result is an integer
        if result.is_integer():
            result = int(result)
        update_entry(result)
        f_num = None
        math_operation = ''
    except Exception:
        update_entry('Error')
        error = True

# Functions for additional features
def button_pi(): # Pi button
    button_click(math.pi)

def button_e(): # e button
    button_click(math.e)

def button_square(): # square button
    try:
        number = float(entry_value.get())
        result = number ** 2
        if result.is_integer():
            result = int(result)
        update_entry(result)
    except Exception:
        update_entry('Error')

def button_cube(): # cube button
    try:
        number = float(entry_value.get())
        result = number ** 3
        if result.is_integer():
            result = int(result)
        update_entry(result)
    except Exception:
        update_entry('Error')

def button_sqrt(): # square root button
    try:
        number = float(entry_value.get())
        if number < 0:
            raise ValueError
        result = math.sqrt(number)
        if result.is_integer():
            result = int(result)
        update_entry(result)
    except Exception:
        update_entry('Error')

def button_cubert(): # cubic root button
    try:
        number = float(entry_value.get())
        result = number ** (1/3)
        if result.is_integer():
            result = int(result)
        update_entry(result)
    except Exception:
        update_entry('Error')

def button_factorial(): # factorial button
    try:
        number = float(entry_value.get())
        if not number.is_integer() or number < 0:
            raise ValueError
        result = math.factorial(int(number))
        update_entry(result)
    except Exception:
        update_entry('Error')

def button_reciprocal(): # recprocal button
    try:
        number = float(entry_value.get())
        if number == 0:
            update_entry('Cannot divide by zero') # Error handling for division by 0 (zero)
            global error
            error = True
            return
        result = 1 / number
        if result.is_integer():
            result = int(result)
        update_entry(result)
    except Exception:
        update_entry('Error')

def button_power_of_10(): # Power of 10 button
    try:
        number = float(entry_value.get())
        result = 10 ** number
        if result.is_integer():
            result = int(result)
        update_entry(result)
    except Exception:
        update_entry('Error')

############################################################################################
####################################  END OF THE BLOK  #####################################
############################################################################################


############################################################################################
######################  THIS BLOCK IS USED TO INITIALIZE THE BUTTONS  ######################
############################################################################################

# Define buttons for main number pad (numbers)
button_1 = Button(root, text='1', padx=20, pady=20, width=3, bg='white', fg='black', command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=20, pady=20, width=3, bg='white', fg='black', command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=20, pady=20, width=3, bg='white', fg='black', command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=20, pady=20, width=3, bg='white', fg='black', command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=20, pady=20, width=3, bg='white', fg='black', command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=20, pady=20, width=3, bg='white', fg='black', command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=20, pady=20, width=3, bg='white', fg='black', command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=20, pady=20, width=3, bg='white', fg='black', command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=20, pady=20, width=3, bg='white', fg='black', command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=20, pady=20, width=3, bg='white', fg='black', command=lambda: button_click(0))
button_decimal = Button(root, text='.', padx=20, pady=20, width=3, bg='white', fg='black', command=lambda: button_click('.'))

# Define buttons for main functions pad (addition, substraction, mltiplication, division, power)
button_add = Button(root, text='+', padx=20, pady=20, width=3, bg='light blue', fg='black', command=lambda: button_operation('addition'))
button_subtract = Button(root, text='-', padx=20, pady=20, width=3, bg='light blue', fg='black', command=lambda: button_operation('subtraction'))
button_multiply = Button(root, text='*', padx=20, pady=20, width=3, bg='light blue', fg='black', command=lambda: button_operation('multiplication'))
button_divide = Button(root, text='/', padx=20, pady=20, width=3, bg='light blue', fg='black', command=lambda: button_operation('division'))
button_power = Button(root, text='^', padx=20, pady=20, width=3, bg='light blue', fg='black', command=lambda: button_operation('power'))

# Define buttons for extra functions pad (equal, AC aka clear, Pi, root and othes)
button_equal = Button(root, text='=', padx=59, pady=20, width=6, bg='orange', fg='black', command=button_equal)
button_clear = Button(root, text='AC', padx=20, pady=20, width=3, bg='red', fg='white', command=button_clear)
button_pi = Button(root, text='π', padx=20, pady=20, width=3, bg='light green', fg='black', command=button_pi)
button_e = Button(root, text='e', padx=20, pady=20, width=3, bg='light green', fg='black', command=button_e)
button_square = Button(root, text='x²', padx=20, pady=20, width=3, bg='light green', fg='black', command=button_square)
button_cube = Button(root, text='x³', padx=20, pady=20, width=3, bg='light green', fg='black', command=button_cube)
button_sqrt = Button(root, text='√', padx=20, pady=20, width=3, bg='light green', fg='black', command=button_sqrt)
button_cubert = Button(root, text='∛', padx=20, pady=20, width=3, bg='light green', fg='black', command=button_cubert)
button_factorial = Button(root, text='x!', padx=20, pady=20, width=3, bg='light green', fg='black', command=button_factorial)
button_reciprocal = Button(root, text='1/x', padx=20, pady=20, width=3, bg='light green', fg='black', command=button_reciprocal)
button_power_of_10 = Button(root, text='10ⁿ', padx=20, pady=20, width=3, bg='light green', fg='black', command=button_power_of_10)

############################################################################################
####################################  END OF THE BLOK  #####################################
############################################################################################


############################################################################################
###################  THIS BLOK IS USED TO ARRANGE BUTTONS ON THE SCREEN  ###################
############################################################################################

# Buttons grid on the screen layout
# First row (1 of 7)
button_e.grid(row=1, column=0)
button_square.grid(row=1, column=1)
button_cube.grid(row=1, column=2)
button_sqrt.grid(row=1, column=3)

# Second row (2 of 7)
button_cubert.grid(row=2, column=0)
button_factorial.grid(row=2, column=1)
button_reciprocal.grid(row=2, column=2)
button_power_of_10.grid(row=2, column=3)

# Third row (3 of 7)
button_clear.grid(row=3, column=0)
button_power.grid(row=3, column=1)
button_pi.grid(row=3, column=2)
button_divide.grid(row=3, column=3)

# Fourth row (4 of 7)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_multiply.grid(row=4, column=3)

# Fifth row (5 of 7)
button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_subtract.grid(row=5, column=3)

# Sixth row (6 of 7)
button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
button_add.grid(row=6, column=3)

# Seventh row (7 of 7)
button_0.grid(row=7, column=0)
button_decimal.grid(row=7, column=1)
button_equal.grid(row=7, column=2, columnspan=2, sticky='ns')

############################################################################################
####################################  END OF THE BLOK  #####################################
############################################################################################


# Loop initialization for the application run
root.mainloop()
