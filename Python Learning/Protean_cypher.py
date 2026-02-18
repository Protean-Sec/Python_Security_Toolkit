import string
import random

chaos_characters = string.ascii_uppercase + string.digits + string.punctuation + string.whitespace + string.ascii_lowercase
double_team = random.choice(chaos_characters)

def Protean_encryption(message):
    print("Welcome to Protean Cipher! Let's encrypt your message with a unique twist!")
    input("Enter whatever you wish to encrypt: ")
    message = ""
    print(f"Your message is: {message}")
    print(f"Your encryption key is: {double_team}")
    

