'''(№ 7251) *Обозначим через a%b остаток от деления натурального числа a на натуральное число b, а через a//b – целую часть от деления a на b. Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 1, если n = 0,
F(n) = F(n // 100) · (n % 10), если n > 0 и n нечётно;
F(n) = F(n // 100), если n > 0 и n чётно.

Определите количество значений n, таких что 109 ≤ n ≤ 6·109, для которых F(n) = 21. '''
from functools import lru_cache

# import sys
# sys.setrecursionlimit(1000000000)
# @lru_cache
# def F(n):
#     if n == 0:
#         return 1
#     else:
#         if n % 2 !=0:
#             return F(n//100) * F(n%10)
#         else:
#             return F(n//100)
#
# for x in range(100):
#     print(x,F(x))



data = dict()

data[0] = 1
for x in range(0,1000):
    if x % 2 != 0:
        data[x]= data[x // 100] * data[x % 10]
    else:
        data[x]= data[x // 100]
