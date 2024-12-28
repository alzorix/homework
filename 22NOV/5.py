F = list()
for N in range(1,26): # Не превышающее,т.е. 25 вкл.
    binN = bin(N)[2::]
    if N % 2 !=0:
        ansewer = '10' + binN + '1' # Перепутал право и лево
    else:
        ansewer = '10' + binN + '0111'
    F.append(int(ansewer,2))
print(max(F))

#исправлено 2 ошибки
#1415