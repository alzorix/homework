''' 	(№ 4172) (Е. Джобс) Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:

F(n) = n + 3, при n ≤ 3
F(n) = F(n – 2) + n, при n > 3 и четном значении F(n-1),
F(n) = F(n – 2) + 2•n, при n > 3 и нечетном значении F(n-1).

Определите сумму значений, являющихся результатом вызова функции для значений n в диапазоне [40; 50]. '''
from functools import lru_cache
@lru_cache(None)
def F(n):
    if n <=3:
        return n+3
    elif n >3 and F(n-1) % 2 ==0:
        return F(n - 2) + n

    elif n >3 and F(n-1) % 2 !=0:
        return F(n - 2) + 2*n
    else:
        print(7678686)
        exit()
count =0
for i in range(40,51):
    count+= F(i)
print(count)
#Слишком долго работает