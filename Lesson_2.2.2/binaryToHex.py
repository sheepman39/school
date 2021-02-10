def convert(binary):
    final = 0
    repeats = 0
    if(not binary.isdigit()):
        return "Please put in a valid number"
    else:
        for i in range(len(binary)):
            
            if(int(binary[-i]) == 1):
                
                final += 2 ** repeats
            
            elif(int(binary[-i]) != 0):
                
                return "invalid binary"
            
            repeats += 1
                
        return str(final)
