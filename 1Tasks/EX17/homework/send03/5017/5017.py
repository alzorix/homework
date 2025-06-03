''' 	(№ 5017) (П. Волгин) В файле 17-278.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от 0 до 1000.
 Определите сначала количество троек чисел, в которых хотя бы один из элементов троек больше,
 чем сумма всех цифр «3» в пятеричной записи всех чисел в файле, кратных 32, а затем максимальную из сумм таких троек.
 Под тройкой подразумевается три идущих подряд элемента последовательности. '''






element = 0
spisok = list()
with open("File") as file:
    line = file.readline().strip()
    while line!= "":
        if int(line) % 32 == 0:
            realline = int(line)
            while realline !=0:
                if realline%5 == 3:
                    element +=3
                realline =realline // 5



        spisok.append(int(line))
        line = file.readline().strip()

kolvo = 0
suumms = list()
for m in range( len(spisok) -2):
    if max(spisok[m : m+ 3]) > element:
        print(1)
        suumms.append(sum(spisok[m:m+3]))


print(len(suumms),max(suumms))

