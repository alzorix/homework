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




ysl = float("inf")
ysl1 = float("-inf")
for n in range(201,1000):
    stroka = "5"*n
    while nashlos(stroka,55555) :
            stroka = zamenit(stroka,55555,88)
            stroka = zamenit(stroka, 888, 555)

    print(n,stroka.count("5"))
    if ysl1 < stroka.count("5"):
        ysl1 = stroka.count("5")
        ysl = n
    elif ysl1 == stroka.count("5"):
        if n <ysl:
            ysl = n



print(ysl)

