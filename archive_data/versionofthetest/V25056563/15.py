def D(x):
    return 17<=x<=58
def C(x):
    return 29<=x<=80
S = list()
for A1 in range(0,1000):
    for A2 in range(A1,A1+1000):
        F = True
        for x in range(1,1000):
            if D(x) <= (((not(C(x))) and (not(A1<=x<= A2))) <= (not(D(x)))):
                None
            else:
                F = False
                break
        if F:
            S.append(A2-A1+1)
print(min(S))

#12