'''(№ 7249) *Обозначим через a%b остаток от деления натурального числа a на натуральное число b, а через a//b – целую часть от деления a на b. Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 1, если n = 0,
F(n) = F(n // 8) · (n % 8), если n > 0 и n нечётно;
F(n) = F(n // 8), если n > 0 и n чётно.

Определите количество значений n, таких что 89 ≤ n ≤ 6·89, для которых F(n) = 35. '''


from functools import lru_cache

@lru_cache #Произведение нечетных цифр в восмеричной записи числа
def F(n):
    if n == 0:
        return 1
    else:
        if n % 2 != 0:
            return F(n // 8) * (n % 8)
        else:
            return F(n // 8)
c=0
for n in range(1000):
    s = F(n)
    if s == 35:
        print(n, s, oct(n)[2::])
        c+=1
print(c)


print(oct(1*8**9)[2::].count("0")) # 9 нулей - 9цифр

print(oct(6*8**9)[2::]) # 9 нулей - 9цифр

from itertools import permutations

random_set = set()
s = len("5700000000")
for NOline in permutations("5700000000"):
    random_set.add("".join(NOline))
print(len(random_set))

a =0

for x in random_set:
    if x[0] =="0":
        a+= 3* 5**7 # на семи позициях 5 цифр 01246, в на первом 1 2 4
    elif x [0] != "7": #≤ 6·89
        a+= 5**8
print(a)