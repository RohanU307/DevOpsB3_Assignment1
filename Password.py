
import re

password = input("Input your password: ")


def check_password_strength(password):
    
    if len(password) < 8:  # Minimum length: The password should be at least 8 characters long
        return False
    
    if not re.search(r'[A-Z]', password):  # Contains uppercase
        return False
    
    if not re.search(r'[a-z]', password):  # Contains lowercase
        return False
    
    if not re.search(r'[0-9]', password):  # contains one digit
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password): # Contains one special character
        return False
    
    return True

Validity = check_password_strength(password)

if Validity:
    print("Valid Password.")
else:
    print("Invalid Password.")

if Validity:
    print("your password is Strong! ")
else:
    print("You password is weak!")
    