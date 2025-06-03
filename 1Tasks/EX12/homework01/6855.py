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




ysl = 0
for n in range(3,1001):
    stroka = "1" + "2"*n
    while nashlos(stroka,12) or nashlos(stroka,322) or nashlos(stroka,222):
        if nashlos(stroka,12):
            stroka = zamenit(stroka,12,2)
        if  nashlos(stroka,322):
            stroka = zamenit(stroka, 322, 21)
        if nashlos(stroka,222):
            stroka = zamenit(stroka, 222, 3)

    if ysl < len(stroka):
        ysl = len(stroka)


print(ysl)



