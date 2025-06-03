
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




Y = float("inf")
for n in range(401,1000):
    R =n
    S = "5"*n
    while  nashlos(S,"5555"):
        S = zamenit(S,5555,8)
        S = zamenit(S,88,5)
    if S.count("5") < Y:
        Y = S.count("5")
        R1 = R
print(R1)