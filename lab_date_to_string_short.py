# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# lab_date_to_string_short.py

# This program reads a string from the user containing a date in the "mm/dd/yyyy" format
# and print the date in the format "Month Day, Year" like "April 20, 2024".

# This program use funcrion with nam "dateToString"
#   Purpose: Transfer date from one format to another
#   Parameters: User input like "mm/dd/yyyy"
#   Return: Print "April 20, 2024"   

# Function to perform convertation
def dateToString(date):
    # Dictionary to map month numbers to month names
    months = {
        "01": "January", "02": "February", "03": "March", "04": "April",
        "05": "May", "06": "June", "07": "July", "08": "August",
        "09": "September", "10": "October", "11": "November", "12": "December"
    }
    
    # Split the input date into parts
    month, day, year = date.split("/")
    
    # Convert the date to the desired format
    formatted_date = f"{months[month]} {int(day)}, {year}"
    
    return formatted_date

# User input
user_input = input("Enter a date in the form mm/dd/yyyy: ")

# Call the function and print the formatted date
print(dateToString(user_input))