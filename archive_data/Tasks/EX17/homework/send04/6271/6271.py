''' 	(№ 6271) (А. Игнатюк) В файле 17-367.txt содержится последовательность натуральных чисел, не превышающих 10000.
Найдите самую длинную непрерывную цепочку чисел, в которой каждое число делится нацело хотя бы на одно из соседних чисел.
 Запишите в ответе сначала длину этой цепочки, а потом - сумму чисел в цепочке. '''

spisok = list()
with open("File") as file:
    line = file.readline().strip()

    while line!= "":






        spisok.append(int(line))
        line = file.readline().strip()





kolvo = list()
maxim = 0
summ = 0
for m in range(1, len(spisok) -2):
    if spisok[m] % spisok[m-1] == 0 or spisok[m] % spisok[m + 1] == 0:
        kolvo.append(spisok[m])
    else:
        if len(kolvo) > maxim:
            maxim = len(kolvo)
            summ = sum(kolvo)
        kolvo.clear()




print(maxim,summ)
