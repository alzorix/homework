def toThree(n):
    F = list()
    while n !=0:
        F.append(str( n % 3))
        n = n // 3
    F.reverse()
    return "".join(F)

for n in range(1,1000):
    threeN = toThree(n)
    if n % 2 ==0:
        threeN = "1" + threeN + "00"
    else:
        c = 0
        for x in threeN:
            c+= int(x)

        threeN = threeN + str(toThree(c))
    #print(threeN)
    if int(threeN,3) > 168:
        print(n)
        exit()
