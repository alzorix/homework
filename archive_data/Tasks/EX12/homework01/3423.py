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





stroka = "4" + "6"*79+"4"
while nashlos(stroka,63) or nashlos(stroka,664) or nashlos(stroka,6665):
        if nashlos(stroka,63):
            stroka = zamenit(stroka,63,4)

        elif  nashlos(stroka,664):
            stroka = zamenit(stroka, 664, 5)
        elif nashlos(stroka,6665):
            stroka = zamenit(stroka, 6665, 3)


print(stroka)

