user_input = int(input("Enter amount of the total square feets: "))
sqft_in_acre = 43560
acres = user_input / sqft_in_acre

print("Your land size is: ", f"{acres:.2f}")