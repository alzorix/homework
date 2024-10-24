''' 	(№ 5437) (Л. Малинов) В файле 17-343.txt содержится последовательность целых чисел. Элементы последовательности
могут принимать целые значения от 0 до 10 000 включительно. Определите количество троек, в которых для каждого числа тройки
 сумма цифр в нечётных разрядах нацело делится на сумму цифр в чётных разрядах. Разряды нумеруются с нуля справа налево.
  В ответе запишите два числа: сначала количество найденных троек, а затем – минимальную сумму элементов таких троек.
  В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности. '''


spisok = list()
with open("File") as file:
    line = file.readline().strip()
    while line!= "":





        spisok.append(int(line))
        line = file.readline().strip()

def func01(num):
    nechet = 0
    chet = 0
    spis = []
    for i in str(num):
        spis.append(int(i))
    spis.reverse()
    for i in range(len(spis)):
        if i % 2==0:
            chet = chet + spis[i]
        else:
            nechet = nechet + spis[i]



    try:
        if nechet % chet  ==0:
            return  True
        else:
            return False
    except:
        None





kolvo = list()

for m in range( len(spisok) -2):
    if func01(spisok[m]) and func01(spisok[m  +1 ]) and func01(spisok[m  +2]):





        kolvo.append(spisok[m]+spisok[m+1]+spisok[m+2])



print(len(kolvo),min(kolvo))




