# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# simple_calc_improved.py
 
 
# Purpose: A simple GUI calculator which reflect all basic functions of calculator
 
import tkinter as tk
from functools import partial
import math

class SimpleCalculator:
    def __init__(self, root): # Self inintialization
        self.root = root
        self.root.title('Simple Calculator+ CS 115U') # Our program title name
        
        # Entry widget for output
        self.entry_value = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 24), justify='right')
        self.entry_value.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
        
        # Variables initialization
        self.current = '' # Initially is blank
        self.total = None # Initially is NONE
        self.operator = '' # Initially is blank
        self.error = False  # Flag to indicate an error state
        
        # Create buttons
        self.create_buttons()
    
    # Function for buttons creation
    def create_buttons(self):
        # Button text and grid positions + buttons functional typization for styling
        buttons = [
            ('AC', 1, 0, 'clear'), ('^', 1, 1, 'operator'), ('x²', 1, 2, 'function'), ('x³', 1, 3, 'function'),
            ('π', 2, 0, 'function'), ('e', 2, 1, 'function'),  ('√', 2, 2, 'function'), ('∛', 2, 3, 'function'),
            ('x!', 3, 0, 'function'), ('1/x', 3, 1, 'function'),('10ⁿ', 3, 2, 'function'),('/', 3, 3, 'operator'),
            ('7', 4, 0, 'number'), ('8', 4, 1, 'number'), ('9', 4, 2, 'number'), ('*', 4, 3, 'operator'),
            ('4', 5, 0, 'number'), ('5', 5, 1, 'number'), ('6', 5, 2, 'number'), ('-', 5, 3, 'operator'),
            ('1', 6, 0, 'number'), ('2', 6, 1, 'number'), ('3', 6, 2, 'number'), ('+', 6, 3, 'operator'),
            ('0', 7, 0, 'number'), ('.', 7, 1, 'number'),  ('=', 7, 2, 'equal')
        ]
        
        # Buttons styling and size
        for (text, row, col, btn_type) in buttons:
            action = partial(self.on_button_click, text)
            # Assign colors based on button type
            if btn_type == 'number':
                bg_color = 'white'
                fg_color = 'black'
            elif btn_type == 'operator':
                bg_color = 'light blue'
                fg_color = 'black'
            elif btn_type == 'function':
                bg_color = 'light green'
                fg_color = 'black'
            elif btn_type == 'equal':
                bg_color = 'orange'
                fg_color = 'black'
            elif btn_type == 'clear':
                bg_color = 'red'
                fg_color = 'white'
            else:
                bg_color = 'light gray'
                fg_color = 'black'
            if btn_type != 'equal': # Styling for all buttons except "equal"
                tk.Button(self.root, text=text, width=5, height=2, font=('Arial', 18),
                    bg=bg_color, fg=fg_color, command=action)\
                .grid(row=row, column=col, padx=5, pady=5)
            else: # Styling for a huge "equal" button
                tk.Button(self.root, text=text, width=14, height=2, font=('Arial', 18),
                    bg=bg_color, fg=fg_color, command=action)\
                .grid(row=row, column=col, columnspan=2, padx=5, pady=5)
    
    # Buttons functionality and behavior
    def on_button_click(self, char):
        if self.error:
            # If an error has occurred, only 'AC' aka 'Clear button should be responsive
            if char == 'AC': # Clear button to resset the calculator state
                self.reset_calculator()
            else:
                return  # Ignore other inputs until 'AC' is pressed
        else:
            if char.isdigit() or char == '.': # Check for the correct input
                self.current += char
                self.update_entry(self.current)
            elif char in '+-*/^': # Check for type of operation (addition, substraction, multiplication, division and power)
                if self.operator and self.current:
                    result = self.evaluate(self.total, self.current, self.operator)
                    if result is not None:
                        self.total = result
                        self.update_entry(self.total)
                    else:
                        # An error occurred; exit the method
                        return
                elif self.current:
                    self.total = float(self.current)
                self.operator = char
                self.current = ''
                # Display the operator in the entry field
                self.update_entry(self.operator)
            elif char == '=': # Equal button to call calculation result logic
                if self.operator and self.current:
                    result = self.evaluate(self.total, self.current, self.operator)
                    if result is not None:
                        self.total = result
                        self.update_entry(self.total)
                        self.current = str(self.total)
                        self.total = None
                        self.operator = ''
                    else:
                        # An error occurred; exit the method
                        return
            elif char == 'AC': # AC/Clear button
                self.reset_calculator() # Clear output screen
            elif char == 'π': # Pi button
                self.current += str(math.pi)
                self.update_entry(self.current) # Update value
            elif char == 'e': # e button
                self.current += str(math.e)
                self.update_entry(self.current) # Update value
            elif char == 'x²': # Power of two button
                try:
                    result = float(self.current) ** 2 # n-number in 2nd power
                    self.current = str(result)
                    self.update_entry(self.current) # Update value
                except Exception:
                    self.display_error('Error') # Error flag rise
            elif char == 'x³': # Power of three button
                try:
                    result = float(self.current) ** 3 # n-number in 3nd power
                    self.current = str(result)
                    self.update_entry(self.current) # Update value
                except Exception:
                    self.display_error('Error') # Error flag rise
            elif char == '√': # Square root button
                try:
                    result = math.sqrt(float(self.current)) # n-number in 2nd root degree
                    self.current = str(result)
                    self.update_entry(self.current) # Update value
                except Exception:
                    self.display_error('Error') # Error flag rise
            elif char == '∛': # Root in 3rd degree button
                try:
                    result = float(self.current) ** (1/3) # n-number in 3nd root degree
                    self.current = str(result)
                    self.update_entry(self.current) # Update value
                except Exception:
                    self.display_error('Error') # Error flag rise
            elif char == 'x!': # Factorial button
                try:
                    result = math.factorial(int(float(self.current))) # Factorial calcualtion
                    self.current = str(result)
                    self.update_entry(self.current) # Update value
                except Exception:
                    self.display_error('Error') # Error flag rise
            elif char == '1/x': # Reciprocal button
                try:
                    if float(self.current) == 0: # Error handling for division by 0 (zero)
                        raise ZeroDivisionError
                    result = 1 / float(self.current) # Reciprocal calcualtion
                    self.current = str(result)
                    self.update_entry(self.current) # Update value
                except ZeroDivisionError:
                    self.display_error('Cannot divide by zero') # Error handling for division by 0 (zero)
                except Exception:
                    self.display_error('Error') # Error flag rise
            elif char == '10ⁿ': # Power of 10 button
                try:
                    result = 10 ** float(self.current) # Power of 10 calcualtion
                    self.current = str(result)
                    self.update_entry(self.current) # Update value
                except Exception:
                    self.display_error('Error') # Error flag rise

    # Function for the entry update
    def update_entry(self, value):
        self.entry_value.delete(0, tk.END)
        # Condition check for decimal point and operators
        try:
            num = float(value)
            if num.is_integer():
                # Display without decimal point if it's an integer
                self.entry_value.insert(0, int(num))
            else:
                # Display as float
                self.entry_value.insert(0, value)
        except ValueError:
            # If value is not a number (e.g., operator or error message), display as is
            self.entry_value.insert(0, value)
    
    # Function for calculations itself
    def evaluate(self, total, current, operator):
        try:
            total = float(total)
            current = float(current)
            if operator == '+': # Addition
                return total + current
            elif operator == '-': # Substraction
                return total - current
            elif operator == '*': # Multiplication
                return total * current
            elif operator == '/': # Division
                if current == 0:
                    raise ZeroDivisionError # Error handling for division by 0 (zero)
                return total / current
            elif operator == '^': # Rising to the power
                return total ** current
        except ZeroDivisionError: # Error handler if someone will try to divide by 0
            self.display_error('Cannot divide by zero') # Error handling for division by 0 (zero)
            return None
        except Exception: # Error handling for unpredicted behavior
            self.display_error('Error') # Error flag rise
            return None
    
    # Error handling function
    def display_error(self, message): # Show error message to user
        self.entry_value.delete(0, tk.END)
        self.entry_value.insert(0, message)
        self.error = True  # Set error flag to True
    
    # Reset calculations and error mesages function, it drops all values to the initial
    def reset_calculator(self):
        self.current = ''
        self.total = None
        self.operator = ''
        self.error = False
        self.update_entry('')
    
# Application run block
if __name__ == '__main__':
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
