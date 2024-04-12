import re
import secrets
import string
import time

# checks if input is a number and greater than 0
def check_input(message, var):
    counter = 0
    while True:
        inp = input(message)
        if inp.isnumeric() and int(inp) > 0:
            counter = 0
            var = int(inp)
            break
        else:
            break
    
    return var

# Gets new inputs or defaults
def get_inputs():
    length = 0
    nums = 1
    special_chars = 1
    uppercase = 1
    lowercase = 1

    print("Please enter your desired constraints: ")
    print("(Leave blank for default)")
    counter = 0
    while True:
        p_length = input("Enter desired password length: ")
        if p_length.isnumeric() and int(p_length) > 0:
            counter = 0
            length = int(p_length)
            break

    nums = check_input("Enter minimum amount of numbers: ", nums)
    special_chars = check_input("Enter minimum amount of special characters: ", special_chars)
    uppercase = check_input("Enter minimum amount of uppercase letters: ", uppercase)
    lowercase = check_input("Enter minimum amount of lowercase letters: ", lowercase)
    
    return length, nums, special_chars, uppercase, lowercase
    

def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_character = letters + digits + symbols

    length, nums, special_chars, uppercase, lowercase = get_inputs()
    while True:
        password = ''

        for _ in range(length):
            password += secrets.choice(all_character)
        constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars, rf'[{symbols}]')
            ]
        # Check Constraints
        # if the amount we want is <= the amount we have, break
        if (nums + lowercase + uppercase + special_chars) <= length:
            if all(constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints):          
                break
        else:
            print("TOO MANY CONSTRAINTS")
            time.sleep(2)
            length, nums, special_chars, uppercase, lowercase = get_inputs()
       
    return password


if __name__ == '__main__':
    new_password = generate_password()
    print("Generated password:", new_password)


