s = list()
for x in range(1,13):

    binN = bin(x)[2::]

    if x % 2 ==0:
        binN = "10"+binN
    else:
        binN = "1" + binN + "01"
    s.append(int(binN,2))
print(max(s))
#109