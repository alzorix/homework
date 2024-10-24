def universal(N, system):
    F = list()
    while N != 0:
        F.append(str(N % system))
        N = N // system
    F.reverse()
    return "".join(F)
def absolutesolver(N,s):
    F = list()
    while N !=0:
        F.append(str(N%s))
        N = N //s
    F.reverse()
    return "".join(F)
F1 = list()
for N in range(1,1000):
    R1 = absolutesolver(N,3)
    if N % 3 ==0:
        R = R1 + R1[-2::]
        #print(R1[-2::])
    else:
        R = R1 + absolutesolver(N//3*5,3)
    R = int(R,3)

    if  R> 133:
        F1.append(R)
print(min(F1))
