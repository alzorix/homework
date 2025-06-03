'''(№ 5527) (М. Ишимов) В файле 17-345.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые — значения от 1 до 10 000 включительно.
 Определите количество пар последовательности, в которых только одно число меньше разности максимального и минимального из чисел последовательности, оканчивающихся на 52.
В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности. '''

spisok = list()



ma = -float("inf")
mi = float("inf")
with open("EX17/homework/send01/5191/file.txt") as f:
    line = f.readline().strip()
    while line != "":
        line = int(line)
        if str(line)[-2::] == "52":

            if line < mi:
                mi = line
            if line > ma:
                ma = line


        spisok.append(int(line))
        line = f.readline().strip()


maxmin = ma - mi


summ = list()
kolvo = 0
for m in range( len(spisok) -1):

    if spisok[m]  < maxmin:


            if  spisok[m + 1]  < maxmin:
                None
            else:
                kolvo +=1
                summ.append(spisok[m] + spisok[m+1] )
    if spisok[m+1]  < maxmin:


            if  spisok[m]  < maxmin:
                None
            else:
                kolvo +=1
                summ.append(spisok[m] + spisok[m + 1])



print(kolvo,max(summ))