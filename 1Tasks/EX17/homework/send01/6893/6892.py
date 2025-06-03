'''(№ 6893) (Н. Сафронов) В файле 17-385.txt содержится последовательность целых неотрицательных чисел, не превышающих 10000.
 Определите количество пар элементов последовательности, в которых каждое число больше максимального из тех элементов последовательности,
  сумма цифр которых минимальна. В ответе запишите два числа: сначала количество найденных пар, затем максимальную сумму цифр элементов таких пар.
   В данной задаче под парой подразумевается два идущих подряд элемента последовательности. '''

spisok = list()
naub = -float("inf")
with open("file.txt") as sup:
    line = sup.readline().strip()
    while line != "":


      spisok.append(int(line))

      if int(line) > naub:
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

