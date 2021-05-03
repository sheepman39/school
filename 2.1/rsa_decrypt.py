#   a212_rsa_decrypt.py
import rsa as rsa
# step 11
# bEAuty of a while loop is that it checks the value of it AND repeats until it is correct
key = input("Enter the decryption key: ")
while not key.isdigit():
    key = input("Enter the decryption Key (must be a number): " )

mod_value = input("Enter the Modulus: " )

while not mod_value.isdigit():
    mod_value = input("Enter the Modulus (must be a number): " )

encrypted_msg = input("Enter a message to decrypt: ")

# once the values are correct, changes the string to I N T E G E R
key = int(key)
mod_value = int(mod_value)


#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
print (rsa.decrypt(key,mod_value , msg))
