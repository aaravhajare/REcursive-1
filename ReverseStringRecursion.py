
def reverse_s(s) :

    l = len(s)

    if l == 1 :
        return s[0]
    
    firstchar = s[0]

    return reverse_s(s[1 :]) + firstchar

s = "AARAV"
print(reverse_s(s))
