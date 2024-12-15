'''(№ 6297) Алгоритм вычисления функции F(a, b), где a и b – неотрицательные числа, задан следующими соотношениями:

F(a, 0) = a;
F(a, b) = F(a–b, b), если a ≥ b > 0;
F(a, b) = F(b, a), если a < b.

Определите количество таких чисел n, принадлежащих отрезку 100 000 000 ≤ n ≤ 200 000 000, для которых F(n, 21) = 1.


Показать ответ'''
import sys
sys.setrecursionlimit(900000000)
from functools import lru_cache
@lru_cache()
def F(a,b):
    if b ==0:
        return a
    elif b > 0 and a >=b:
        return F(a-b,b)
    elif a<b:
        return F(b,a)
    else:
        print("E")

c = 0
for n in range(100_000_000, 200_000_000):
    if F(n,21) == 1:
        c+=1
print(c)
