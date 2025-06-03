
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
stroka = "1"+"0"*33

while nashlos(stroka,1) or nashlos(stroka,100):
    if nashlos(stroka,100):
        stroka= zamenit(stroka,100,"0001")
    else:
        stroka = zamenit(stroka, 1, "00")
print(stroka.count("0"))