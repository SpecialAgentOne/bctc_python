# Yury Bakaev
# CS 115U: Intro to Computer Programming (19Z1 19Z2 19Z3)
# lab_date_to_string.py

# This program reads a string from the user containing a date in the "mm/dd/yyyy" format
# and print the date in the format "Month Day, Year" like "April 20, 2024".

# This program use funcrion with nam "dateToString"
#   Purpose: Transfer date from one format to another
#   Parameters: User input like "mm/dd/yyyy"
#   Return: Print "April 20, 2024"   

# Variable initialization
date = ""
error_month = "Month error, wrong format or data"
error_day = "Day error, wrong format or data"

# Function to perform convertation
def dateToString(date):
    # User input
    user_date = str(input("Please input date in format mm/dd/yyyy: "))

    # Check that user entered the right amount of numbers and in appropriate format
    while len(user_date) != 10:
        print("Input should be in format mm/dd/yyyy!")
        user_date = str(input("Please input date in format mm/dd/yyyy: "))

    # Slicing to get month value
    mm = user_date[0:2]
    # Slicing to get day value
    dd = user_date[3:5]
    # Slicing to get year value
    yyyy = user_date[6:10]

    # Converting month number to the text version 01 --> January
    mm = str(mm)
    if mm == "01":
        mm = "January"
    elif mm == "02":
        mm = "February"
    elif mm == "03":
        mm = "March"
    elif mm == "04":
        mm = "April"
    elif mm == "05":
        mm = "May"
    elif mm == "06":
        mm = "June"
    elif mm == "07":
        mm = "July"
    elif mm == "08":
        mm = "August"
    elif mm == "09":
        mm = "September"
    elif mm == "10":
        mm = "October"
    elif mm == "11":
        mm = "November"
    elif mm == "12":
        mm = "December"
    else:
        return error_month

    # Checking date range validity (acceptable from 01 to 31)
    if int(dd) <= 0 or int(dd) > 31:
        return error_day
    
    # Combining results in to one statement
    new_date_format = mm + " " + dd + ", " + yyyy
#    return transformed_date
#    return user_date
    return new_date_format

print(dateToString(date))