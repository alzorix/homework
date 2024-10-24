'''(№ 6761) (А. Рогов) В файле 17-383.txt содержится последовательность целых чисел. Элементы последовательности могут
принимать целые значения от -10 000 до 10 000 включительно. Определите количество пар последовательности, в которых хотя
 бы одно число является двузначным, а сумма элементов пары не превышает максимальный двузначный элемент последовательности.
  В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности. '''
elementmax = -float("inf")
spisok = list()
with open("File.txt") as file:
    line = file.readline().strip()
    while line!= "":
        if len(str(abs(int(line)))) == 2 and int(line) > elementmax:
            elementmax = int(line)

        spisok.append(line)
        line =

kolvo = 0
suumms = list()
print(elementmax)
for m in range( len(spisok) -1):
        if len(str(abs(int(spisok[m + 1])))) == 2 or len(str(abs(int(spisok[m])))) == 2:


            if int(spisok[m + 1] )+ int(spisok[m]) <= elementmax:
                kolvo += 1
                suumms.append(int(spisok[m + 1] )+ int(spisok[m]))

print(kolvo,max(suumms))
