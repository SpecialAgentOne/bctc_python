# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# lab3OR.py

# Expected output according to the task for "OR"
# p   q   p⋁q
# -------------
# T   T    T
# T   F    T
# F   T    T
# F   F    F

# Print the header with styling
print("p", "q", "p\u22c1q", sep="   ")  # Header values for our table
print("-" * 13)     # Printing cool bars to style code in the header

# Variables initialization for the thruth table
index_shift = 0     # Initial index number to run through the loop to match True/False results
p = "TTFF"          # Values of True/False for "p" related with "q"
q = "TFTF"          # Values of True/False for "p" related with "p"

# "FOR" loop to print all possible values in range according to the task
for index_shift in range(4):
    # We check that at least one of the values ​​is True to print True statement by "if-elif-else"
    if p[index_shift] == "T" or q[index_shift] == "T":
        # If is True, printing the pair where we get True
        print(p[index_shift], q[index_shift], " T", sep="   ") 
        # Adding +1 to shift for the next letter in the table
        index_shift += 1
    else:
        # If is False, printing the pair where we get False
        print(p[index_shift], q[index_shift], " F", sep="   ")
        # Adding +1 to shift for the next letter in the table
        index_shift += 1