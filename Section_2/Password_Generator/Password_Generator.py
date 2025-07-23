## PasswordGenerator_Code
import string
import secrets

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
alphabet = letters + digits + punctuation

def password_generator(password_length=12):

    password = ''
    
    while True:
        for _ in range(password_length):
            password += secrets.choice(alphabet)
            
        if any(character in punctuation for character in password) \
            and \
            sum(character in digits for character in password) >= 2:
            break
            
    return password
    
print(password_generator(20))