''' 	(№ 5357) (ЕГЭ-2022) Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:

F(n) = 1, если n < 3
F(n) = F(n – 1) + n – 1, если n > 2 и число n чётное,
F(n) = F(n – 2) + 2n - 2, если n > 2 и число n нечётное.

Определите значение F(34). '''



def F(n):
    if n<3:
        return n
    elif n>2 and n%2 ==0:
        return F(n - 1) + n - 1
    elif n>2 and n%2 !=0:
        return F(n - 2) + 2*n - 2
    else:
        print("ERROR")

print(F(34))
#578