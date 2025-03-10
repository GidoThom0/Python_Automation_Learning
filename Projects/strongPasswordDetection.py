import re

def is_strong_password(password):
    # Regex patterns
    length_regex = r'.{8,}'  # At least 8 characters
    uppercase_regex = r'[A-Z]'  # At least one uppercase letter
    lowercase_regex = r'[a-z]'  # At least one lowercase letter
    digit_regex = r'\d'  # At least one digit

    # Check all conditions
    if (re.search(length_regex, password) and
        re.search(uppercase_regex, password) and
        re.search(lowercase_regex, password) and
        re.search(digit_regex, password)):
        return True
    else:
        return False
    
# Example usage
password = input('Enter a password: ')
print(is_strong_password(password))
