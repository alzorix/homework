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





for n in range(0,10000):
    stroka = "1" + "7"*n
    while nashlos(stroka,17) or nashlos(stroka,377) or nashlos(stroka,777):
        if nashlos(stroka,17):
            stroka = zamenit(stroka,17,1)
        if  nashlos(stroka,377):
            stroka = zamenit(stroka, 377, 73)
        if nashlos(stroka,777):
            stroka = zamenit(stroka, 777, 3)

    if stroka.count("3") ==2:
        print(n)
        break






