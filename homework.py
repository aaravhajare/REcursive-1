
def pof2(n) :

    if n <= 0 :
        return False
    
    elif n == 1 :
        return True
    
    elif n % 2 == 0 :
        return pof2(n // 2)
    
n = int(input("Enter a number"))

if pof2(n) :
    print("Power of 2")

else :
    print("NOt power of 2")