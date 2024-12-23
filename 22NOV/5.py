F = list()
for N in range(1,25):
    binN = bin(N)[2::]
    if N % 2 !=0:
        ansewer = '1' + binN + '10'
    else:
        ansewer = '10' + binN + '0111'
    F.append(int(ansewer,2))
print(max(F))

#Первичная проверка