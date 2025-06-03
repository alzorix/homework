''' 	(№ 5281) (А. Агафонцев) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Найдите наименьшие 7 чисел, удовлетворяющих маске ?6*6*?6 и при этом кратных 6, 7 и 8. Выведите эти числа в порядке возрастания, справа от каждого числа выведите сумму его делителей. '''

from math import sqrt
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

F = list()
F.append("")
from itertools import product
for i in product("0123456789",repeat = 1):
    F.append("".join(i))

for i in product("0123456789",repeat = 2):
    F.append("".join(i))


ysl = list()
for quest1 in range(1,10):
    for quest2 in range(0, 10):
        for a1 in F:
            for a2 in F:
                S = int(f"{quest1}6{a1}6{a2}{quest2}6")
                if S % 7 == 0:
                    if S % 8 == 0:
                        if S % 6 == 0:
                            ysl.append(S)
ysl.sort()
ysll = list(dict.fromkeys(ysl))

for i in range(7):
    r = simplegit(ysll[i])
    print(ysll[i],sum(r))