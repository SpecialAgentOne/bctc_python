# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# prog1.py

# Program 1 - Pennies for Pay

# This program calculates the amount of money a person earn over a period of time.
# From the desriprion, if persons salary is one penny for the first day, two pennies 
# for the second and double each next day.
# All output results in dollars.

# Initializing variables
ERR = "\nPlease enter positive number and not 0!\n"     # Error message if user will type 0 or negative number
pay_rate_pennies = 1                                    # Pay rate is one penny
total_pay_in_dollars = 0                                # Initital total salary in dollars

# Asking user for the number of days to be calculated
user_days = int(input("How many days? "))

# Catching error, if user decide to type "0" or negative number for the days
while user_days <= 0:
    print(ERR)
    # Asking user to input days again after error message
    user_days = int(input("How many days? "))

# Printing the header with styling
print("\nDay    Pay for Day")

# Program logic to calculate pay according to the days from user
# Using FOR loop to calculate pay per each day and total
for day in range(1, user_days + 1):
    # Convertation from pennies to dollars per day
    daily_pay_in_dollars = pay_rate_pennies / 100
    # Printing current's day pay with styling
    print(f"{day:2}      {daily_pay_in_dollars:6.2f}")
    # Adding current day to the total pay
    total_pay_in_dollars += daily_pay_in_dollars
    # Doubling the pay for the next day
    pay_rate_pennies = pay_rate_pennies * 2

# Printing the total pay at the end of period
if user_days == 1:
    print(f"\nTotal for {user_days} day is ${total_pay_in_dollars:.2f}")
else:
    print(f"\nTotal for {user_days} days is ${total_pay_in_dollars:.2f}")