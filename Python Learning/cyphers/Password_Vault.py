import hashlib

def Password_Vault():
    print("Welcome to the Password Vault! Let's secure your passwords.")
    
    
    while True:
        password = input("Enter your password: ")
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
       
        store_password(password_hash)
        print("Your password has been securely stored.")
        
       
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


Password_Vault()