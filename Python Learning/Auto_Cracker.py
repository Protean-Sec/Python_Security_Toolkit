import string


alphabet = "X7?#Y5$*QWE9R_T@U!IOPASDF8G&HJKLZCVBNM123460% "

common_words = ["THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", 
                "CAN", "HIS", "HER", "WAS", "WITH", "ON", "AS", "BY", 
                "AT", "FROM", "THIS", "THAT", "OR", "BE", "THEY", "I", 
                "MY", "ME", "OF", "IN", "IS", "IT", "TO", "A", "AM",
                "WAS", "WERE", "HAD", "DO", "DID", "SO", "FOR", "UP", "DOWN",
                "LEFT", "RIGHT", "OVER", "UNDER", "BEHIND", "IN FRONT OF",
                "ABOVE", "BELOW", "NEAR", "FAR", "BETWEEN", "AMONG", "THROUGH",
                "ACROSS", "AROUND", "TOWARDS", "AWAY FROM", "OUT OF", "INTO",
                "ONTO", "OFF", "OVER", "UNDER", "BEHIND", "IN FRONT OF",
                "LORD", "GOD", "KING", "QUEEN", "PRINCE", "PRINCESS", "DUKE", "DUCHESS",
                "SIR", "LADY", "MR", "MRS", "MS", "DR", "PROFESSOR", "DOCTOR", "CAPTAIN", "SERGEANT", "PRIVATE",
                "POLICE", "FIRE", "EMT", "TEACHER", "STUDENT", "WORKER", "BOSS", "EMPLOYEE",
                "FRIEND", "FAMILY", "LOVER", "ENEMY", "NEIGHBOR", "COLLEAGUE", "STRANGER",
                "ANIMAL", "PET", "DOG", "CAT", "BIRD", "FISH", "HORSE", "COW", "SHEEP", "PIG",
                "ALEX", "PROGRAMMER", "PYTHON", "IS", "NOT", "FLY","AWAY", "NOW",
                "LATER", "SOON", "NEVER", "ALWAYS", "SOMETIMES", "OFTEN", "RARELY", "USUALLY",
                "HAPPY", "SAD", "ANGRY", "EXCITED", "BORED", "TIRED", "SCARED", "CONFUSED", "SURPRISED", "DISGUSTED",
                "LOVE", "HATE", "LIKE", "DISLIKE", "ADORE", "DESPISE", "RESPECT", "FEAR", "TRUST", "ENVY"
                "SMILE", "FROWN", "LAUGH", "CRY", "SHOUT", "WHISPER", "SING", "DANCE", "RUN", "WALK"
                "HELLO", "GOODBYE", "PLEASE", "THANK", "SORRY", "YES", "NO", "MAYBE", "ALRIGHT", "OKAY"
                "DAY", "NIGHT", "MORNING", "AFTERNOON", "EVENING", "WEEK", "MONTH", "YEAR", "TIME", "HOUR"
                "SHALL", "WILL", "MUST", "CAN", "COULD", "MAY", "MIGHT", "WOULD", "SHOULD", "DID", "SUCCEDED", 
                "FAILED", "WIN", "LOSE", "VICTORY", "DEFEAT", "SUCCESS", "FAILURE", "TRIUMPH", "DISASTER", "SUCCEED"]
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