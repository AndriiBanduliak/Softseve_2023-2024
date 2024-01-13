import re


def is_valid_password(password):
    return 6 <= len(password) <= 16 and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in "$#@%" for c in password)

# Test with user input
user_password = input("Enter your password: ")
if is_valid_password(user_password):
    print("The password is valid.")
else:
    print("The password is invalid.")
