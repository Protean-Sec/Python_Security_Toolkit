import Text_utilits
import Atbash
import string

 
common_words = Text_utilits.common_words
total_common_words = len(common_words)

def crack_atbash(message):
    decrypted_message = Atbash.Atbash_encryption(message)
    print(f"Attempting Atbash decryption..")
    print(f"Raw output: {decrypted_message}")
    words = decrypted_message.split()
    valid_word_count = sum(1 for word in words if word.strip(string.punctuation).upper() in common_words)
    
    confidence = valid_word_count / len(words) if words else 0
    if confidence > 0.5:
        return ("The decrypted message is: " + decrypted_message)
    else:
        return ("FAILURE: Unable to confidently decrypt the message.")
test_code = "FTB X&DXFX84L!GWX8CGOCFQQBC"
print(crack_atbash(test_code))