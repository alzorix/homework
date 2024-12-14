'''(№ 3929) (А. Богданов) Алгоритмы вычисления функций F(n) и G(n) заданы следующими соотношениями (здесь // – операция деления нацело, % – остаток от деления):

F(n) = n, при n < 10,
F(n) = n % 10 + F(n // 10), при n ≥ 10.
G(n) = n, при n < 10,
G(n) = G(F(n)), при n ≥ 10

Чему равна сумма значений функции G(n) для всех двузначных n?'''
from functools import lru_cache

@lru_cache()
def F(n):
    if n <10:
        return n
    else:
        return n % 10 + F(n // 10)
@lru_cache()
def G(n):
    if n<10:
        return n
    else:
        return G(F(n))
    
c=0
for i in range(10,100):
    c+=G(i)

print( c)