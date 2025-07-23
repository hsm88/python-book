## MorseCode_Code
import string
import time
import winsound

letters = string.ascii_letters
digits = string.digits
valid_chars = letters + digits + " "

def morse_encoder(message):
    
    if not all(char in valid_chars for char in message):
        return "There is invalid charater(s) in message!"
    
    morse_codes= {
                    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
                    "e": ".", "f": "..-.", "g": "--.", "h": "....",
                    "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
                    "m": "--", "n": "-.", "o": "---", "p": ".--.",
                    "q": "--.-", "r": ".-.", "s": "...", "t": "-",
                    "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                    "y": "-.--", "z": "--..", "1": ".----", "2": "..---", 
                    "3": "...--", "4": "....-", "5": ".....", "6": "-....",
                    "7": "--...", "8": "---..", "9": "----.", "0": "-----",
                    " ": " "
                 }
    
    encoded_message = ""
    
    for character in message.lower():
        encoded_message += " " + morse_codes[character]
    
    print(encoded_message)
    
    for code in encoded_message:
        if code == ".":
            winsound.Beep(1000, 200)
        elif code == "-":
            winsound.Beep(1000, 600)
        else: # for space character
            time.sleep(0.2)
    
    return encoded_message
