''' 	(№ 5412) (А. Богданов) В файле 17-342.txt содержится последовательность целых чисел.
 Элементы последовательности – натуральные числа, не превосходящие 10000. Найдите такие пары элементов,
  в которых только одно число находится между значениями минимального кратного 37 и максимального кратного 73.
   Гарантируется, что такая пара в последовательности есть.  В ответе запишите количество найденных пар и минимальную
   сумму элементов среди таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности. '''

spisok = list()

min37 = float("inf")
max73 = -float("inf")
with open("file") as f:
    line = f.readline().strip()
    while line != "":
        line = int(line)



        if line % 37 == 0 and line < min37 :
            min37 = line
        if line % 73 == 0 and line > max73 :
            max73 = line

        spisok.append(line)

        line = f.readline().strip()


#print(min37,max73)



kolvo = 0
minsum = list()
for m in range( len(spisok) -1):
    try:

        if max73< spisok[m] < min37:
            if max73< spisok[m + 1] < min37:
                None
            else:
                kolvo += 1
                minsum.append(spisok[m + 1] +  spisok[m])

        if max73 < spisok[m+ 1] < min37:
            if max73 < spisok[m] < min37:
                None
            else:
                kolvo += 1
                minsum.append(spisok[m + 1] +  spisok[m])









    except:
        None


print(kolvo,min(minsum))
