'''(№ 6523) (А. Богданов) Обозначим частное от деления натурального числа a на натуральное число b как a // b, а остаток как a%b. Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = n, если n < 2;
F(n) = n % 2  + 10· F(n//2), если n ≥ 2.

Определите значение n, для которого функция F(n) = 100000100001000100101. ''' # Мне это значение перепечатывать нужно будет?
data = dict()

from functools import lru_cache
@lru_cache()
def check(n):
    if n<2:
        return n
    else:
        s = n % 2  + 10* check(n//2)
        return s

# for i in range(1,100):
#     print(i,check(i),bin(i)[2::])

#Тут сразу видно

print(int("100000100001000100101",2))
#1065509