import string

alphabet = "X7?#Y5$*QWE9R_T@U!IOPASDF8G&HJKLZCVBNM123460% "
reversed_alphabet = alphabet [::-1]
def Atbash_encryption (message):
    
    encrypted_message = ""
     
    for char in message.upper():
      if char in alphabet:
        encrypted_message  += reversed_alphabet[alphabet.find(char)]
      else:
         encrypted_message += char
    return encrypted_message


print("Hello user! Let's encrypt your message using a simple Atbash Cipher!")
name = input("Enter your name:    ")
print("Welcome " + name.upper() + "! Let's get started!" + "\nEnter the message you want to encrypt:")
message = input("Message: ")
result = Atbash_encryption(message)
print("Encrypted message: ",  result)