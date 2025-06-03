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
        if i != ">":
            F = F + int(i)
    return F



GLA = True

for k in range(100,201):
    if GLA == True:

     for m in range(100,201):
       if GLA == True:

            S   = ">" + "0"*k + m*"1"
            T = 0

            while nashlos(S,">1") or nashlos(S,">2") or nashlos(S,">0"):
                T = S

                if nashlos(S,">1"):
                    S = zamenit(S,">1","20>")
                if nashlos(S,">2"):
                    S = zamenit(S,">2","00>")
                if nashlos(S,">0"):
                    S = zamenit(S,">0","10>")
                if S == T:
                    break

            if zifrsum(S) == 599:
                print(k)
                GLA = False
                break
