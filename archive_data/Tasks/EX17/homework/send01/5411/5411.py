''' 	(№ 5411) (Е. Джобс) В файле 17-341.txt содержится последовательность целых чисел.
Элементы последовательности – целые числа, не превосходящие по модулю 10000. Найдите такие пары элементов,
в которых произведение элементов больше, чем произведение рядом стоящих чисел (перед и после пары).
В качестве ответа выведите максимальную сумму среди найденных пар, затем количество таких из этих пар,
 в которых есть хотя бы одно число, большее среднего арифметического всех чисел в файле. Под парой в задаче подразумевается два подряд идущих числа.
  Первая и последняя пара в файле не рассматриваются, так как перед ними (или после них) нет чисел. '''
spisok = list()

with open("EX17/homework/send01/5191/file.txt") as f:
    line = f.readline().strip()
    while line != "":
      spisok.append(int(line))
      line = f.readline().strip()


average = sum(spisok)/len(spisok)


summa = -float("inf")
kolvo = 0
sum = list()
for m in range( len(spisok) -1):
    try:
        if spisok[m] * spisok[m + 1] > spisok[m - 1] * spisok[m + 2]:


            if  spisok[m] + spisok[m + 1] > summa:
                summa = spisok[m] + spisok[m + 1]

            if spisok[m] > average or spisok[m + 1] > average:
                kolvo += 1
    except:
        None


print(summa ,kolvo)

