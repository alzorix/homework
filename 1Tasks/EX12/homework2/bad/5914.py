
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

    S   = 15*"3" + 18*"2" + n *"1"

    while nashlos(S,"31") or nashlos(S,"33") or nashlos(S,"21"):
     if nashlos(S,"31"):
        S = zamenit(S,"31","123")
     if nashlos(S,"33"):
        S = zamenit(S,"33","211")
     if nashlos(S,"21"):
        S = zamenit(S,"21","1")
    if zifrsum(S) >24:

            print(n)
            break
            #Где ошибка?