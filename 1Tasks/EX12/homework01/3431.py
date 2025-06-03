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

s = 0
stroka = "5"*500
while nashlos(stroka,555) or nashlos(stroka,333):
    if nashlos(stroka,333):
        stroka= zamenit(stroka,333,"5")
    else:
        stroka = zamenit(stroka, 555, "3")
        s +=3
print(s)