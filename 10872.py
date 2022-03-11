n = int(input())

i = 1

def factorial(c): 
    global i 
    if i != 0:
        i *= c  
        if c == 1:
            print(i)
            return
        factorial(c - 1)
    else:
        print(1)

factorial(n)

