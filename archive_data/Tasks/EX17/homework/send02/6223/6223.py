'''(№ 6223) (А. Богданов) В файле 17-365.txt содержится последовательность целых чисел, по модулю не превышающих 10000. Найдите все пары соседних элементов, отвечающие условиям:
– только один из элементов пары заканчивается на 1;
– оба элемента пары (меньше максимального среднего значения пары) среди всех пар отвечающих предыдущему условию.
В ответе запишите два числа: сначала количество найденных пар, затем максимальный элемент из пар, которые содержат минимальный элемент из всех найденных пар. '''

spisok = list()

with open("Fike") as f:
    line = f.readline().strip()
    while line != "":
        line = int(line)
        spisok.append(int(line))
        line = f.readline().strip()



yslovie= list()

maxx = -float("inf")
for m in range( len(spisok) -1):

    if str(spisok[m])[-1] =="1" and str(spisok[m +1])[-1] !="1":

        if (spisok[m] + spisok[m +1]) /2 > maxx:
            maxx = (spisok[m] + spisok[m +1]) /2


        yslovie.append((spisok[m],spisok[m+ 1]))

    elif str(spisok[m + 1])[-1] =="1" and str(spisok[m])[-1] !="1":
        if (spisok[m] + spisok[m +1]) /2 > maxx:
            maxx = (spisok[m] + spisok[m +1]) /2
        yslovie.append((spisok[m],spisok[m+ 1]))

    else:
        None


minelement = float("inf")
print(yslovie)

kolvo = 0

maxelement = -float("inf")
for m in range( len(yslovie) ):
    if yslovie[m][0] < maxx and yslovie[m][1] < maxx:
        minelement = min(minelement,yslovie[m][0],yslovie[m][1])

        kolvo += 1

for m in range(len(yslovie)):
    if yslovie[m][0] < maxx and yslovie[m][1] < maxx:
       if minelement in yslovie[m]:
           maxelement = max(yslovie[m][0],yslovie[m][1],maxelement)






print(kolvo,maxelement)

#меньше максимального среднего значения ???
