# Ask the user for the number of days, with validation
num_days = int(input("How many days? "))
while num_days <= 0:
    print("The number of days must be a positive integer.")
    num_days = int(input("Please enter a valid number of days: "))

# Initialize variables
pay_in_pennies = 1  # Initial pay is 1 penny
total_pay_in_pennies = 0

# Print the table header
print("\n  Day2Pay for Day")
print("  ------------------")

# Loop through each day to calculate the pay and total
for day in range(1, num_days + 1):
    # Convert pay for the day from pennies to dollars
    pay_in_dollars = pay_in_pennies / 100.0
    
    # Print the current day's pay
    print(f"  {day:2}       {pay_in_dollars:6.2f}")
    
    # Add the current day's pay to the total
    total_pay_in_pennies += pay_in_pennies
    
    # Double the pay for the next day
    pay_in_pennies *= 2

# Convert total pay from pennies to dollars
total_pay_in_dollars = total_pay_in_pennies / 100.0

# Print the total pay at the end
print(f"\nTotal for {num_days} days is ${total_pay_in_dollars:.2f}")