def main():

    num_days = int(input('How many days? '))

    sales_files = open('sales_01.txt', 'w')

    for count in range(1, num_days + 1):
        sales = float(input(f'Enter amount sales for day #{count} '))

    sales_files.write(f'{sales} \n')

    sales_files.close()
    print("Data saved")

main()