'''(№ 5651) (М. Ишимов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
- символ «?» означает ровно одну произвольную цифру;
- символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300405. Среди натуральных чисел, не превышающих 107, найдите все числа,
 соответствующие маске 3*52?, у которых нечётное количество делителей. В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
  а во втором столбце – соответствующие им максимальные делители, не считая самого числа. '''

F = list()

from math import sqrt
from itertools import product
F.append("")
for i in product("1234567890",repeat = 1):
    F.append("".join(i))

for i in product("1234567890",repeat = 2):
    F.append("".join(i))

for i in product("1234567890",repeat = 3):
    F.append("".join(i))


def simplegit(num):

    KOREN = int(sqrt(num))
    for i in range(2,KOREN +1):
        if num % i == 0 :
            return num//i

S = dict()
S1key = list()
for i in range(0,10):
    for star in F:
        Temp = "3"+  star + "52" + str(i)



        Tempint = int(Temp)
        if sqrt(Tempint) == int(sqrt(Tempint)):




            S1key.append(Tempint)
            S[Tempint] = simplegit(Tempint)

S1key.sort()

for i in S1key:
    print(i,S.get(i) )
