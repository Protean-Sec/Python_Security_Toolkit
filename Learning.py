
print("Hello user! Welcome to the Basic Arithmetic Operations Program!" + "\nWhat's your name?")

name = input("Enter your name:  ")
print(name.upper())
print("Hello " + name + "! Let's begin!")
print("What basic aremtic operations would you like to perform today?")
Question =  input("Choose from Addition, Subtraction, Multiplication, Division or Power? ")
Answer = print("You chose " + Question)
#Getting user input for numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
#Performing calculations
add_numbers = x + y
subtract_numbers = x - y
multiply_numbers = x * y
divide_numbers = x / y
power_numbers = x ** y
#Displaying results based on user choice
if Question == "Addition":
    result = add_numbers
    print("Addition: " + str(add_numbers))

elif Question == "Subtraction":
    result = subtract_numbers
    print("Subtraction: " + str(subtract_numbers))

elif Question == "Multiplication":
    result = multiply_numbers
    print("Multiplication: " + str(multiply_numbers))

elif Question == "Division":
    result = divide_numbers
    print("Division: " + str(divide_numbers))
elif Question == "Power":
    print("Power: " + str(power_numbers))

elif Question != "Addition" or "Subtraction" or "Multiplication" or "Division" or "Power":
    print("Invalid operation. Please choose a valid operation next time.")
  
print("Thank you for using the basic arithmetic operations program, " + name + "! See ya")
#The str() function is used to convert numbers to strings for concatenation in print statements.
#Not bad for someone dealing with deppresion right?
