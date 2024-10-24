'''(№ 6067) В файле 17-354.txt содержится последовательность целых чисел, по модулю не превышающих 10000.
Определите количество пар элементов последовательности, в которых запись большего из двух элементов заканчивается цифрой 2,
а сумма квадратов элементов пары меньше, чем квадрат наибольшего из всех элементов последовательности, запись которых заканчивается цифрой 9.
 В ответе запишите два числа: сначала количество найденных пар, затем максимальную сумму квадратов элементов этих пар. В данной задаче под парой
  подразумевается два идущих подряд элемента последовательности. '''

spisok = list()



naibposled = -float("inf")
with open("EX17/homework/send02/6067/File") as f:
    line = f.readline().strip()
    while line != "":
        line = int(line)
        if str(line)[-1] == "9" and line > naibposled:
            naibposled = line





        spisok.append(int(line))
        line = f.readline().strip()

KVADRATNAIB = naibposled **2
good = list()
for m in range( len(spisok) -1):
    Bspisok = None
    Nspisok = None
    if spisok[m] > spisok[m+1]:
        Bspisok = spisok[m]
        Nspisok = spisok[m + 1]
        print(1)
    elif spisok[m] == spisok[m+1]:
        None
    else:
        Bspisok = spisok[m + 1]
        Nspisok = spisok[m]

    if Bspisok != None:
        if str(Bspisok)[-1] == "2":
            if Bspisok **2 + Nspisok**2 < KVADRATNAIB:
                good.append(Bspisok **2 + Nspisok**2)




    else:
        break





print(len(good),max(good))
