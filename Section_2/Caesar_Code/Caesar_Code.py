## Caesar_Code
def decrypt(text, key):
    result = ""

    for character in text:
        if character.isupper():
            result += chr((ord(character) - key - 65) % 26 + 65)
        else:
            result += chr((ord(character) - key - 97) % 26 + 97)
 
    return result