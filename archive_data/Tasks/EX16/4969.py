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

f = 0
#print(len(bin(1_000_000_000)[2::]))

from math import factorial
c= 0
for x in range(25,0,-1):
    s = "1" * x + "0000"
        #1 + 4 нуля + s единицы
    n = len(s) - 1
    k = 4 #  первым у нас в любом случае идет единица,поэтому её и вычетаем разве нет?
    c+= factorial(n)//(factorial(k) * (factorial(n-k)))

print(bin(1_000_000_000)[2::])
a = set()
for x in permutations(str(26*"1" + "0000")):
    if "".join(x)[4::] != "1111":
      if  int("".join(x),2) < 1_000_000_000:


        a.add(x)


print(len(a) + c )




