
def check_password_strength(password):
    Length = len(password)
    Uppercase = any(char.isupper() for char in password)
    Lowercase = any(char.islower() for char in password)
    Number = any(char.isdigit() for char in password)
    Symbols = any(not char.isalnum() for char in password)

    if Length >= 8 and Uppercase and Lowercase and Number and Symbols:
        print("Strong Password! Your password meets all the criteria.")
    elif Length >= 7 and (Uppercase or Lowercase) and Number and not Symbols: 
        print("Weak Password. Consider adding more characters or symbols.")
    elif Length < 7 and (Uppercase or Lowercase) and Number and not Symbols:
        print("Very weak Password. Try to use at least 7 characters.")
    elif Length <= 5 and (not Uppercase and Lowercase) and not Number and not Symbols:
        print("Extremely Weak Password.")
    elif Length and (Uppercase and not Lowercase) and not Number and not Symbols:
        print("Weak Password bro. Try to include lowercase letters and numbers/symbols.")
    else: 
        print("SUPER MEGA WEAK Password. At least try bro :(")
    
if __name__ == "__main__":
    print("Hello user! Welcome to the Password Strength Checker Program!" + "\nWhat's your name?")
    name = input("Enter your name:  ")
    print(name.upper())
    print("Greetings " + name + "! " "Let's test your password strength!")
    
    password = input("Enter your password: ")
    check_password_strength(password)

    print("Want to try again? (yes/no)")
    input_choice = input().lower()
    while input_choice == "yes":
        password = input("Enter your new password for strength check: ")
        check_password_strength(password)
        input_choice = input("Try again? (yes/no)").lower()
        


  #The any() function is used to check for the presence of uppercase letters, lowercase letters, numbers, and symbols in the password.
  #The program evaluates the password based on length and character variety to determine its strength.
  