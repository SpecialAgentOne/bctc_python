num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

devider = 0

if num1 > num2:
    devider = num2
else:
    devider = num1

for i in range(devider, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
        break
print(f"The GCD of {num1} and {num2} is: {gcd}")