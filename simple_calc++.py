# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# simple_calc++.py
 
 
# Purpose: An improved graphing calculator that displays all the basic calculator functions and more!
# Now it allows you to use scientific notation and percentages with floating point numbers and can work with fractions.
# As a bonus, it can calculate a loan based on terms.

import math
import tkinter as tk
from functools import partial


# Fraction Class
class Fraction:
    # __init__
    #
    # Purpose: Initialize a Fraction instance with a numerator and denominator.
    # Parameters: numerator (int), denominator (int)
    # Return: None
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            self.denominator = 1

    # set_denominator
    #
    # Purpose: Set the denominator of the fraction.
    # Parameters: den (int)
    # Return: None
    def set_denominator(self, den):
        if den != 0:
            self.denominator = den

    # set_numerator
    #
    # Purpose: Set the numerator of the fraction.
    # Parameters: num (int)
    # Return: None
    def set_numerator(self, num):
        self.numerator = num

    # get_denominator
    #
    # Purpose: Get the denominator.
    # Parameters: None
    # Return: int - denominator
    def get_denominator(self):
        return self.denominator

    # get_numerator
    #
    # Purpose: Get the numerator.
    # Parameters: None
    # Return: int - numerator
    def get_numerator(self):
        return self.numerator

    # reduce
    #
    # Purpose: Reduce the fraction to lowest terms.
    # Parameters: None
    # Return: None
    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    # add
    #
    # Purpose: Add another fraction to this fraction.
    # Parameters: frac (Fraction)
    # Return: None
    def add(self, frac):
        new_denominator = self.denominator * frac.denominator
        new_numerator = (self.numerator * frac.denominator) + (frac.numerator * self.denominator)
        self.numerator = new_numerator
        self.denominator = new_denominator
        self.reduce()

    # subtract
    #
    # Purpose: Subtract another fraction from this fraction.
    # Parameters: frac (Fraction)
    # Return: None
    def subtract(self, frac):
        new_denominator = self.denominator * frac.denominator
        new_numerator = (self.numerator * frac.denominator) - (frac.numerator * self.denominator)
        self.numerator = new_numerator
        self.denominator = new_denominator
        self.reduce()

    # __str__
    #
    # Purpose: String representation of the fraction.
    # Parameters: None
    # Return: str
    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"


# MixedNumber Class
class MixedNumber(Fraction):
    # __init__
    #
    # Purpose: Initialize a MixedNumber instance with whole, numerator, denominator.
    # Parameters: whole (int), numerator (int), denominator (int)
    # Return: None
    def __init__(self, whole, numerator, denominator):
        super().__init__(numerator, denominator)
        self.whole = whole

    # setWhole
    #
    # Purpose: Set the whole part of the mixed number.
    # Parameters: whole (int)
    # Return: None
    def setWhole(self, whole):
        self.whole = whole

    # reduce
    #
    # Purpose: Reduce the mixed number to a proper mixed number.
    # Parameters: None
    # Return: None
    def reduce(self):
        super().reduce()
        whole = self.numerator // self.denominator
        remainder = self.numerator % self.denominator
        self.numerator = remainder
        self.whole += whole

    # add
    #
    # Purpose: Add another fraction or mixed number to this mixed number.
    # Parameters: frac (Fraction or MixedNumber)
    # Return: None
    def add(self, frac):
        self.numerator += self.whole * self.denominator
        if isinstance(frac, MixedNumber):
            frac_numerator = frac.whole * frac.denominator + frac.numerator
            frac = Fraction(frac_numerator, frac.denominator)
        super().add(frac)
        self.whole = self.numerator // self.denominator
        self.numerator = self.numerator % self.denominator
        if self.numerator < 0:
            self.numerator += self.denominator
            self.whole -= 1

    # subtract
    #
    # Purpose: Subtract another fraction or mixed number from this mixed number.
    # Parameters: frac (Fraction or MixedNumber)
    # Return: None
    def subtract(self, frac):
        self.numerator += self.whole * self.denominator
        if isinstance(frac, MixedNumber):
            frac_numerator = frac.whole * frac.denominator + frac.numerator
            frac = Fraction(frac_numerator, frac.denominator)
        super().subtract(frac)
        self.whole = self.numerator // self.denominator
        self.numerator = self.numerator % self.denominator
        if self.numerator < 0:
            self.numerator += self.denominator
            self.whole -= 1

    # __str__
    #
    # Purpose: String representation of the mixed number.
    # Parameters: None
    # Return: str
    def __str__(self):
        if self.whole == 0:
            return super().__str__()
        elif self.numerator == 0:
            return f"{self.whole}"
        return f"{self.whole} {self.numerator}/{self.denominator}"


