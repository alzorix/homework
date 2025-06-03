'''(№ 5209) (М. Шагитов) В файле 17-316.txt содержится последовательность целых чисел. Элементы последовательности - четырёхзначные натуральные числа.
Назовём два различных четырёхзначных числа хорошей парой, если их сумма является полным квадратом натурального числа.
Найдите все тройки элементов последовательности, в которых есть хотя бы одна хорошая пара, а среднее арифметическое всех чисел тройки больше,
 чем среднее арифметическое всех чисел в файле. В ответе запишите количество найденных троек,
  затем максимальную из сумм элементов таких троек. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности. '''
sp = list()
from math import sqrt
def noname(s,n):
    summ = s + n
    if sqrt(summ) == int(sqrt(summ)):

        return True
    else:
        return False


with open("File") as file:
    line = file.readline().strip()
    while line!= "":
        line= int(line)

        sp.append(line)
        line = file.readline().strip()
spis = list()
average  = sum(sp)/len(sp)
for i in range(len(sp) -2):
    if noname(sp[i], sp[i+1]) or noname( sp[i+1], sp[i+2]) or noname( sp[i], sp[i+2]):
        if (sp[i]+ sp[i+1]+ sp[i+2]) /3> average:
            spis.append(sp[i]+ sp[i+1]+ sp[i+2])
print(len(spis),max(spis))


        #sp[i] sp[i+1] sp[i+2]

    #Проверка сложна