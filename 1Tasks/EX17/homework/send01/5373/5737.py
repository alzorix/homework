'''(№ 5373) (ЕГЭ-2022) В файле 17-339.txt содержится последовательность целых чисел. Элементы последовательности могут
 принимать целые значения от –100 000 до 100 000 включительно. Определите количество пар последовательности, в которых сумма
 элементов меньше минимального положительного элемента последовательности, кратного 19. Гарантируется. что такой элемент в последовательности есть.
 В ответе запишите количество найденных пар, затем абсолютное значение максимальной из сумм элементов таких пар. В данной задаче под парой подразумевается
  два идущих подряд элемента последовательности. '''

spisok = list()
min= float("inf")
with open("EX17/homework/send01/5191/file.txt") as file:
    line = file.readline().strip()
    while line != "":
      line = int(line)



      if line > 0 and line<min and line % 19 == 0:
            min = line


      spisok.append(int(line))
      line = file.readline().strip()




abslokute = list()
kolvo = 0
for m in range( len(spisok) -1):
    if spisok[m] + spisok[m + 1] < min:
        kolvo += 1
        abslokute.append(spisok[m] + spisok[m + 1])


print(kolvo,max(abslokute))

