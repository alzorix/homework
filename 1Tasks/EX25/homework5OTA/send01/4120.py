'''(№ 4120) (А. Кабанов) Обозначим через F целую часть среднего арифметического всех простых делителей целого числа,
 не считая самого числа. Если таких делителей у числа нет, то считаем значение F равным нулю. Напишите программу, которая перебирает целые числа,
  большие 650000, в порядке возрастания и ищет среди них такие, для которых значение F при делении на 37 даёт в остатке 23.
   Выведите первые 4 найденных числа в порядке возрастания и справа от каждого числа – соответствующее значение F. '''
from math import sqrt


def OTAs(num):
    num1 = num
    F = list()
    q = 2
    while q**2 <= num:
        if num % q == 0:
            F.append(q)
            num = num//q
        else:
            q +=1
    if num == num1:
        return [1]
    else:
        F.append(num)

    return F



def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(2,KOREN +1):
        if num % i == 0 :
            D.append(i)
            if num // i != i :
                D.append(num // i)
    D.sort()
    return D


k = 208

a = 650000  + k
print(a)
fun = simplegit(a)
print(fun)
F = sum(fun)//len(fun)
print(F)



if F %37 ==23:
    print(a,F)
    print("GOOD")










#
# k = 208
#
# a = 650000  + k
# print(a)
# fun = OTAs(a)
# print(fun)
# F = sum(fun)//len(fun)
# print(F)
#
#
#
# if F %37 ==23:
#     print(a,F)
#     print("GOOD")









s = 0
k = 0
while s !=5:
    a = 650000  + k
    fun = OTAs(a)
    F = int(sum(fun)//len(fun))



    if F %37 ==23:
        print(a,F)
        s+=1
    k +=1



