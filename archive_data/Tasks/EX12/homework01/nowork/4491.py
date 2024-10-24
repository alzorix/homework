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

stroka = "3"*70
while nashlos(stroka,333) or nashlos(stroka,77777):
    if nashlos(stroka,333):
        stroka = zamenit(stroka,333,77)
    else:
        stroka = zamenit(stroka, 77777, 7)

print(sumstr(stroka))