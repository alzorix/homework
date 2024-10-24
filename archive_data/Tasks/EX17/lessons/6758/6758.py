'''(№ 6758) (ЕГЭ-2023) В файле 17-380.txt содержится последовательность целых чисел, не превышающих по модулю 100 000.
Определите количество троек элементов последовательности, в которых не более двух из трёх элементов являются четырёхзначными числами,
 а сумма элементов тройки не больше максимального элемента последовательности, оканчивающегося на 25. В ответе запишите количество найденных троек чисел,
  затем максимальную из сумм элементов таких троек. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности. '''
mxelement = -float("inf")
spisok = list()
with open("F") as file:
    line = file.readline().strip()
    while line!= "":
        spisok.append(int(line))
        if line[-2::] == "25":
            if int(line) > mxelement:
                mxelement = int(line)
        line = file.readline().strip()
kolc= list()
for m in range(len(spisok) -2):
    if not ( len(str(abs(spisok[m]))) == 4 and len(str(abs(spisok[m + 1])))== 4 and len(str(abs(spisok[m + 2])))== 4 ) :
        if spisok[m] + spisok[m + 1 ] + spisok[m + 2 ]  <= mxelement:
            kolc.append(spisok[m] + spisok[m + 1 ] + spisok[m + 2 ])
print(len(kolc),max(kolc))