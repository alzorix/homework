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

stepeni2 = list()
for i in range(0,500):
    stepeni2.append(2**i)


results = list()
for two in range(0,100):
    for one in range(0,100):
        s = "0" + "2"*two+ "1" *one
        s1 = s
        if len(s) >= 65:
         while nashlos(s, "01") or nashlos(s, "02"):

            s = zamenit(s, "02", 110)
            s = zamenit(s, "01", 2120)
         R = zifrsum(s)
         if R in stepeni2:
                results.append(zifrsum(s1))
print(min(results))