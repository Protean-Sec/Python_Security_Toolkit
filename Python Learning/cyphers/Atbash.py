import string

alphabet = "X7?#Y5$*QWE9R_T@U!IOPASDF8G&HJKLZCVBNM123460% "
reversed_alphabet = alphabet [::-1] # This creates a new string that is the reverse of the original alphabet string. 
#The slicing syntax [::-1] is used to reverse the order of the characters in the string.
def Atbash_encryption (message):
    
    encrypted_message = ""
    for char in message.upper():
      if char in alphabet:
        encrypted_message  += reversed_alphabet[alphabet.find(char)] # This line 
        #finds the index of the current character in the original alphabet string 
        # using alphabet.find(char) and then uses that index to get the corresponding character 
        # from the reversed_alphabet string. The resulting character is then added 
        # to the encrypted_message string.
      else:
         encrypted_message += char 
    return encrypted_message
if __name__ == "__main__":
    print("Hello user!  Let's encrypt your message using a simple Atbash Cipher!" + "\nWhat's your name?")
    name = input("Enter your name:  ")
    print(name.upper())
    print("Greetings " + name + "! " "Let's encrypt with Atbash Cipher!")

    print("Welcome " + name.upper() + "! Let's get started!" + "\nEnter the message you want to encrypt:")
    message = input("Message: ")
    result = Atbash_encryption(message)
    print("Encrypted message: ",  result)

