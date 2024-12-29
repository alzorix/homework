''' 	(№ 6830) (А. Богданов) Обозначим частное от деления натурального числа a на натуральное число b как a // b, а остаток как a%b.
 Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = n, если n < 2;
F(n) = F(n // 2)  + F(n % 2), если n ≥ 2.

Определите количество значений n < 2^30, для которых функция F(n) = 27. '''
#



def F(n):
    if n<2:
        return n
    else:
        return F(n // 2) + F(n % 2)
for x in range(100):
    print(x,bin(x)[2::],F(x))
#
# print(bin(2**30)[2::])
#
# print(int("1"*27,2))
# c = 0
# for x in range(134217727,2**30):
#     if bin(x)[2::].count("1") == 27:
#         c+=1
# print(c)
from math import factorial
#
print(factorial(30)/(factorial(27) * factorial(3)))