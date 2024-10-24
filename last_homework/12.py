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


results = set()

for string in range(4,1000):
    string = "1" + "2"* string
    while nashlos(string,"12") or nashlos(string,"322") or nashlos(string,"222"):
        if nashlos(string,"12"):
            string = zamenit(string,"12","2")
        if nashlos(string,"322"):
            string = zamenit(string,"322","21")
        if nashlos(string,"222"):
            string = zamenit(string,"222","3")

    results.add(string.count("2"))
print(max(results))

