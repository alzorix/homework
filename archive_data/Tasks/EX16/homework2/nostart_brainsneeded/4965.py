'''(№ 4965) Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:

F(0) = 1
F(n) = 1 + F(n - 1), если n > 0 и n нечётное
F(n) = F(n / 2) в остальных случаях

Определите количество значений n на отрезке [1, 500 000 000], для которых F(n) = 4. '''
from functools import lru_cache
@lru_cache()
def F(n):
    if n == 0:
        return 1
    else:
        if n %2:
            return 1 + F(n - 1)

        
        else:
            return F(n // 2)
c = 0
for n in range(1,500000001):
    if F(n) == 4:
        c+=1
print(c)