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
        if strt[i] != "<" and strt[i] != ">":
            F = F + int(strt[i])
    return F

for n in range(1,1000):
    stroka = ">2" + "12"*n + "<"

    while stroka.count(">2<") ==0:
        bad = stroka
        stroka = zamenit(stroka,">1",">2")
        stroka = zamenit(stroka, "12<", "1<2")
        stroka = zamenit(stroka, ">21", "1>")
        stroka = zamenit(stroka, "1<", "<2")
        if stroka ==bad:
            break


    if sumstr(stroka) >103:

        print(n)
        break
