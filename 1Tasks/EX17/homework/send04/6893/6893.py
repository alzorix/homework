'''(№ 6892) (Н. Сафронов) В файле 17-385.txt содержится последовательность целых неотрицательных чисел, не превышающих 10000.
 Определите количество пар элементов последовательности, в которых каждое число больше максимального из тех элементов последовательности,
  сумма цифр которых минимальна. В ответе запишите два числа: сначала количество найденных пар, затем максимальную сумму цифр элементов таких пар.
   В данной задаче под парой подразумевается два идущих подряд элемента последовательности. '''
def func01(num):

    spis = []
    for i in str(num):
        spis.append(int(i))

    return sum(spis)





the_highest_value = -float("inf")
summa = float("inf")

spisok = list()
with open("File") as file:
    line = file.readline().strip()

    while line!= "":
        line = int(line)
        #print(func01(line))
        result = func01(line)
        if result < summa:
            summa = result

            the_highest_value = line
        elif result == summa:
            if the_highest_value < line:
                the_highest_value = line







        spisok.append(int(line))
        line = file.readline().strip()





kolvo = list()
print(the_highest_value)

for m in range( len(spisok) -1):
    if spisok[m] > the_highest_value and  spisok[m + 1] > the_highest_value:
        kolvo.append(func01(spisok[m]) + func01(spisok[m+1]) )

print(len(kolvo),max(kolvo))