'''(№ 2263) Алгоритм вычисления значений функций F(n) и G(n), где n – натуральное число, задан следующими соотношениями:

F(1) = 1; G(1) = 1;
F(n) = F(n–1) – 2·G(n–1), при n >=2
G(n) = F(n–1) + G(n–1) + n, при n >=2

Чему равна сумма цифр величины G(36)? '''
from  functools import lru_cache
@lru_cache()
def F(n):
    if n ==1:
        return 1
    elif n>=2:
        return F(n-1) - 2*G(n-1)
    else:
        print("ERR")
        exit()
@lru_cache()
def G(n):
    if n ==1:
        return 1
    elif n>=2:
        return F(n-1) + G(n-1) + n
    else:
        print("ERR")
        exit()
#print(G(36))
c = 0
s = G(36)
for i in str(s):
    c+=int(i)
print(c)
#долго решает СЛИШКОМ долго