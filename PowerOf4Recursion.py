
def pof4(n) :

    if n <= 0 :
        return False
    
    elif n == 1 :
        return True
    
    elif n % 4 == 0 :
        return pof4(n//4)

n = 612014

if pof4(n) :
    print("power of 4")

else :
    print("Not power of 4")
