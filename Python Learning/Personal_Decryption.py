import string
import sys
def decrypt_message (message, shift):
    alphabet = string.ascii_uppercase
    shift = shift % 26
    encrypted_message = ""
     
    for char in message:
      if char in alphabet:
        original_message = ""
        original_message = alphabet.find(char)
        new_position = (original_message - shift) % 26
        new_char = alphabet[new_position]
        encrypted_message += new_char
    print("Decrypted message: " + encrypted_message)
       
print("Hello user! Let's decrypt your message using a simple Caesar Cipher!")
name = input("Enter your name:    ")
print("Welcome " + name.upper() + "! Let's get started!" + "\nEnter the message you want to decrypt:")
message = input("Message: ")
message = message.upper()

decrypt_message(message, 3)