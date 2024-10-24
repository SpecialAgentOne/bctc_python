def main():
    # Open and create file
    ourfile = open('testnumbers.txt', 'w')

    # User numbers input
    user_number_1 = int(input('Please input the first number: '))
    user_number_2 = int(input('Please input the second number: '))
    user_number_3 = int(input('Please input the third number: '))

    # Values type change before write
    user_number_1 = str(user_number_1) + '\n'
    user_number_2 = str(user_number_2) + '\n'
    user_number_3 = str(user_number_3) + '\n'

    # Write the numbers to the file
    ourfile.write(user_number_1)
    ourfile.write(user_number_2)
    ourfile.write(user_number_3)

    # Close the file
    ourfile.close()
    print('Data writen to the file')

main()
