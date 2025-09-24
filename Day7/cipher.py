from helper import logo
from functions import encode, decode
print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()    
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encode(text, shift)
    elif direction == "decode":
        decode(text, shift)
    else:
        print("Invalid input. Please type 'encode' or 'decode'.")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        break
    elif restart == "yes":
        continue