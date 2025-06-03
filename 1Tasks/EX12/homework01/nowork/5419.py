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



stroka = "7"*100
while nashlos(stroka,333) or nashlos(stroka,777):
    if nashlos(stroka,333):
        bad = stroka
        stroka = zamenit(stroka,333,77)
        if stroka == bad:
            break

    else:
        bad = stroka
        stroka = zamenit(stroka, 77777, 7)
        if stroka == bad:
            break

print(sumstr(stroka))