import random
import string

chars = " " + string.punctuation + string.digits +string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print("------------------------------------------------------------------------")
print()

your_msg = input("Enter a Message to encrypt: ")
cipher_msg = ''

# encryption

for ch in your_msg:
    indx = chars.index(ch)
    cipher_msg += key[indx]

print(f"Your Original Message: {your_msg}")
print(f"Encrypted Message: {cipher_msg}")

print("------------------------------------------------------------------------")
print()

# decryption

cipher_msg = input("Enter a Message to decrypt: ")
your_msg = ""

for ch in cipher_msg:
    indx = key.index(ch)
    your_msg += chars[indx]

print(f"Encrypted Message: {cipher_msg}")
print(f"Decrypted Message: {your_msg}")