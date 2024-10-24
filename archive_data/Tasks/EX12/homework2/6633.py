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
All = list()
nmin = float("inf")
Smax = -float("inf")



for n in range(108,1000,9):
    S = "5"*n
    while nashlos(S,"25") or nashlos(S,"35") or nashlos(S,"555"):
        while nashlos(S, "555") or nashlos(S, "11") or nashlos(S, "2"):
            if nashlos(S, "555"):
                S = zamenit(S,"555",1)
            if nashlos(S, "11"):
                S = zamenit(S,"11",25)
            if nashlos(S, "2"):
                S = zamenit(S,"2",5)


    if int(S) > Smax:

            nmin = n
            Smax = int(S)

print(nmin)




#Как правильно условие написать?
