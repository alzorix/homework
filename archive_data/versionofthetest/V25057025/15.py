def DEL(n,m):
    return n % m ==0

for A in range(1,10000):
    E = True
    for x in range(1,1000):
        if DEL(x,33)<= ((not(DEL(x,A))) <= (not(DEL(x,242)))):
            None
        else:
            E = False
    if E:
        print(A)
#726