# Validation of input
# 1. Username no more than 12 chars
# 2. Username must not contain spaces
# 3. Username must not contain digits

username = input("Please input your user name: ")

msg_error_len = "Username must be less than 12 characters!"
msg_error_spaces = "Username must be without spaces!"
msg_error_digits = "Username must be without digits"

def check_checkusername(value):
    while len(value) > 12:
        return msg_error_len
        value = input("Please input your user name: ")
    while value.find(" ") != -1:
        return msg_error_spaces
        value = input("Please input your user name: ")
    while value.isdigit():
        return msg_error_digits
        value = input("Please input your user name: ")
        
    return value
    
valid_username = check_checkusername(username)

print(f"Your username is {valid_username}")