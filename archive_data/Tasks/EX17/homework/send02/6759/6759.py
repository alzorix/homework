'''(№ 6759) (ЕГЭ-2023) В файле 17-381.txt содержится последовательность целых чисел, не превышающих по модулю 100 000.
Определите количество пар последовательности, в которых только один из элементов является четырёхзначным числом,
 а квадрат суммы элементов пары не больше квадрата максимального элемента последовательности, являющегося четырёхзначным
  числом и оканчивающегося на 39. В ответе запишите количество найденных пар чисел, затем максимальную из сумм элементов таких пар.
   В данной задаче под парой подразумевается два идущих подряд элемента последовательности. '''

spisok = list()

super = float("inf")
with open("f") as f:
    line = f.readline().strip()
    while line != "":
        line= int(line)


        if str(abs(line))[-1] == "39" and len(str(abs(line))) == 4 and line > super:
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

            if a < super:
                good.append(a)
print(good)
print(len(good),min(good))