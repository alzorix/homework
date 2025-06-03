'''(№ 6077) Алгоритм вычисления функции F(a, b), где a и b – неотрицательные целые числа, задан следующими соотношениями:

F(a, b) = 0, если a = 0 и b = 0
F(a, b) = F(a–1, b) + b, если a > b
F(a, b) = F(a, b–1) + a, если a ≤ b

Найдите количество таких чисел a, для которых можно найти число b, такое что F(a, b) = 18522000. '''
from functools import lru_cache
import sys
sys.setrecursionlimit(900000000)
@lru_cache()
def F(a,b):
    if a == 0 and b ==0:
        return 0
    else:
        if a > b:
            return F(a-1,b)+b
        else:
            return F(a,b-1)+a

for a in range(0,10):
    for b in range(0,10):
        print(a,b, F(a,b) )
#делаем вывод,что тут цифры просто перемножаются


# c =0
# for a in range(0,18522000):
#     F = False
#     for b in range(0,18522000):
#         if a * b ==18522000:
#             F= True
#             break
#     if F:
#         c+=1
# #делаем вывод,что тут цифры просто перемножаются
# print(c)

from math import sqrt

def dell(n):
    c = 0
    for x in range(1,n+1):
        if n % x ==0:
            c+=1
    return c
print(dell(18522000))
#320