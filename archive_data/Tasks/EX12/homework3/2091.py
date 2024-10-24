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

S = 50*"1" + 50*"2" + 50*"3"

while nashlos(S,"13")   or nashlos(S,"32") or nashlos(S,"12") :

        S1 = S
        if nashlos(S,"13"):
            S = zamenit(S, "13", "31")
        else:
            if nashlos(S, "32"):
                S = zamenit(S, "32", "23")
            else:
                S = zamenit(S, "12", "21")

        if S1 == S:
            break



print(S[10-1],S[70-1],S[140-1])

print(S)

