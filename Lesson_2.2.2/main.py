import binascii

conversion = input("Is this binary (b) to decimal or decimal to binary (d)? ")
while(conversion != "b" and conversion != "d"):
    conversion = input("Is this binary (b) to decimal or decimal to binary (d)?\n Please put down 'b' or 'd' ")

converting = input("Please put in what you want to be converted: ")
if(conversion == "b"):
    
    print("The answer is: " + str(int(converting,2)))

elif(conversion == "d"):
    
    print("The answer is: " + str(bin(int(converting))[2:]))

