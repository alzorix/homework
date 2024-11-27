'''(№ 4883) (П. Волгин) Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:

F(n) = 1 при n = 0
F(n) = 7·(n - 1) + F(n - 1) при n > 0

Сколько существует значений n на отрезке [2, 200], для которых значение функции F(n) является простым числом?
	'''
from zoneinfo import reset_tzpath


def F(n):
    if n == 0:
        return 1
    else:
        return 7*(n - 1) + F(n - 1)


def itsTrue(n):
    for candidates in range(2,n):
        if n% candidates ==0:
            return 0
    return 1
count = 0
for n in range(2,201):
    result = F(n)
    if itsTrue(result):
        count+=1
print(count)
#43