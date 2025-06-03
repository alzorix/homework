'''(№ 6025) (Н. Сафронов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300405. Найдите все натуральные числа, не превосходящие 107, для которых выполняются одновременно все условия:
1) соответствуют маске *2?2*;
2) являются палиндромами;
3) делятся на число 53 без остатка;
4) количество делителей больше 30.
В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, справа от каждого числа – сумму его делителей'''
from itertools import product
from math import sqrt

#Создание L лист с всевозможными вариантами чисел за место *
# L = list()
# L.append("")
# for i in product("0123456789",repeat = 1):
#     L.append("".join(i))
# for i in product("0123456789",repeat = 2):
#     L.append("".join(i))
# for i in product("0123456789",repeat = 3):
#     L.append("".join(i))
# for i in product("0123456789",repeat = 4):
#     L.append("".join(i))

# def SEARCHDELALL(x):
#     delList= list()
#
#
#     sx = int(sqrt(x))
#     for i in range(1,sx+1):
#         if x % i == 0:
#             if (x % i not in delList) :
#
#
#                     delList.append( i)
#
#             if (x // i not in delList) :
#                     delList.append(x // i)
#     return delList

def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(1,KOREN +1):
        if num % i == 0:
            D.append(i)
            if num // i != i:
                D.append(num // i)
    D.sort()
    return D



# S = dict()
# S1key = list()

#
# for i in range(0,10):
#     i = str(i)
#     for a1 in L:
#         for a2 in L:
#             if len(a1) ==4 and len(a2) ==4:
#                 break
#             z = a1 + "2" + i + "2" + a2
#             if z[0] != "0":
#             #z = str(int(z))
#             #print(z)
#                 if len(z)<8:
#                     if int(z) % 53 == 0:
#                         if z == z[::-1]:
#                             f = simplegit(int(z))
#                             if len(f) >30:
#                                 if z not in S1key:
#                                     S1key.append(z)
#                                     S[z] = sum(f)
#
# S1key.sort()
#
#
# for i in S1key:
#     print(i,S.get(i) )

print(" ")
from fnmatch import fnmatch

for i in range(1,10**7):
    stri = str(i)
    if fnmatch(stri,"*2?2*"):
        if stri[::-1] == stri:
            if i % 53==0:
                D = simplegit(i)
                if len(D) > 30:
                    print(i,sum(D))







