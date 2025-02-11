#   This program should use the Fraction and MixedNumber
#   classes and test their add() and subtract() methods
# 
#   Try several values to test, including adding a Fraction
#   to a MixedNumber. The code below is merely an example of
#   how the add() and subtract() methods are to be used.

from fraction import Fraction
from fraction import MixedNumber

def main():
    frac1 = Fraction(1, 2)  # 1/2
    frac2 = Fraction(1, 4)  # 1/4
    frac1.add(frac2)        # adds frac2 to frac1, so frac1 should be 3/4
    print(f"After adding frac2 to frac1: {frac1}")
    
    frac1.subtract(frac2)   # subtracts frac2 from frac1, so frac1 should be 1/2
    print(f"After subtracting frac2 from frac1: {frac1}")

    mn1 = MixedNumber(1, 2, 3)  # 1 2/3
    mn2 = MixedNumber(2, 1, 6)  # 2 1/6
    mn2.add(mn1)                # adds mn1 to mn2, so mn2 should be 3 5/6
    print(f"After adding mn1 to mn2: {mn2}")
    
    mn2.subtract(mn1)           # subtracts mn1 from mn2, so mn2 should be 2 1/6
    print(f"After subtracting mn1 from mn2: {mn2}")

if __name__ == '__main__':
    main()
