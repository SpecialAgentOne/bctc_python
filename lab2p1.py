num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

for i in range (num1, num2 + 1):
    if i % 2 == 0:
        if i == num2 or i == num2 -1:
            print(i)
        else:
            print(i, end=", ")