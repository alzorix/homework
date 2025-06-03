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

F = set()

for n in range(1,1000):

    S =  n*"1"
    while nashlos(S,"1111")   or nashlos(S,"222") or nashlos(S,"33") :

        S1 = S
        if nashlos(S,"1111"):
            S = zamenit(S, "1111", "333")
        else:
            if nashlos(S, "222"):
                S = zamenit(S, "222", "11")
            else:
                S = zamenit(S, "33", "2")

        if S1 == S:
            break

    F.add(S)
print(len(F))
#неправильный ответ




