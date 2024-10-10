# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# prog2.py

# Program 2 - Celsius to Fahrenheit Table

# This is a program that displays a table of the Celsius temperatures
# 0 degrees through 20 degrees and their Fahrenheit equivalents

# Initializing variables
start_celsius = 0       # Initial temperature in Celsius
end_celsius = 20        # Final temperature in Celsius

# Printing the header with styling
print("  Celsius    Fahrenheit")

# Calculating from C to F in loop
for celsius in range(start_celsius, end_celsius + 1):
    # Using the formula for converting a temperature from Celsius to Fahrenheit
    fahrenheit = (9/5) * celsius + 32 
    # Printing result for each calcualtion per line with style formating
    print(f"    {celsius:2}        {fahrenheit:6.1f}")
    # Adding degree to the next loop iteration
    celsius += 1