class SimpleCalculator:
    # __init__
    #
    # Purpose: Initialize the calculator GUI and state.
    # Parameters: root (tk.Tk) - the main application window
    # Return: None
    def __init__(self, root):
        self.root = root
        self.root.title('Simple Calculator+ CS 115U')

        # Variables initialization
        self.current = ''
        self.total = None
        self.operator = ''
        self.error = False
        self.fraction_mode = False  # Toggle between fraction and float mode
        self.display_format = tk.StringVar(value="normal")  # normal, scientific, percentage
        self.loan_mode = False
        self.selected_loan_field = None

        # Entry widget for output (for calculator mode)
        self.entry_value = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 24), justify='right')
        self.entry_value.grid(row=0, column=0, columnspan=5, padx=10, pady=20)

        # Create format radio buttons
        self.create_format_radio_buttons()

        # Create fraction/float mode toggle
        self.create_mode_toggle()

        # Create loan mode toggle
        self.create_loan_mode_toggle()

        # Create loan frame (initially hidden)
        self.create_loan_frame()

        # Create buttons
        self.create_buttons()

    # create_format_radio_buttons
    #
    # Purpose: Create radio buttons for display formats.
    # Parameters: None
    # Return: None
    def create_format_radio_buttons(self):
        frame = tk.Frame(self.root)
        frame.grid(row=1, column=0, columnspan=5, pady=5)

        tk.Radiobutton(frame, text="Normal", variable=self.display_format, value="normal",
                       command=self.update_display).pack(side=tk.LEFT)
        tk.Radiobutton(frame, text="Scientific", variable=self.display_format, value="scientific",
                       command=self.update_display).pack(side=tk.LEFT)
        tk.Radiobutton(frame, text="Percentage", variable=self.display_format, value="percentage",
                       command=self.update_display).pack(side=tk.LEFT)

    # create_mode_toggle
    #
    # Purpose: Create a button to toggle between fraction mode and float mode.
    # Parameters: None
    # Return: None
    def create_mode_toggle(self):
        def toggle_mode():
            self.fraction_mode = not self.fraction_mode
            mode_text = "Fraction Mode" if self.fraction_mode else "Float Mode"
            mode_button.config(text=mode_text)
            self.reset_calculator()

        mode_button = tk.Button(self.root, text="Float Mode", command=toggle_mode, bg='lightyellow')
        mode_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # create_loan_mode_toggle
    #
    # Purpose: Create a button that toggles loan mode in the same window.
    # Parameters: None
    # Return: None
    def create_loan_mode_toggle(self):
        def toggle_loan_mode():
            self.loan_mode = not self.loan_mode
            if self.loan_mode:
                loan_button.config(text="Calculator Mode")
                self.loan_frame.grid(row=3, column=0, columnspan=5, pady=5)
                self.reset_calculator()
            else:
                loan_button.config(text="Loan Mode")
                self.loan_frame.grid_remove()
                self.reset_calculator()

        loan_button = tk.Button(self.root, text="Loan Mode", command=toggle_loan_mode, bg='lightpink')
        loan_button.grid(row=2, column=2, columnspan=3, padx=5, pady=5)

    # create_loan_frame
    #
    # Purpose: Create a frame for loan calculation input in the same window.
    # Parameters: None
    # Return: None
    def create_loan_frame(self):
        self.loan_frame = tk.Frame(self.root, bd=2, relief='groove')

        tk.Label(self.loan_frame, text="Loan Amount:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        tk.Label(self.loan_frame, text="Annual Interest Rate (%):").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        tk.Label(self.loan_frame, text="Number of Years:").grid(row=2, column=0, padx=5, pady=5, sticky='e')

        self.loan_amount_var = tk.StringVar()
        self.interest_rate_var = tk.StringVar()
        self.years_var = tk.StringVar()

        self.loan_amount_entry = tk.Entry(self.loan_frame, textvariable=self.loan_amount_var, width=20)
        self.interest_rate_entry = tk.Entry(self.loan_frame, textvariable=self.interest_rate_var, width=20)
        self.years_entry = tk.Entry(self.loan_frame, textvariable=self.years_var, width=20)

        self.loan_amount_entry.grid(row=0, column=1, padx=5, pady=5)
        self.interest_rate_entry.grid(row=1, column=1, padx=5, pady=5)
        self.years_entry.grid(row=2, column=1, padx=5, pady=5)

        # Clicking on these fields selects them for numeric input
        self.loan_amount_entry.bind("<Button-1>", lambda e: self.select_loan_field("amount"))
        self.interest_rate_entry.bind("<Button-1>", lambda e: self.select_loan_field("rate"))
        self.years_entry.bind("<Button-1>", lambda e: self.select_loan_field("years"))

        tk.Button(self.loan_frame, text="Calculate Loan", command=self.calculate_loan).grid(row=3, column=0, columnspan=2, pady=10)

        self.loan_result_label = tk.Label(self.loan_frame, text="", fg='blue', justify='left')
        self.loan_result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Initially not visible until loan mode is toggled
        self.loan_frame.grid_remove()

    # select_loan_field
    #
    # Purpose: Select which loan field is currently active for numeric input from calculator buttons.
    # Parameters: field (str) - 'amount', 'rate', or 'years'
    # Return: None
    def select_loan_field(self, field):
        self.selected_loan_field = field

    # calculate_loan
    #
    # Purpose: Calculate and display the loan details.
    # Parameters: None
    # Return: None
    def calculate_loan(self):
        try:
            loan_amount = float(self.loan_amount_var.get())
            annual_interest_rate = float(self.interest_rate_var.get()) / 100.0
            years = int(self.years_var.get())

            monthly_interest_rate = annual_interest_rate / 12
            number_of_payments = years * 12

            if monthly_interest_rate == 0:
                monthly_payment = loan_amount / number_of_payments
            else:
                monthly_payment = (loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments)) \
                                  / ((1 + monthly_interest_rate)**number_of_payments - 1)

            total_amount_paid = monthly_payment * number_of_payments
            total_interest_paid = total_amount_paid - loan_amount

            result_text = (f"Monthly Payment: ${monthly_payment:.2f}\n"
                           f"Total Interest Paid: ${total_interest_paid:.2f}\n"
                           f"Total Amount Paid: ${total_amount_paid:.2f}")
            self.loan_result_label.config(text=result_text)
        except Exception:
            self.loan_result_label.config(text="Error in calculation.")

    # create_buttons
    #
    # Purpose: Create the calculator buttons.
    # Parameters: None
    # Return: None
    def create_buttons(self):
        buttons = [
            ('AC', 4, 0, 'clear'), ('^', 4, 1, 'operator'), ('x²', 4, 2, 'function'), ('x³', 4, 3, 'function'),
            ('π', 5, 0, 'function'), ('e', 5, 1, 'function'),  ('√', 5, 2, 'function'), ('∛', 5, 3, 'function'),
            ('x!', 6, 0, 'function'), ('1/x', 6, 1, 'function'),('10ⁿ', 6, 2, 'function'),('/', 6, 3, 'operator'),
            ('7', 7, 0, 'number'), ('8', 7, 1, 'number'), ('9', 7, 2, 'number'), ('*', 7, 3, 'operator'),
            ('4', 8, 0, 'number'), ('5', 8, 1, 'number'), ('6', 8, 2, 'number'), ('-', 8, 3, 'operator'),
            ('1', 9, 0, 'number'), ('2', 9, 1, 'number'), ('3', 9, 2, 'number'), ('+', 9, 3, 'operator'),
            ('0', 10, 0, 'number'), ('.', 10, 1, 'number'),  ('=', 10, 2, 'equal')
        ]

        for (text, row, col, btn_type) in buttons:
            action = partial(self.on_button_click, text, btn_type)
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
            if btn_type != 'equal':
                tk.Button(self.root, text=text, width=5, height=2, font=('Arial', 18),
                          bg=bg_color, fg=fg_color, command=action)\
                    .grid(row=row, column=col, padx=5, pady=5)
            else:
                tk.Button(self.root, text=text, width=14, height=2, font=('Arial', 18),
                          bg=bg_color, fg=fg_color, command=action)\
                    .grid(row=row, column=col, columnspan=2, padx=5, pady=5)

    # on_button_click
    #
    # Purpose: Handle button clicks for numbers, operators, functions, and input in loan mode.
    # Parameters: char (str), btn_type (str)
    # Return: None
    def on_button_click(self, char, btn_type):
        if self.loan_mode:
            # In loan mode, only number and '.' inputs affect the selected loan field
            if self.selected_loan_field is not None:
                if btn_type == 'number':
                    # Append the character to the selected loan field
                    if self.selected_loan_field == "amount":
                        self.loan_amount_var.set(self.loan_amount_var.get() + char)
                    elif self.selected_loan_field == "rate":
                        self.interest_rate_var.set(self.interest_rate_var.get() + char)
                    elif self.selected_loan_field == "years":
                        self.years_var.set(self.years_var.get() + char)
                elif char == '.' and self.selected_loan_field:
                    # Add decimal point if not present
                    field_val = ""
                    if self.selected_loan_field == "amount":
                        field_val = self.loan_amount_var.get()
                        if '.' not in field_val:
                            self.loan_amount_var.set(field_val + '.')
                    elif self.selected_loan_field == "rate":
                        field_val = self.interest_rate_var.get()
                        if '.' not in field_val:
                            self.interest_rate_var.set(field_val + '.')
                    elif self.selected_loan_field == "years":
                        field_val = self.years_var.get()
                        if '.' not in field_val:
                            self.years_var.set(field_val + '.')
                elif char == 'AC':
                    # Clear loan fields
                    self.loan_amount_var.set('')
                    self.interest_rate_var.set('')
                    self.years_var.set('')
                    self.loan_result_label.config(text="")
            else:
                # No field selected, only AC makes sense
                if char == 'AC':
                    self.loan_amount_var.set('')
                    self.interest_rate_var.set('')
                    self.years_var.set('')
                    self.loan_result_label.config(text="")
            return

        # Normal calculator mode:
        if self.error:
            if char == 'AC':
                self.reset_calculator()
            else:
                return
        else:
            if btn_type == 'number':
                self.current += char
                self.update_entry(self.current)
            elif btn_type == 'operator':
                if self.operator and self.current:
                    result = self.do_calculation(self.total, self.current, self.operator)
                    if result is not None:
                        self.total = result
                        self.update_entry(self.total)
                    else:
                        return
                elif self.current:
                    self.total = self.parse_input(self.current)
                self.operator = char
                self.current = ''
                self.update_entry(self.operator)
            elif char == '=':
                if self.operator and self.current:
                    result = self.do_calculation(self.total, self.current, self.operator)
                    if result is not None:
                        self.total = result
                        self.update_entry(self.total)
                        self.current = str(self.total)
                        self.total = None
                        self.operator = ''
                    else:
                        return
            elif char == 'AC':
                self.reset_calculator()
            elif char == 'π':
                self.current += str(math.pi)
                self.update_entry(self.current)
            elif char == 'e':
                self.current += str(math.e)
                self.update_entry(self.current)
            elif char == 'x²':
                try:
                    val = self.parse_input(self.current)
                    result = self.square(val)
                    self.current = str(result)
                    self.update_entry(self.current)
                except Exception:
                    self.display_error('Error')
            elif char == 'x³':
                try:
                    val = self.parse_input(self.current)
                    result = self.cube(val)
                    self.current = str(result)
                    self.update_entry(self.current)
                except Exception:
                    self.display_error('Error')
            elif char == '√':
                try:
                    val = self.parse_input(self.current)
                    result = self.sqrt(val)
                    self.current = str(result)
                    self.update_entry(self.current)
                except Exception:
                    self.display_error('Error')
            elif char == '∛':
                try:
                    val = self.parse_input(self.current)
                    result = self.cbrt(val)
                    self.current = str(result)
                    self.update_entry(self.current)
                except Exception:
                    self.display_error('Error')
            elif char == 'x!':
                try:
                    val = self.parse_input(self.current)
                    result = self.factorial(val)
                    self.current = str(result)
                    self.update_entry(self.current)
                except Exception:
                    self.display_error('Error')
            elif char == '1/x':
                try:
                    val = self.parse_input(self.current)
                    result = self.reciprocal(val)
                    self.current = str(result)
                    self.update_entry(self.current)
                except ZeroDivisionError:
                    self.display_error('Cannot divide by zero')
                except Exception:
                    self.display_error('Error')
            elif char == '10ⁿ':
                try:
                    val = self.parse_input(self.current)
                    result = self.ten_pow(val)
                    self.current = str(result)
                    self.update_entry(self.current)
                except Exception:
                    self.display_error('Error')

    # parse_input
    #
    # Purpose: Parse the current input (string) into either a float or a Fraction/MixedNumber depending on mode.
    # Parameters: input_str (str)
    # Return: float or Fraction/MixedNumber
    def parse_input(self, input_str):
        input_str = input_str.strip()
        if not self.fraction_mode:
            # Just parse as float
            return float(input_str)
        else:
            # Fraction mode: If slash is found, parse as fraction; if mixed format, parse as MixedNumber; 
            # Otherwise fraction with denominator = 1
            if ' ' in input_str:
                # Mixed number format: "a b/c"
                parts = input_str.split()
                if len(parts) == 2 and '/' in parts[1]:
                    whole = int(parts[0])
                    num, den = parts[1].split('/')
                    num, den = int(num), int(den)
                    mix = MixedNumber(whole, num, den)
                    mix.reduce()
                    return mix
                else:
                    # No valid fraction detected, treat as fraction with denominator = 1
                    val = float(input_str)
                    return self.float_to_fraction(val)
            else:
                # Simple fraction a/b or just a number, like 3/4 or 0.75
                if '/' in input_str:
                    num, den = input_str.split('/')
                    num, den = int(num), int(den)
                    frac = Fraction(num, den)
                    frac.reduce()
                    return frac
                else:
                    # No slash means it's a whole number in fraction mode -> fraction with denominator = 1
                    val = float(input_str)
                    return self.float_to_fraction(val)

    # float_to_fraction
    #
    # Purpose: Convert a float to a fraction (denominator=1 if it's an integer).
    # Parameters: val (float)
    # Return: Fraction
    def float_to_fraction(self, val):
        # If val is an integer, just Fraction(val, 1)
        if val.is_integer():
            return Fraction(int(val), 1)
        # If val not integer, limit denominator:
        from fractions import Fraction as PyFraction
        f = PyFraction(val).limit_denominator(1000000)
        return Fraction(f.numerator, f.denominator)

    # do_calculation
    #
    # Purpose: Perform arithmetic operations on total and current.
    # Parameters: total (float/Fraction), current (str), operator (str)
    # Return: float/Fraction/MixedNumber or None if error
    def do_calculation(self, total, current, operator):
        try:
            current_val = self.parse_input(current)
            return self.evaluate(total, current_val, operator)
        except ZeroDivisionError:
            self.display_error('Cannot divide by zero')
            return None
        except Exception:
            self.display_error('Error')
            return None

    # evaluate
    #
    # Purpose: Evaluate the operation (total operator current_val).
    # Parameters: total (float/Fraction), current_val (float/Fraction), operator (str)
    # Return: float/Fraction/MixedNumber
    def evaluate(self, total, current_val, operator):
        if isinstance(total, (Fraction, MixedNumber)) or isinstance(current_val, (Fraction, MixedNumber)) or self.fraction_mode:
            # Always do fraction arithmetic in fraction mode
            total = self.to_fraction(total)
            current_val = self.to_fraction(current_val)
            if operator == '+':
                total.add(current_val)
                return total
            elif operator == '-':
                total.subtract(current_val)
                return total
            elif operator == '*':
                f = Fraction(total.numerator * current_val.numerator, total.denominator * current_val.denominator)
                f.reduce()
                return f
            elif operator == '/':
                if current_val.numerator == 0:
                    raise ZeroDivisionError
                f = Fraction(total.numerator * current_val.denominator, total.denominator * current_val.numerator)
                f.reduce()
                return f
            elif operator == '^':
                # Fraction exponentiation: convert to float for exponentiation
                val = (total.numerator / total.denominator) ** (current_val.numerator / current_val.denominator)
                # Return fraction if fraction_mode is on
                if self.fraction_mode:
                    return self.float_to_fraction(val)
                else:
                    return val
        else:
            # Float operations (fraction_mode off)
            total = float(total)
            current_val = float(current_val)
            if operator == '+':
                return total + current_val
            elif operator == '-':
                return total - current_val
            elif operator == '*':
                return total * current_val
            elif operator == '/':
                if current_val == 0:
                    raise ZeroDivisionError
                return total / current_val
            elif operator == '^':
                return total ** current_val

    # to_fraction
    #
    # Purpose: Convert a float or Fraction/MixedNumber to a Fraction.
    # Parameters: val (float or Fraction/MixedNumber)
    # Return: Fraction
    def to_fraction(self, val):
        if isinstance(val, Fraction):
            return val
        if isinstance(val, MixedNumber):
            # Convert mixed number to improper fraction
            num = val.whole * val.denominator + val.numerator
            return Fraction(num, val.denominator)
        else:
            # Convert float to fraction
            from fractions import Fraction as PyFraction
            f = PyFraction(float(val)).limit_denominator(1000000)
            return Fraction(f.numerator, f.denominator)

    # update_entry
    #
    # Purpose: Update the entry display with the given value, formatted according to the selected mode.
    # Parameters: value (str or float or Fraction)
    # Return: None
    def update_entry(self, value):
        self.entry_value.delete(0, tk.END)
        display_str = self.format_value(value)
        self.entry_value.insert(0, display_str)

    # update_display
    #
    # Purpose: Update the display after changing the display format radio button.
    # Parameters: None
    # Return: None
    def update_display(self):
        current_display = self.entry_value.get()
        self.update_entry(current_display)

    # format_value
    #
    # Purpose: Format the given value according to the selected display format (normal, scientific, percentage).
    # If fraction_mode is on and value is a fraction/mixed number, always show fraction form.
    # Parameters: value (float/Fraction/MixedNumber)
    # Return: str
    def format_value(self, value):
        # If fraction_mode and value is fraction or mixed number, show fraction as fraction:
        if self.fraction_mode and (isinstance(value, Fraction) or isinstance(value, MixedNumber)):
            return str(value)

        # Otherwise, convert to float for formatting
        try:
            if isinstance(value, Fraction):
                val_float = value.numerator / value.denominator
            elif isinstance(value, MixedNumber):
                val_float = (value.whole * value.denominator + value.numerator) / value.denominator
            else:
                val_float = float(value)
        except:
            return str(value)

        fmt = self.display_format.get()
        if fmt == 'normal':
            if val_float.is_integer():
                return str(int(val_float))
            else:
                return str(val_float)
        elif fmt == 'scientific':
            return f"{val_float:.6e}"
        elif fmt == 'percentage':
            return f"{val_float*100:.2f}%"
        else:
            return str(val_float)

    # display_error
    #
    # Purpose: Display an error message in the entry field.
    # Parameters: message (str)
    # Return: None
    def display_error(self, message):
        self.entry_value.delete(0, tk.END)
        self.entry_value.insert(0, message)
        self.error = True

    # reset_calculator
    #
    # Purpose: Reset the calculator to its initial state.
    # Parameters: None
    # Return: None
    def reset_calculator(self):
        self.current = ''
        self.total = None
        self.operator = ''
        self.error = False
        self.update_entry('')

    # square
    #
    # Purpose: Compute the square of the given value.
    # Parameters: val (float/Fraction)
    # Return: float/Fraction
    def square(self, val):
        if isinstance(val, Fraction):
            return Fraction(val.numerator**2, val.denominator**2)
        else:
            return float(val) ** 2

    # cube
    #
    # Purpose: Compute the cube of the given value.
    # Parameters: val (float/Fraction)
    # Return: float/Fraction
    def cube(self, val):
        if isinstance(val, Fraction):
            return Fraction(val.numerator**3, val.denominator**3)
        else:
            return float(val) ** 3

    # sqrt
    #
    # Purpose: Compute the square root of the given value.
    # Parameters: val (float/Fraction)
    # Return: float
    def sqrt(self, val):
        if isinstance(val, Fraction):
            val = val.numerator / val.denominator
        return math.sqrt(float(val))

    # cbrt
    #
    # Purpose: Compute the cube root of the given value.
    # Parameters: val (float/Fraction)
    # Return: float
    def cbrt(self, val):
        if isinstance(val, Fraction):
            val = val.numerator / val.denominator
        return float(val)**(1/3)

    # factorial
    #
    # Purpose: Compute the factorial of the given value.
    # Parameters: val (float/Fraction)
    # Return: float
    def factorial(self, val):
        if isinstance(val, Fraction):
            val = val.numerator / val.denominator
        return math.factorial(int(val))

    # reciprocal
    #
    # Purpose: Compute the reciprocal (1/val) of the given value.
    # Parameters: val (float/Fraction)
    # Return: float/Fraction
    def reciprocal(self, val):
        if isinstance(val, Fraction):
            if val.numerator == 0:
                raise ZeroDivisionError
            return Fraction(val.denominator, val.numerator)
        else:
            val = float(val)
            if val == 0:
                raise ZeroDivisionError
            return 1/val

    # ten_pow
    #
    # Purpose: Compute 10 raised to the given value.
    # Parameters: val (float/Fraction)
    # Return: float
    def ten_pow(self, val):
        if isinstance(val, Fraction):
            val = val.numerator / val.denominator
        return 10**(float(val))


# Application run block
if __name__ == '__main__':
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
