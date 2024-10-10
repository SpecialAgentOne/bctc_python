# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# lab3AND_while.py

# Expected output according to the task for "AND"
# p   q   p⋀q
# -------------
# T   T    T
# T   F    F
# F	  T	   F
# F	  F	   F

# Print the header with styling
print("p", "q", "p\u22c0q", sep="   ")  # Header values for our table
print("-" * 13)     # Printing cool bars to style code in the header

# Variables initialization for the thruth table
combinations = [(True, True), (True, False), (False, True), (False, False)]     # Possible pairs of combinations True/False
index = 0   # Index for the while loop

# Use a while loop to iterate through the combinations
while index < len(combinations):
    p, q = combinations[index]
    
    # Determine 'T' or 'F' for p and q
    p_value = 'T' if p else 'F'
    q_value = 'T' if q else 'F'
    
    # We check that all values ​​is True to print "True" statement by "if-elif-else"
    if p and q:
        result = 'T'
    else:
        result = 'F'
    
    # Print the result
    print(f"{p_value}   {q_value}    {result}")
    # Increment by +1 in index for the while loop
    index += 1