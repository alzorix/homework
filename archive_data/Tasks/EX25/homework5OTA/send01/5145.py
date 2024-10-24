''' 	(№ 5145) Пусть N(k) = 75 000 000 + k, где k – натуральное число. Найдите пять наименьших значений k,
 при которых N(k) имеет нечётное количество различных чётных делителей. В ответе запишите найденные значения k в порядке возрастания,
  справа от каждого значения запишите число чётных делителей N(k).'''

from math import sqrt
def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(2,KOREN +1,2):
        if num % i == 0:
            D.append(i)
            if num // i != i and (num // i) %2 ==0:
                D.append(num // i)
    D.sort()
    return D


s = 0
k = 0
while s !=5:
    a = 75000000  + k
    fun = simplegit(a)
    if len(fun) %2 !=0:
        print(k,len(fun))
        s+=1
    k +=1

#Где ошибка?
# k = 6752
# a = 75000000  + k
# fun = simplegit(a)
# print(fun)
# if len(fun) %2 !=0:
#         print(k,len(fun))
#         #s+=1
# #k +=1