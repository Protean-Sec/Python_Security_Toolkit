import string
import random

chaos_characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
smoke_screen = random.choice(chaos_characters)
def Protean_encryption():
    print("Welcome to Protean Cipher! Let's encrypt your message with a unique twist!")
    
    message = input("Enter your message: ")
    protean_types = [658, 94, 65, 491, 68, 1, 15, 862, 131, 6, 448, 445]
    final_encryption = ""
    for i, letter in enumerate(message):
        key_index = i % len(protean_types)
        current_key = protean_types[key_index]

    
    for letter in message:
        encrypted_letter = chr((ord(letter) ^ current_key))
        fake_char = random.choice(chaos_characters)
        final_encryption += fake_char + encrypted_letter
    print(f"You entered: {message}")
    print(f"Your encrypted message is: {final_encryption}")
    
Protean_encryption()

