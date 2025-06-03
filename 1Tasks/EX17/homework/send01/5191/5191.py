'''(№ 5191) (М. Шагитов) В файле 17-304.txt содержится последовательность целых чисел. Элементы последовательности могут
 принимать целые значения от 0 до 10 000. Найдите все пары элементов последовательности, в которых произведение чисел пары в
  двоичной записи содержит сочетание цифр 101010, а сумма чисел пары больше, чем среднее арифметическое всех чисел в файле.
   В ответе запишите количество найденных пар, затем минимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности. '''

spisok = list()

with open("EX17/homework/send01/5191/file.txt") as sup:
    line = sup.readline().strip()
    while line != "":


      spisok.append(int(line))
      line = sup.readline().strip()


average = sum(spisok)/len(spisok)


summa = float("inf")
kolvo = 0
for m in range( len(spisok) -1):
    if spisok[m] + spisok[m + 1] > average:
     if "101010" in bin(spisok[m] * spisok[m + 1])[2::] :

            kolvo += 1
            if  spisok[m] + spisok[m + 1] < summa:
                summa = spisok[m] + spisok[m + 1]
print(kolvo,summa)

