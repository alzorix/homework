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





stroka = "3" + "5"*100+"3"
while nashlos(stroka,25) or nashlos(stroka,355) or nashlos(stroka,4555):

        if nashlos(stroka,25):
            stroka = zamenit(stroka,25,4)

        if  nashlos(stroka,355):
            stroka = zamenit(stroka, 355, 2)

        if nashlos(stroka,4555):
            stroka = zamenit(stroka, 4555, 3)


print(stroka)

