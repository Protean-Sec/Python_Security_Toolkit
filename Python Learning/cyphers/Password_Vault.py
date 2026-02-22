import hashlib
import Password_Checker
import re
def Password_Vault():
    print("Welcome to the Password Vault! Let's secure your passwords.")
    
    if not master_log_in():
       print("Acess denied. Unauthorized entry attempt recorded")
       return
         
        
    while True: 
        password = input("Enter your password: ")
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        score = check_password_strength(password)
        if score >= 4:
            print("Great! Your password is strong enough to be stored in the vault.")
            
        elif score <= 3:
            print("Your password is not strong enough to be stored in the vault. Please try again.")
            continue
        
        check = input("Do you want to store this password in the vault? (yes/no): ")

        if check.lower() == "yes":
                store_password(password_hash)
                print("Password stored securely in the vault.")
        else: print("Thank you for using Password Vault! Shutting down.")


        check = input("\nManage Vault: [V]iew, [E]rase, or [C]ontinue? ")
        if check.lower() == "v":
            retrieved_hashes = retrieve_password() 
            print(f"--- VAULT CONTENTS ---\n{retrieved_hashes}----------------------")
            break
        elif check.lower() == "e":
            confirm = input("Are you ABSOLUTELY sure? This wipes all data. (yes/no): ")
            if confirm.lower() == "yes":
                erase_vault()
                print("Vault wiped clean.")
                break
            else:         print("Phew! Vault remains intact.")
            break

        elif check.lower() == "c":
             second_password = input("Do you want to store another password? (yes/no): ")
             if second_password.lower() == "yes":
                continue
             
             else:
                print("Thanks for using Password Vault! Shutting down.")
                break
    

def store_password(p_hash):
    
    with open("password_vault.txt", "a") as file:
        file.write(p_hash + "\n")

def retrieve_password():
    with open("password_vault.txt", "r") as file:
        return file.read()
def erase_vault():
    with open("password_vault.txt", "w") as file:
        file.write("")
def check_password_strength(text):
    Password_Checker.check_password_strength(text)
    score = 0
    if len(text) >= 8:
        score += 1
        if any(char.isupper() for char in text):
            score += 1
        if any(char.islower() for char in text):
            score += 1
        if any(char.isdigit() for char in text):
            score += 1
        if any(not char.isalnum() for char in text):
            score += 1
    return score

def master_log_in ():
    attempts = 3
    MASTER_HASH_CONSTANT = "735392b496684c0933d78fac61066f690de198907fbe207e8eec8ddb44621c70"

    while attempts > 0:
        entered_password = input("Enter the master password to acess the vault:")
        guess_hash = hashlib.sha256(entered_password.encode()).hexdigest()
        if guess_hash == MASTER_HASH_CONSTANT:
            print("Acess granted! Welcome to the vault.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. You have {attempts} attempts left.")
     
            print("Acess deined")
    return False


Password_Vault()
