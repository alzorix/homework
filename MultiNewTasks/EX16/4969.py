'''(№ 4969) Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:

F(0) = 3
F(n) = 1 + F(n / 2), если n > 0 и n чётное
F(n) = F(n // 2) в остальных случаях

Здесь // означает деление нацело. Определите количество значений n на отрезке [1, 1 000 000 000], для которых F(n) = 7. '''
from functools import lru_cache

@lru_cache()
def F(n):
    if n == 0:
        return 3
    else:
        if n % 2 ==0:
            return 1 + F(n/2)
        else:
            return F(n//2)

for x in range(10000):
    if bin(x)[2::].count("0") ==4:
        #print(x,F(x),bin(x)[2::])
        None
#Имеем,что в случае,если в записи числа у нас 4 нуля,то F = 7


all_lines = set()

from itertools import permutations


print(len(bin(1_000_000_000)[2::]))


for x in range(40):
    s = "1" * (x - 4) + "0000"
    if int(s,2) <= 1000000000:

     for i in permutations(s):
        l = "".join(i)

        if l[0] != "0":
            all_lines.add(l)
        else:
            t = l.find("1")
            l = l[t::]
            all_lines.add(l)
    else:
        break
print(len(all_lines))
print(c)