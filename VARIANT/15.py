for A in range(0,10000):
    F = True
    for x in range(0,10000):
        if ((x&52 != 0) and (x&48 ==0))  <= (not(x&A ==0)):
            None
        else:
            F = False
    if F:
        print(A)
        break

#4