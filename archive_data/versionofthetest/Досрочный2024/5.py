for N in range(1,999):
    binN = bin(N)[2::]
    if N % 2 ==0:
        binN = binN + "01"
    else:
        binN = "1"+binN+"1"
    t = int(binN,2)
    if t >156:
        print(N)
        break