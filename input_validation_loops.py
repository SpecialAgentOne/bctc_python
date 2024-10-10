def count_even_numbers():
    even_count = 0
    total_numbers = 0

    while True:
        user_input = input()

        # Check if the user entered 'stop'
        if user_input.lower() == 'stop':
            if total_numbers == 0:
                print("At least one accepted number must be provided.")
                continue
            else:
                break

        # Try to convert the input to an integer
        try:
            number = int(user_input)
            # Check if the number is between 0 and 100 (inclusive)
            if 0 <= number <= 100:
                total_numbers += 1
                # Check if the number is even
                if number % 2 == 0:
                    even_count += 1
            else:
                print("Only numbers between 0 and 100 are accepted.")
        except ValueError:
            # Catch non-integer inputs other than 'stop'
            print("Only numbers between 0 and 100 are accepted.")

    # Print the total count of even numbers
    print(f"{even_count}")

# Call the function to run the program
count_even_numbers()
