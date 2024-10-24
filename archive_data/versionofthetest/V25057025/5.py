minn = list()

for N in range(1,10000):
    binN = bin(N)[2::]
    binN = binN + str(binN.count("1") %2)
    binN = binN + str(binN.count("1") % 2)
    if int(binN,2)>123:
        minn.append(int(binN,2))
print(min(minn))
#126