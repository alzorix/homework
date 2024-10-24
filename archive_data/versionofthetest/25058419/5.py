f = set()
for N in range(9999):
    binN = bin(N)[2::]
    if binN.count("1") % 2 == 0:
        binN = binN + "11"
    else:
        binN = binN + "01"

    R = int(binN,2)
    f.add(R)

f =sorted(f)
for i in f:
    if i>= 61:
        print(i)
        exit()
#63