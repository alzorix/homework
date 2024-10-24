def zamenit(S, V, W):
    S = str(S)
    V = str(V)
    W = str(W)
    S = S.replace(V, W, 1)
    return S


def nashlos(S, V):
    S = str(S)
    V = str(V)
    return S.count(V)


for n in range(1, 100):
    stroka = "1" + "0" * n

    while nashlos(stroka, 10) or nashlos(stroka, 1):
        if nashlos(stroka, 10):
            stroka = zamenit(stroka, "10", "001")

        else:
            if nashlos(stroka, 1):
                stroka = zamenit(stroka, "1", "0")

    if len(str(len(stroka))) == 3:
        print(n)
        break
