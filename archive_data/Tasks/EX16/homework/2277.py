''' 	(№ 2277) Алгоритм вычисления значения функции F(n),
 где n – натуральное число, задан следующими соотношениями:

F(n) = 2*n*n*n + n*n, при n > 25
F(n) = F(n+2) + 2*F(n+3), при n ≤ 25

Определите сумму цифр значения F(2).'''
def F(n):
    if n > 25:
        return 2*n**3 + n**2
    else:
        return F(n+2) + 2*F(n+3)
c = 0
l = str(F(2))
for i in l:
    c +=int(i)
print(c)
#33