''' 	(№ 6183) (Н. Сафронов) В файле 17-363.txt содержится последовательность целых неотрицательных чисел, не превышающих 10000.
 Определите количество пар элементов последовательности, в которых запись хотя бы одного элемента из двух состоит только из четных цифр,
  а сумма элементов пары больше максимального элемента последовательности, состоящего только из нечетных цифр. В ответе запишите два числа:
   сначала количество найденных пар, затем максимальную сумму элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности. '''


def func01(num):
    nechet = 0
    chet = 0
    spis = []
    for i in str(num):
        spis.append(int(i))

    for i in range(len(spis)):
        if spis[i] % 2==0:
            chet = chet + 1
        elif spis[i] % 2!=0:
            nechet = nechet + 1

    if chet == 0 and nechet != 0:
            return True
    elif nechet == 0 and chet != 0:
            return False
    else:
            return "Это же не True??"





the_highest_element_of_a_sequence_consisting_only_of_odd_digits = -float("inf")

spisok = list()
with open("File") as file:
    line = file.readline().strip()

    while line!= "":
        print(func01(line))
        line = int(line)
        #print(func01(line))
        if line > the_highest_element_of_a_sequence_consisting_only_of_odd_digits and func01(line) == True:
            print(func01(line))
            the_highest_element_of_a_sequence_consisting_only_of_odd_digits = line






        spisok.append(int(line))
        line = file.readline().strip()





kolvo = list()

for m in range( len(spisok) -1):
    if func01(spisok[m]) == False or func01(spisok[m  +1 ]) == False:
        if spisok[m] + spisok[m  +1] > the_highest_element_of_a_sequence_consisting_only_of_odd_digits:
            kolvo.append(spisok[m] + spisok[m  +1])
print(len(kolvo),max(kolvo))
