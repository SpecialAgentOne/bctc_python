# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# prog3.py

# Program 3 - Calculating the Factorial of a Number

# This program calculate the factorial

# Initializing variables
ERR = "\nPlease enter positive number and not 0!\n"     # Error message if user will type 0 or negative number
factorial = 1                                           # Initial factorial value

# Asking user for the number
user_number = int(input("Enter a nonnegative number: "))

# Catching error, if user decide to type "0" or negative number
while user_number <= 0:
    print(ERR)
    # Asking to type a proper nonnegative number
    user_number = int(input("Enter a nonnegative number: "))

# Program logic to calculate the factorial
for i in range(1, user_number + 1):
    factorial = i * factorial

# Output to print factorial accroing to the task
print(f"{user_number}! = {factorial}")