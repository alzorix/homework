'''' (№ 7389) *(А. Минак) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(1) = F(2) = 1,
F(n) = 3·F(n – 2) + F(n – 1), если n > 2.

Чему равно значение выражения F(20000024) / F(20000020)? Запишите в ответе только целую часть числа. '''


# F = [0]*20000025
#
# F[1] = 1
# F[2]= 1
# for index in range(3,20000025):
#     F[index] = 3 * F[index - 2] + F[index -1]
#
# print(F[20000024] // F[20000020])
import sys
sys.setrecursionlimit(100000000)
from functools import lru_cache
@lru_cache()
def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return 3*F(n - 2) + F(n - 1)

print(F)
print(F(20000024) // F(20000020))
