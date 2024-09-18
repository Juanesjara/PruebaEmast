def esPalindromo(palabra):  
    for i in range(0,int(len(palabra)/2)):
        if palabra[i]!=palabra[-i-1]:
            return False
        return True
    
    

    