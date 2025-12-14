import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#print(f"chars : {chars}")
#print(f"key : {key}")

#Encrypt

plain_text = input("Enter the text you want to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"The plain text is: {plain_text}")
print(f"The encrypted text is: {cipher_text}")

#Decrypt

cipher_text = input("Enter the text you want to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"The encrypted text is: {cipher_text}")
print(f"The plain text is: {plain_text}")

