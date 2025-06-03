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
def sumstr(strt):
    F = 0
    for i in range(len(strt)):
        F = F + int(strt[i])
    return F


stroka = "9"*96
while nashlos(stroka,22222) or nashlos(stroka,9999):
    if nashlos(stroka,22222):
        stroka = zamenit(stroka,22222,99)
    else:
        stroka = zamenit(stroka, 9999, 2)

print(stroka)