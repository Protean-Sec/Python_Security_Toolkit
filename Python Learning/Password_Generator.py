import Password_Checker
import random
import string
import sys

def generate_password():
    # Everything below is indented, so it belongs to the function
    print("Hello user! Welcome to the Password Generator Program!" + "\nWhat's your name?")
    
    name = input("Enter your name:    ")
    print(name.upper())
    print("WAZZA " + name + "! " "Let's create a password!")
    
    try:
        Length = int(input("Enter desired password length (minimum 8 characters. NO EXCEPTIONS): "))
    except ValueError:
        print("That's not a number! defaulting to 8.")
        Length = 8

    include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    include_upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    include_lower = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    include_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

    character_pool = ""

    if include_lower:
        character_pool += string.ascii_lowercase
    if include_upper:
        character_pool += string.ascii_uppercase
    if include_numbers:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation
    
     
    if not character_pool:
        print("Bro you need to select at least one character type! Try again")
        sys.exit(1)

    generate_pass = ''.join(random.choices(character_pool, k=Length))
    print("---------------------------------\n")
    print("Your generated password is: " + generate_pass)

generate_password()