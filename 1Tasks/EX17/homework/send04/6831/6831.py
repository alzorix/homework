'''(№ 6831) (А. Богданов) В файле 17-384.txt содержится последовательность натуральных чисел.
 Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно. Определите количество элементов последовательности,
  которые больше любой суммы пары элементов, в которой ровно одно число двухзначное. В ответе запишите количество найденных элементов, затем минимальный из них.
   В данной задаче под парой подразумевается два идущих подряд элемента последовательности. '''
spisok = list()


with open("File") as file:
    line = file.readline().strip()
    while line!= "":
        line = int(line)


        spisok.append(int(line))
        line = file.readline().strip()

kolvo = list()
the_maximum = -float("inf")
for m in range( len(spisok) -1):
    if (len(str(spisok[m])) == 2  and len(str(spisok[m  +1 ])) !=2 ) or  (len(str(spisok[m])) != 2  and len(str(spisok[m  +1 ])) ==2 ):
        if the_maximum < (spisok[m] + spisok[m+ 1]):
            the_maximum = spisok[m] + spisok[m+ 1]

for m in range(len(spisok)):

        if   spisok[m]  > the_maximum:
            kolvo.append(spisok[m])
print(len(kolvo),min(kolvo))
