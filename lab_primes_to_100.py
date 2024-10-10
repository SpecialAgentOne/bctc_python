# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# lab_primes_to_100.py

# This program prints only the prime numbers from 2 to 100.
# A prime number is a number that is only evenly divisible by itself and 1. 
# For example, the number 5 is prime because it can only be evenly divided by 1 and 5. 
# The number 6, however, is not prime because it can be divided by 2 and 3 with no remainder.

# Function to determine that number is prime or not
def isPrime(number):

    # Checking that number is not a prime
    if number < 2:              # 1 and 0 are not prime
        return False            # Setting state to False, number not a prime

    # Check if number is divisible by something other than 1 or itself
    else:  
        # Check n from 2 to one less than number
        for n in range(2 , number):
            # Checking if remainder is "0" when divided by "n" means that "n" not prime
            if number % n == 0:
                return False    # Setting state to False, number not a prime
                break           # We are done; only need to find one other integer that divides number
        return True             # Setting state to True, number is a prime

# Ask user for a number and determine if it's prime or composite
number = int(input("Enter a positive integer: "))

# User output
if isPrime(number) == True:           # Deciding that our condition True or False
    print(f'{number} is prime')       # If True - it's a prime number
else: 
    print(f'{number} is composite')   # Else False - number not prime