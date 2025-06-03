'''(№ 4692) В файле 17-243.txt содержится последовательность целых чисел. Элементы последовательности могут принимать
целые значения от 0 до 10 000 включительно. Определите количество пар чисел, в которых хотя бы один из двух элементов больше,
 чем наибольшее из всех чисел в файле, делящихся на 111, и хотя бы один элемент из двух оканчивается на 7. В ответе запишите два числа:
  сначала количество найденных пар, а затем – минимальную сумму элементов таких пар. В данной задаче под парой подразумевается два идущих
  подряд элемента последовательности. '''
spisok = list()
naub = -float("inf")
with open("17-386.txt") as sup:
    line = sup.readline().strip()
    while line != "":


      spisok.append(int(line))

      if int(line) > naub and  int(line) % 111 == 0:
          naub = int(line)
      line = sup.readline().strip()



summa = float("inf")
kolvo = 0
for m in range( len(spisok) -1):
    if spisok[m] > naub or spisok[m + 1] > naub:
        if spisok[m] % 10 == 7 or spisok[m + 1] % 10 == 7:
            kolvo += 1
            if  spisok[m] + spisok[m + 1] < summa:
                summa = spisok[m] + spisok[m + 1]
print(kolvo,summa)






