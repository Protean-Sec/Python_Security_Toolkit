import string
import sys
def decrypt_message (message, shift):
    alphabet = "X7?#Y5$*QWE9R_T@U!IOPASDF8G&HJKLZCVBNM123460% "
    shift = shift % len(alphabet)
    encrypted_message = ""
     
    for char in message:
      if char in alphabet:
        char_index = alphabet.find(char)
        new_position = (char_index - shift) % len(alphabet)
        new_char = alphabet[new_position]
        encrypted_message += new_char
    print("Decrypted message: " + encrypted_message)
       
print("Hello user! Let's decrypt your message using a simple Caesar Cipher!")
name = input("Enter your name:    ")
print("Welcome " + name.upper() + "! Let's get started!" + "\nEnter the message you want to decrypt:")
message = input("Message: ")
message = message.upper()

decrypt_message(message, 22)