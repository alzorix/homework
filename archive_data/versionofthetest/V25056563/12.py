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



F = list()
for n in range(3,10000):
    S = "1" + n * "2"
    Fl = True

    while nashlos(S,"12")   or nashlos(S,"322") or nashlos(S,"222") :

        S1 = S
        if nashlos(S,"12"):
            S = zamenit(S, "12", "2")

        if nashlos(S, "322"):
                S = zamenit(S, "322", "21")
        if nashlos(S, "222"):
                S = zamenit(S, "222", "3")

        if S1 == S:
            Fl = False
            break
    print(S)

    if Fl:
        temp = 0
        for i in S:
            temp  +=int(i)

        F.append(temp)



print(max(F))
#Быстро выводит ответ 17,но только если проверять значения до 1000.