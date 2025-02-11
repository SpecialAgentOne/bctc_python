# Yury Bakaev (Project 3 - Classes)
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# fraction.py

#    Import math module to use GCD function
#    Usage, where x and y are integers:
#            gcd = math.gcd(x, y)

# Import for using GCD function from math module
import math

# Class for Fractions and calculations with denominator and numerator
class Fraction:
    # Class Fraction initialization
    def __init__(self, numerator, denominator):
        # Check that denominator is not equal to zero ((denominator != 0)
        if denominator == 0:
            # Error handling in case if denominator is zero (denominator == 0)
            raise ValueError("Denominator cannot be zero.") # Prevent division by zero
        # Assign values for numerator and denominator
        self.numerator = numerator
        self.denominator = denominator

    def set_denominator(self, den):
        # Check that denominator is not equal to zero ((denominator != 0)
        if den == 0:
            # Error handling in case if denominator is zero (denominator == 0)
            raise ValueError("Denominator cannot be zero.") # Prevent division by zero
        # Assign the value to denominator
        self.denominator = den

    def set_numerator(self, num):
        # Set numerator for the fraction
        self.numerator = num

    def get_denominator(self):
        # Set denominator for the fraction
        return self.denominator

    def get_numerator(self):
        # Get the numerator of the fraction
        return self.numerator

    def reduce(self):
        # Reducing the fraction to the simplest form
        gcd = math.gcd(self.numerator, self.denominator) # Getting the GCD
        self.numerator //= gcd
        self.denominator //= gcd
        # Handle negative denominators by moving the negative sign to the numerator
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def add(self, frac):
        # Operation to add another fraction to this fraction
        numerator = self.numerator * frac.denominator + frac.numerator * self.denominator # Add numerator
        denominator = self.denominator * frac.denominator
        # Updating the values for numerator and denominator
        self.numerator = numerator
        self.denominator = denominator
        # Simplification of the fraction
        self.reduce()

    def subtract(self, frac):
        # Operation to substract another fraction to this fraction
        numerator = self.numerator * frac.denominator - frac.numerator * self.denominator # Substract numerator
        denominator = self.denominator * frac.denominator
        # Updating the values for numerator and denominator
        self.numerator = numerator
        self.denominator = denominator
        # Simplification of the fraction
        self.reduce()

    def __str__(self):
        # Returning a string for the fraction representation
        if self.denominator == 1:
            return f"{self.numerator}" # Should be a whole number
        elif self.numerator == 0:
            return "0" # Getting zero (0)
        else:
            return f"{self.numerator}/{self.denominator}" # Getting a proper fraction

# Class for mixed numbers with a whole part and a fraction
class MixedNumber(Fraction):
    # Class MixedNumber initialization
    def __init__(self, whole, numerator, denominator):
         # Check that denominator is not equal to zero ((denominator != 0)
        if denominator == 0:
            # Error handling in case if denominator is zero (denominator == 0)
            raise ValueError("Denominator cannot be zero.") # Prevent division by zero
        # Assign the value to the whole number
        self.whole = whole
        # Calling the superclass/parent Fraction, we can reuse methods and attributes for numerator/denominator
        super().__init__(numerator, denominator)

    def setWhole(self, whole):
        # Setting the wole number from mixed number
        self.whole = whole

    def reduce(self):
        # Reducing the mixed number to its simplest available form
        super().reduce()
        # Adjust whole number and fraction part
        self.whole += self.numerator // self.denominator # Adding the ingeteger part to the whole
        self.numerator = self.numerator % self.denominator # Update numerator with the remainder
        # Handle negative numerator
        if self.numerator < 0 and self.whole > 0:
            self.numerator += self.denominator
            self.whole -= 1

    def add(self, frac):
        # Operation to add another fraction or mixed number to this mixed number
        # Convert self to improper fraction
        self.numerator += self.whole * self.denominator
        self.whole = 0  # Reset whole part
        # Convert frac to Fraction if it's a MixedNumber
        if isinstance(frac, MixedNumber):
            frac = Fraction(frac.whole * frac.denominator + frac.numerator, frac.denominator)
        # Add fractions
        super().add(frac)
        # Convert back to mixed number
        self.reduce()

    def subtract(self, frac):
        # Operation to substract another fraction or mixed number from this mixed number
        # Convert self to improper fraction
        self.numerator += self.whole * self.denominator
        self.whole = 0  # Reset whole part
        # Convert frac to Fraction if it's a MixedNumber
        if isinstance(frac, MixedNumber):
            frac = Fraction(frac.whole * frac.denominator + frac.numerator, frac.denominator)
        # Subtract fractions
        super().subtract(frac)
        # Convert back to mixed number
        self.reduce()

    def __str__(self):
        # Returning a string for the mixed number representation
        if self.whole == 0 and self.numerator == 0:
            return "0" # Zero
        elif self.numerator == 0:
            return f"{self.whole}" # Only whole numbers!
        elif self.whole == 0:
            return f"{self.numerator}/{self.denominator}" # Only fractions!
        else:
            return f"{self.whole} {self.numerator}/{self.denominator}" # Getting the mixed number!
