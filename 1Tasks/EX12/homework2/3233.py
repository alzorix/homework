
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

max = -float("inf")
for n in range(91,1000):
    S = "1"* n
    while nashlos(S,111):
        S = zamenit(S,111,2)
        S = zamenit(S,2222,333)
        S = zamenit(S,33,1)
    if S.count("1") > max:
            R = n
            max = S.count("1")
print(R)