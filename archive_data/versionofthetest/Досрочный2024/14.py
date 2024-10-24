chislo = 3*5103**2020+3*729**2021-2*343**2022+27**2023-4*7**2024-2029
#print(chislo)

slovar = dict()
for i in range(10,27):
    temps = 65 + (i -10)

    slovar[i] = chr(temps)
print(slovar)
def solver27(num):
    numbers = 0
    F = list()
    num = int(num)
    while num != 0:
        s1 = num% 27
        if s1 < 10:

            F.append(str(s1))
        else:
            F.append(slovar.get(s1))
            numbers+=1

        num = num//27
    # F.reverse()
    # z = "".join(F)
    return numbers

x = solver27(chislo)

print("Первый вариант")
print(x)

print("Второй вариант задачи:")
#print(ydl2)
ydl2 = list()
for i in range(1,27):
    ydl2.append(i)

ydl2.reverse()

for i in ydl2:
    chast1 = 1 * 27 ** 5 + 2 * 27 ** 4 + 3 * 27 ** 3 + i * 27 ** 2 + 2 * 27 ** 1 + 4
    chast2 = i * 27 ** 3 + 1 * 27 ** 2 + 7 * 27 ** 1 + 8


    cheloe = chast1 + chast2
    #print(cheloe,chast1,chast2,i)
    if cheloe % 26 ==0:

        print(cheloe // 26)
        break
