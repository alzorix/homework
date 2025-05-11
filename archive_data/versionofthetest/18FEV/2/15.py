def mod(x,y):
    return x % y


for A in range(1,10000):
    F = True
    for x in range(1,1000):
        if ( (A + 2*x ) > (400 -A) ) and (( mod(A,100) + (mod(120,A) ))   >140     )     :
            None
        else:
            F = False
    if F:
        print(A)
        exit()

#221