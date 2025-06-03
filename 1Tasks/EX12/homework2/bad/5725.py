
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
def zifrsum(S):
    S = str(S)
    F = 0
    for i in S:
        F = F + int(i)
    return F

for n in range(1,1000):

    S   = ">" +  "1" * 22 +"2" *n + "3"*23

    while nashlos(S,">1") or nashlos(S,">2") or nashlos(S,">3"):
     if nashlos(S,">1"):
        S = zamenit(S,">1","2>")
     if nashlos(S,">2"):
        S = zamenit(S,">2","21>")
     if nashlos(S,">3"):
        S = zamenit(S,">3","11>")
    S = S[:-1:]

    if zifrsum(S) > 2023:
        print(n)
        break
