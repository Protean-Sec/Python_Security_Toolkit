print("Hello user! Welcome to the Password Strength Checker Program!" + "\nWhat's your name?")
name = input("Enter your name:  ")
print(name.upper())
print("Greetings " + name + "! " "Let's test your password strength!")
print("Please enter a password to check its strength.")
password = input("Enter your password: ")
Length = len(password)
Uppercase = any(char.isupper() for char in password)
Lowercase = any(char.islower() for char in password)
Number = any(char.isdigit () for char in password)
Symbols = any(not char.isalnum() for char in password)

if Length >= 8 and Uppercase and Lowercase and Number and Symbols:
    print("Strong Password! Your password meets all the criteria.")
elif Length >= 7 and (Uppercase or Lowercase) and Number and not Symbols: 
    print("Weak Password. Consider adding more characters or symbols for a stronger password.")
elif Length < 7 and (Uppercase or Lowercase) and Number and not Symbols:
    print("Very weak Password. Try to use at least 7 characters, including numbers and symbols.")
elif Length <= 5 and (not Uppercase and Lowercase) and not Number and not Symbols:
    print("Extremely Weak Password. Your password is too short and lacks variety. Use at least 6 characters with a mix of letters and numbers.")
elif Length and (Uppercase and not Lowercase) and not Number and not Symbols:
    print("Weak Password bro. Try to include lowercase letters and mix it with  numbers and/or symbols.")
else: 
    print("SUPER MEGA WEAK Password. At least try bro :(, including uppercase letters, lowercase letters, numbers, and symbols.")
print("Want to try again? (yes/no)")
input_choice = input().lower()
if input_choice == "yes":
    print("Restart the program to try again!")
else: 
    print("Thank you for using the Password Strength Checker Program, " + name + "! Stay safe!")
  