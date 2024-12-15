'''(№ 2269) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = n, при n ≤ 3
при n > 3:
  F(n) = F(n–1) + 2*F(n/2), при чётном n;
  F(n) = F(n–1) + F(n-3), при нечётном n;

Определите количество натуральных значений n, при которых F(n) меньше, чем 108.
'''
from functools import lru_cache
@lru_cache()
def F(n):
    if n <=3:
        return n
    else:
        if n % 2 ==0:
            return F(n-1) + 2*F(n//2)
        else:
            return F(n-1) + F(n-3)
count = 0
for n in range(1,1000):
    if F(n) <10**8:

        count+=1
print(count)
#64
