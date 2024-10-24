'''(№ 6387) (А. Богданов) В файле 17-369.txt содержится последовательность натуральных чисел,
 которые могут принимать значения от 10 до 100000 включительно. Обозначим через S сумму цифр минимального числа,
  состоящего из строго убывающих цифр (например, 321, где 3>2>1).
Определите количество пар последовательности, в которых только одно число состоит из строго возрастающих цифр (например, 247, где 2<4<7),
 а произведение элементов пары кратно S. В ответе запишите сначала количество найденных пар, затем минимальную из сумм элементов таких пар.
  Под парой элементов подразумеваются два соседних элемента последовательности. '''



def STROG(num):
    num = str(num)
    FLAG = True

    for i in range(len(str(int(num) ))- 1):
        if int(num[i]) < int(num[i+1]):
            None
        else:
            FLAG = False

    return FLAG


def NOSTROG(num):
    num = str(num)
    FLAG = True

    for i in range(len(str(int(num) ))- 1):
        if int(num[i]) > int(num[i+1]):
            None
        else:
            FLAG = False

    return FLAG








S = float("inf")

spisok = list()
with open("File") as file:
    line = file.readline().strip()

    while line!= "":
        line = int(line)

        if line < S and NOSTROG(str(line)):
            S = line






        spisok.append(int(line))
        line = file.readline().strip()




def calc(num:str):
    F = list()
    for i in range(len(num)):
        F.append(int(num[i]))
    return sum(F)
S = calc(str(S))

kolvo = list()

for m in range( len(spisok) -1):
    if (STROG( spisok[m]) == True and STROG( spisok[m + 1]) == False) or (STROG( spisok[m]) == False and STROG( spisok[m + 1]) == True):
        if (spisok[m] * spisok[m +1]) % S ==0:
            kolvo.append(spisok[m] + spisok[m +1])


print(len(kolvo),min(kolvo))
