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

from math import sqrt

results = list()
for two in range(0,100):
    for one in range(0,100):
        s = "0"  + "1" *one+ "2"*two
        s1 = s
        if len(s) >= 70:

            while nashlos(s,"01") or  nashlos(s,"02"):

                s = zamenit(s,"02",1110)
                s= zamenit(s,"01",2210)

            R = zifrsum(s)

            if sqrt(R) == int(sqrt(R)):

                    results.append(zifrsum(s1))
print(min(results))