for N in range(1,10000):
    binN = bin(N)[2::]
    binN = binN+ str(binN.count("1")%2)
    binN = binN+ str(binN.count("1")%2)

    R = int(binN,2)
    if R >253:
        print(N)
        exit()
#64