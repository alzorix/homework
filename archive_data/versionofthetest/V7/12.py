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

F = list()
for x in range(4,10000):

    S = "1" + "9"*x

    while nashlos(S,"19")   or nashlos(S,"49") or nashlos(S,"999") :

        S1 = S
        if nashlos(S,"19"):
            S = zamenit(S, "19", "9")

        if nashlos(S, "49"):
                S = zamenit(S, "49", "91")
        if nashlos(S,"999"):
                S = zamenit(S, "999", "4")



        if S1 == S:
            break

    F.append((zifrsum(S), S))




print(max(F))
