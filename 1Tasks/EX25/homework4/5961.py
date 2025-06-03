'''(№ 5961) (Н. Сафронов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300405. Среди натуральных чисел, не превышающих 107, найдите все числа,
соответствующие маске 12*348, которые делятся на 12 без остатка и имеют ровно 12 делителей. В ответе запишите все найденные числа в порядке возрастания,
 а справа от каждого числа — максимальный делитель, не равный самому числу. '''
F = list()

from math import sqrt
from itertools import product
F.append("")
for i in product("1234567890",repeat = 1):
    F.append("".join(i))

for i in product("1234567890",repeat = 2):
    F.append("".join(i))






def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(1,KOREN +1):
        if num % i == 0 :
            D.append(i)
            if num // i != i :
                D.append(num // i)
    D.sort()
    return D







S = dict()
S1key = list()
for star in F:
    Temp = "12"+star+"348"
    Tempint = int(Temp)
    if sqrt(Tempint) != int(sqrt(Tempint)):

      if Tempint % 12 == 0:
        tem2 = simplegit(Tempint)
        if len(tem2)==12:
            # S = dict()
            # S1key = list()
            S1key.append(Tempint)
            S[Tempint] = tem2[-2]

S1key.sort()

for i in S1key:
    print(i,S.get(i) )
