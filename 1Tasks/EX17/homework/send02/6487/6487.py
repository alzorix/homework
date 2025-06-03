'''(№ 6487) В файле 17-370.txt содержится последовательность целых чисел, по модулю не превышающих 20000. Определите количество пар элементов последовательности, в которых
– только одно число четырёхзначное;
– сумма квадратов элементов пары делится нацело на минимальное трёхзначное число в последовательности, оканчивающееся на 3.
В ответе запишите сначала количество найденных пар, затем минимальную из сумм квадратов элементов таких пар. Под парой элементов подразумеваются два соседних элемента последовательности. '''

spisok = list()

super = float("inf")
with open("file") as f:
    line = f.readline().strip()
    while line != "":
        line= int(line)


        if str(abs(line))[-1] == "3" and len(str(abs(line))) == 3 and line < super:
            super = line

        spisok.append(line)
        line = f.readline().strip()
yslovie= list()
good = list()
for m in range( len(spisok) -1):

    if (len(str(abs(spisok[m]))) ==4 or len(str(abs(spisok[m +1]))) == 4):
        if len(str(abs(spisok[m]))) ==4 and  len(str(abs(spisok[m +1]))) == 4:
            None
        else:

            a = spisok[m] ** 2 + spisok[m + 1] ** 2

            if a % super == 0:
                good.append(a)
print(good)
print(len(good),min(good))

