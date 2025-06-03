def zamenit(S,V,W):
    S = str(S)
    V = str(V)
    W = str(W)
    S = S.replace(V,W)
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


ysl = 0
for n in range(3,10001):
    stroka = "5" + "2"*n
    while nashlos(stroka,52) or nashlos(stroka,2222) or nashlos(stroka,1122):
        if nashlos(stroka,52):
            stroka = zamenit(stroka,52,11)
        if  nashlos(stroka,2222):
            stroka = zamenit(stroka, 2222, 5)
        if nashlos(stroka,1122):
            stroka = zamenit(stroka, 1122, 25)

    if sumstr(stroka) ==64:
        ysl = n
print(ysl)



