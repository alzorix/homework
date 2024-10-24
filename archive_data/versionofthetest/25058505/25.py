from math import sqrt
def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(2,KOREN +1):
        if num % i == 0 :
            D.append(i)
            if num // i != i:
                D.append(num // i)
    D.sort()

    try:
        M = D[0] + D[-1]
    except:
        M = 0
    return  str(M)


n = 800001
c = 0
while True:
    M = simplegit(n)
    #print(M)
    if str(M)[-1] == "4":

        print(n,M)
        c+=1
    if c == 5:
        exit()
    n+=1

