import string
import random
def encrypt_message (message, shift):
    alphabet = "X7?#Y5L$*QWE9R_T@U!IOPASDF8G&HJKLZCVBNM123460%"
    shift = shift % len(alphabet)
    encrypted_message = ""
     
    for char in message:
      if char in alphabet:
        original_message = ""
        original_message = alphabet.find(char)
        new_position = (original_message + shift) % len(alphabet)
        new_char = alphabet[new_position]
        encrypted_message += new_char
    print("Encrypted message: " + encrypted_message)
       
print("Hello user! Let's encrypt your message using a simple Caesar Cipher!")
name = input("Enter your name:    ")
print("Welcome " + name.upper() + "! Let's get started!" + "\nEnter the message you want to encrypt:")
message = input("Message: ")
message = message.upper()

encrypt_message(message, 3)