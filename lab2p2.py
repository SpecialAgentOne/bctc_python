num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

counter = num1

while counter <= num2:
    if counter % 2 == 0:
        if counter == num2 or counter == num2 - 1:
            print(counter)
        else:
            print(counter, end=", ")
    counter += 1