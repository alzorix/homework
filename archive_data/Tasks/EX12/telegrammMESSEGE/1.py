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
for x in range(1000,2000):

    S = "8" + "4"*x
    S2 = S

    while nashlos(S,"11")   or nashlos(S,"444") or nashlos(S,"8888") :

        S1 = S
        if nashlos(S,"11"):
            S = zamenit(S, "11", "4")

        if nashlos(S, "444"):
                S = zamenit(S, "444", "88")
        if nashlos(S,"8888"):
                S = zamenit(S, "8888", "1")
        if S1 == S:
            break

    F.append((zifrsum(S),S,S2))






print(max(F))
