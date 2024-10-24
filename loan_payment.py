# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# loan_payment.py

# This program calculate a loan payments based on a user data entry

# Function to calculate payments based on user input
# p = payment, 
# P = amount borrowed (principle)
# r = annual interest rate (as a decimal)
# t = time in years
# Formula is p = ((r/12) * P) / (1 - (1 + r/12)^-12t)
def payment(rate, years, principle):
    rate = float(input("Please enter loan rate: "))
    years = float(input("Please enter amount of years: "))
    principle = float(input("Please enter principle value: "))

    payment_calculated = ((rate/12) * principle) / (1 - (1 + rate/12)**(-12 * years))

    return payment_calculated

# Function to calculate total payments
# p = payment, 
# t = time in years
# T = total
# Formula is T = p * 12t
def totalOfPayments(rate, years, principle):
    


# Function to calculate interests
# P = amount borrowed (principle)
# T = total of payments
# I = interests
# Formula is I = T - P
def financeCharge(rate, years, principle):