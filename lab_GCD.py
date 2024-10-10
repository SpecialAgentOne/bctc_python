# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# lab_GCD.py

# This program calculates the Greatest Common Divisor (GCD) of two integers,
# and prints the GCD on the screen.

# Our function to find the GCD
def GCD(n1, n2):
    # We assume that the initial GCD is 1
    gcd = 1

    # Set the limit to the smaller of the two numbers using a ternary operator
    limit = n1 if n1 < n2 else n2

    # Count variable to control the loop
    count = 1

    # Loop to find the GCD
    while count <= limit:
        # Check if both n1 and n2 are divisible by count without a remainder
        if n1 % count == 0 and n2 % count == 0:
            # Update GCD to the current count value if it divides both numbers
            gcd = count
        # Increment the count for the next iteration
        count += 1

    # Return the GCD value
    return gcd

# User input area
n1 = int(input("Enter an integer: "))
n2 = int(input("Enter another integer: "))

# Call the GCD function and store the result
gcd_result = GCD(n1, n2)

# Print the results to the user
print(f"GCD of {n1} and {n2} is {gcd_result}")