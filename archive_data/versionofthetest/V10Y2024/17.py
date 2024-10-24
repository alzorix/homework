'''Задача 17. В файле содержится последовательность натуральных чисел, каждое
из которых не превышает 10 000. В начальной строке файла находится число n - коли-
чество чисел в файле.

 Определите количество троек элементов последовательности, в
которых ровно один элемент является 3-х значным числом в 16-ричной системе счис-
ления, и хотя бы одно число заканчивается на 17. Гарантируется, что в последователь-
ности есть хотя бы одно число, оканчивающееся на 17. В ответе запишите количество
найденных троек чисел, затем максимальную из сумм элементов таких троек. В данной
задаче под тройкой подразумевается три идущих подряд элемента последовательности.'''


def ysl16(num1,num2,num3):
    num1_16 = len(hex(num1  )[2::])
    num2_16 = len(hex( num2 )[2::])
    num3_16 = len(hex( num3 )[2::])


    if num1_16 ==3 and num3_16 !=3 and num2_16 !=3:
        return True

    if num1_16 != 3 and num3_16 == 3 and num2_16 != 3:
        return True

    if num1_16 != 3 and num3_16 != 3 and num2_16 == 3:
        return True

    return False


the_min = float("inf")
spisok = list()

with open("17var.txt") as file:
    line = file.readline().strip()
    line = file.readline().strip()
    while line!= "":
        spisok.append(int(line))
        line = file.readline().strip()



kolvo = list()
for m in range( len(spisok) -2):
    # print( str(spisok[m])[-2::])
    # print(spisok[m])
    if str(spisok[m])[-2::] == "17" or str(spisok[m+1])[-2::] == "17" or str(spisok[m+2])[-2::] == "17":
        if ysl16(spisok[m],spisok[m+1],spisok[m+2]):
            print(spisok[m],spisok[m+1],spisok[m+2])


            kolvo.append(sum(spisok[m:m+3]))




print(len(kolvo),max(kolvo))