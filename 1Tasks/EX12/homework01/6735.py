
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


for n in range(3,10001):
    stroka = "5" + "2"*n
    while nashlos(stroka,72) or nashlos(stroka,522) or nashlos(stroka,2222):
        if nashlos(stroka,72):
            stroka = zamenit(stroka,72,2)
        if  nashlos(stroka,522):
            stroka = zamenit(stroka, 522, 27)
        if nashlos(stroka,2222):
            stroka = zamenit(stroka, 2222, 5)


    if sumstr(stroka) ==63:
        print(n)
        break





