N = 0
f = -float("inf")
while N <=12:
    binN = bin(N)[2::]
    if binN.count("1") %2 ==0:
        binN = "10" +binN
    else:
        binN = "1" + binN + "01"



    if int(binN,2) > f:
        f = int(binN,2)
    N +=1
print(f)
