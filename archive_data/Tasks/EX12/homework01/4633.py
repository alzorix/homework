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

a = set()
for n in range(2,100):
    stroka = "8"*n
    while nashlos(stroka,555) or nashlos(stroka,888):
            stroka = zamenit(stroka,555,8)
            stroka = zamenit(stroka, 888, 55)



    a.add(stroka)
print(len(a))

