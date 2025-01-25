def toThree(num):
    F = list()
    while num !=0:
        F.append(str(num%3))
        num = num//3
    F.reverse()
    return "".join(F)

ans = list()
for N in range(1,100000):
    threeN = toThree(N)
    if N % 3 ==0:
        threeN = threeN + threeN[-2::]
    else:
        ss = 0
        for x in threeN:
            ss+=int(x)
        threeN = threeN+ toThree(ss)
    R = int(threeN,3)
    if R > 220 and R %2 ==0:
        ans.append(R)
print(min(ans))
#222
