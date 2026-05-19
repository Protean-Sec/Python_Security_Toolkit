import random
print("Hello user! Welcome to the Dice Roller Program!" + "\nWhat's your name?")
name = input("Enter your name:   ")
print(name.upper())
print ("Hey " + name + "! Let's roll a dice!")
dice_roll = random.randint(1, 6)
print("You rolled a " + str(dice_roll) + "!")
print("Would you like to roll again? (yes/no)")
input_choice = input().lower()

while input_choice == "yes":
    dice_roll = random.randint(1,6)
    print("You rolled a " + str(dice_roll) + "!")
    print("Roll again? (yes/no)")
    input_choice = input().lower()

    while input_choice == "no":
            print("Thank you for using the Dice Roller Program, " + name + "! Vielen Dank!")
         
            break


