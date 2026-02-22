
def check_password_strength(password):
    checks = {
        "Length": len(password) >= 8,
        "Uppercase": any(char.isupper() for char in password),
        "Lowercase": any(char.islower() for char in password),
        "Number": any(char.isdigit() for char in password),
        "Symbols": any(not char.isalnum() for char in password)
    }

    score = sum(checks.values())
    if score == 5:
        print("Strong Password! Great Job!")
    elif score >= 3:
        print("Moderate Password. Consider adding more character types for better security.")
    else:
        print("Weak Password. Consider adding more characters or symbols.")

     
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
  