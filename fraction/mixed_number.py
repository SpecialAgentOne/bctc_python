# Proposed solution for Lab - MixedNumber Class
# CS 115U
# fraction.py

import math


# Represents a fraction with numerator and denominator
class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            self.denominator = 1

    # Purpose: Reduce the fraction by dividing both numerator and denominator by their GCD
    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd
        self.denominator //= gcd

    def __str__(self):
        if self.denominator == 1:
            return f"{self.denominator}"
        else:
            return f"{self.numerator}/{self.denominator}"

    ############################################
    # CHALLENGE -------> Can you implement an add function?
    ############################################
    # Parameter: frac is a Fraction object being added to this instance
    def add(self, frac):
        print(f"adding {frac} to {self}")  # remove this line when implementing

    ############################################
    # CHALLENGE -------> Can you implement a subtract function?
    ############################################
    # Parameter: frac is a Fraction object being subtracted from this instance
    def subtract(self, frac):
        print(f"subtracting {frac} from {self}")  # remove this line when implementing

    ############################################
    # This allows an f-string containing a Fraction object to use a format specifier
    ############################################
    def __format__(self, format_spec):
        return f"{str(self):{format_spec}}"


class MixedNumber(Fraction):
    def __init__(self, whole, numerator, denominator):
        self.whole = whole
        super().__init__(numerator, denominator)

    def setWhole(self, whole):
        self.whole = whole

    def reduce(self):
        super().reduce()
        if self.numerator > self.denominator:
            self.whole += self.numerator // self.denominator
            self.numerator = self.numerator % self.denominator

    ############################################
    # CHALLENGE -------> Can you implement an add function?
    #     If you do this right, you'll use the super class add in this add
    ############################################
    # Parameter: frac is a Fraction object being added to this instance
    def add(self, frac):
        print(f"adding {frac} to {self}")  # remove this line when implementing

    ############################################
    # CHALLENGE -------> Can you implement a subtract function?
    ############################################
    # Parameter: frac is a Fraction object being subtracted from this instance
    def subtract(self, frac):
        print(f"subtracting {frac} from {self}")  # remove this line when implementing

    def __str__(self):
        if self.numerator == 0:
            return f"{self.whole}"
        elif self.whole == 0:
            return super().__str__
        else:
            return f"{self.whole} {self.numerator}/{self.denominator}"


def main():
    frac = Fraction(4, 6)
    frac.reduce()
    print(frac)

    mn = MixedNumber(2, 5, 4)
    print(mn)
    mn.reduce()
    print(f"reduced: {mn}")

    isFraction = isinstance(frac, Fraction)
    print(f"{frac:6} is-a Fraction: {isFraction}")

    isFraction = isinstance(mn, Fraction)
    print(f"{mn:6} is-a Fraction: {isFraction}")

    isMixedNumber = isinstance(frac, MixedNumber)
    print(f"{frac:6} is-a MixedNumber: {isMixedNumber}")

    isMixedNumber = isinstance(mn, MixedNumber)
    print(f"{mn:6} is-a MixedNumber: {isMixedNumber}")


if __name__ == "__main__":
    main()
