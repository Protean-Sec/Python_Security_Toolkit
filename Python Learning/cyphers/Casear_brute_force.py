import string
import Text_utilits

common_words = Text_utilits.common_words
alphabet = Text_utilits.alphabet
total_common_words = len(common_words)

def decrypt_one_attempt(encrypted_text, shift):
    alphabet_length = len(alphabet)
    

    decrypted_attempt = ""
    
    for char in encrypted_text:
        if char in alphabet:
            original_index = alphabet.find(char)
            new_position = (original_index - shift) % alphabet_length
            decrypted_attempt += alphabet[new_position]
        else:
            decrypted_attempt += char
            
    return decrypted_attempt


def crack_caesar_cipher(encrypted_text):
    print("----- CRACKING IN PROGRESS -----")
    
    best_score = -1
    best_shift = -1
    best_decryption = ""
    
    
    for shift in range(len(alphabet)):
        
        
        current_text = decrypt_one_attempt(encrypted_text, shift)
        
        
        current_score = 0
        words = current_text.split() 
        print(f"Shift{shift:02}: {current_text}")

       
        for word in words:
            
            cleaned_word = word.strip(string.punctuation)
            if cleaned_word in common_words:
                current_score += 1

        
        if current_score > best_score:
            best_score = current_score
            best_shift = shift
            best_decryption = current_text
   
        if current_score > 0:
             confidence = current_score / len(words)
        else:
             confidence = 0.0    
        
        if confidence > 0.5:
            print(f"\n[!] EARLY SUCCESS AT SHIFT {shift}! STOPPING NOW.")
            break
    print("\n------- CRACK COMPLETE -------")
    print(f"Confidence Score: {best_score} matches")
    print(f"Likely Shift: {best_shift}")
    print(f"DECRYPTED MESSAGE: {best_decryption}")

 
secret_message = input("Enter the encrypted message: ")
secret_message = secret_message.upper()
crack_caesar_cipher(secret_message)