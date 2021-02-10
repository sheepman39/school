import binaryToHex as bH
import hexToBinary as hB
import binascii

conversion = input("Is this binary (b) to hex or hex to binary (h)? ")
while(conversion != "b" and conversion != "h"):
    conversion = input("Is this binary (b) to hex or hex to binary (h)?\n Please put down 'b' or 'h' ")

converting = input("Please put in what you want to be converted: ")
if(conversion == "b"):
    print("The answer is: " + bH.convert(converting))
elif(conversion == "h"):
    
    print("The answer is: " + str(bin(int(converting))[2:]))

