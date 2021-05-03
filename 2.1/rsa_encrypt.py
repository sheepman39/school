#   a212_rsa_encrypt.py
import rsa as rsa


key = input("Enter the Encryption Key: " )

# step 11
# bEAuty of a while loop is that it checks the value of it AND repeats until it is correct
while not key.isdigit():
    key = input("Enter the Encryption Key (must be a number): " )

mod_value = input("Enter the Modulus: " )

while not mod_value.isdigit():
    mod_value = input("Enter the Modulus (must be a number): " )

plaintext = input("Enter a message to encrypt: ")

# once the values are correct, changes the string to integer
key = int(key)
mod_value = int(mod_value)

encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:", encrypted_msg)
