'''(№ 5173) (Е. Джобс) Алгоритмы вычисления функций F(n) и G(n), где n – целое число, заданы следующими соотношениями::

F(n) = G(n) = 1, если n < 3
F(n) = G(n) + F(n – 1), если n > 2 и n чётно,
F(n) = F(n – 2) - 2·G(n + 1), если n > 2 и n нечётно,
G(n) = F(n – 3) + F(n – 2), если n > 2 и n чётно,
G(n) = F(n + 1) – G(n – 1), если n > 2 и n нечётно

Вычислите значений функции G(120). '''

from functools import lru_cache
@lru_cache()
def F(n):
    if n <3:
        return 1
    elif n % 2 == 0:
        return G(n) + F(n - 1)
    else:
        return F(n - 2) - 2*G(n + 1)
@lru_cache()
def G(n):
    if n <3:
        return 1
    elif n % 2 == 0:
        return F(n - 3) + F(n - 2)
    else:
        return F(n + 1) - G(n - 1)

print(G(120))