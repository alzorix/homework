'''(№ 7241) *Обозначим через a%b остаток от деления натурального числа a
на натуральное число b, а через a//b – целую часть от деления a на b.
 Алгоритм вычисления значения функции F(n), где n – натуральное число,
  задан следующими соотношениями:

F(n) = 0, если n = 0,
F(n) = F(n // 10) + n % 10, если n > 0 и n чётно;
F(n) = F(n // 10), если n > 0 и n нечётно.

Определите количество значений n, таких что 109 ≤ n ≤ 6·109,
 для которых F(n) = 2. '''


def F(n):
    if n ==0:
        return 0
    else:
        if n% 2 ==0:
            return F(n//10) + n % 10
        else:
            return F(n//10)

for nis in range(100): # сумма четный чисел
    if F(nis) == 2:
        print(nis,F(nis))

print(3*5**9 * 1) # ( 1 3 5 )  (1 3 5 7 9) (2)