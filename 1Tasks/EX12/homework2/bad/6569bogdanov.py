from math import sqrt
def zamenit(S,V,W):
    S = str(S)
    V = str(V)
    W = str(W)
    S = S.replace(V,W,1)
    return S
def nashlos(S,V):
    S = str(S)
    V = str(V)
    return S.count(V)
def zifrsum(S):
    S = str(S)
    F = 0
    for i in S:
        F = F + int(i)
    return F
def TRUEDIG(dig):
    sqrts = int(sqrt(dig))
    for i in range(2,sqrts+1):
        if dig % i == 0:
            return False
    return True
for n in range(3,1000,2):
    if TRUEDIG(n):

        S   = ">" + "0"*21 +"1" *n + "2"*11
        while nashlos(S,">1") or nashlos(S,">2") or nashlos(S,">0"):
         if nashlos(S,">1"):
            S = zamenit(S,">1","22>")
         if nashlos(S,">2"):
            S = zamenit(S,">2","2>")
         if nashlos(S,">0"):
            S = zamenit(S,">0","1>")
        S = S[:-1:]

        if zifrsum(S) % n ==0:

            print(n)
            break
