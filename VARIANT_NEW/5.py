ans = list()
for N in range(1,10000):
    binN = bin(N)[2::]
    if N % 2==0:
        binN = "1"+binN + "00"
    else:
        binN = binN + bin(binN.count("1"))[2::]

    R = int(binN,2)
    if R >=205:
        ans.append((R,N))
ans.sort(key=lambda x:x[0])
#print(ans)
print(min(ans)[1])
#20