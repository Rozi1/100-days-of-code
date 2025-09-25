from helper import logo, alphabet
def encode(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")
def decode(text, shift):
    decipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift) % 26
            new_letter = alphabet[new_position]
            decipher_text += new_letter
        else:
            decipher_text += letter
    print(f"The decoded text is {decipher_text}")   
