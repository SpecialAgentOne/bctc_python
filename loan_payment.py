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
    # Check that rate is not negative
    if rate < 0:
        raise ValueError("Rate should be positive!")
    # Calculation according to the formula
    monthly_rate = rate / 12
    number_payments = years * 12
    p = (monthly_rate * principle) / (1 - (1 + monthly_rate) ** (-number_payments))
    return p

# Function to calculate total payments
# p = payment, 
# t = time in years
# T = total
# Formula is T = p * 12t
def totalOfPayments(rate, years, principle):
    # Calculation according to the formula
    p = payment(rate, years, principle)
    T = p * 12 * years
    return T

# Function to calculate interests
# P = amount borrowed (principle)
# T = total of payments
# I = interests
# Formula is I = T - P
def financeCharge(rate, years, principle):
    T = totalOfPayments(rate, years, principle)
    I = T - principle
    return I

# Function to show the results
def showResult(rate, years, principle):
    # Mapping of the values
    p = payment(rate, years, principle)
    T = totalOfPayments(rate, years, principle)
    I = financeCharge(rate, years, principle)
    # User output with calculated results
    print(f"Payments: {p:,.2f}")
    print(f"Finance Charge: {I:,.2f}")
    print(f"Total: {T:,.2f}")

# Main function to run program
def main():
    # User input for the values
    rate = float(input("Please enter loan rate: "))

    years = float(input("Please enter amount of years: "))
    # Check that years is not negative
    if years < 0:
        raise ValueError("Year should be positive!")
    
    principle = float(input("Please enter principle value: "))
    # Check that principle is not negative
    if principle < 0:
        raise ValueError(("Principle should be positive!"))
    
    # Output of the calculations to the user
    showResult(rate, years, principle)

# Check the function call
if __name__ == "__main__":
    main()