from math import  sqrt
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
def TRUEDIG(dig):
    sqrts = int(sqrt(dig))
    for i in range(2,sqrts+1):
        if dig % i == 0:
            return False
    return True



for n in range(1,1000):

    S = "0"  + n*"1" + n*"2" + "0"
    while not nashlos(S,"00"):

        S =zamenit(S,"02","101")

        S =zamenit(S,"11","2")

        S =zamenit(S,"12","21")

        S =zamenit(S,"010","00")
    R = zifrsum(S)

    if R > 400 and  TRUEDIG(R):
        print(n)
        break


