from math import sqrt as koren
def delitelsdiender(num):
    go_back = set()
    t = int(koren(num) +1)

    for p in range(2,t):
        if num % p == 0:
            go_back.add(p)
            go_back.add(num//p)

    return sum(go_back)

c  = 0
num = 500_001
while True:
    R = delitelsdiender(num)

    if str(R)[-1] == "9":
        print(num,R)
        c+=1
    if c == 5:

        exit()

    num+=1
