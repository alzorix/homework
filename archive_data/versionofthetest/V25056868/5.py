

for N in range(0,5000):
    binN = bin(N)[2::]
    #print(binN)

    if sum(map(int,binN.split())) % 2 == 0:



        binN = "10"+binN[2::]+"0"
    else:
        binN = "1" + binN[::2] + "11"
    R = int(binN,2)
    if R > 50:
        print(N)
        break


#17