E = list()
def absolutesolver(N):

    F = list()

    while N !=0:

        F.append(str(N%3))
        N = N//3

    F.reverse()
    return "".join(F)
for N in range(1,1000):
  trueN = absolutesolver(N)
  if len(trueN)>=3: #Нужно ли здесь перепроверять есть ли в выражении 3 цифры?

    if N% 3 ==0:
        trueN = trueN+trueN[:3]
    else:
        s = sum(int(x) for x in trueN)
        s = s*5
        trueS = absolutesolver(s)
        trueN = trueN + trueS
    R = int(trueN,3)
    if R>2500:
        if R%2 !=0:
            E.append(R)
print(min(E))


#2521


