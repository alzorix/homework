'''(№ 3127) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(1) = G(1) = 1
F(n) = 3·F(n–1) + G(n–1) – n + 5, если n > 1
G(n) = F(n–1) + 3·G(n–1) – 3·n, если n > 1

Чему равно значение F(14) + G(14)? '''



def F(n):
    if n ==1:
        return 1
    elif n>1:
        return 3*F(n-1) + G(n-1) - n + 5
    else:
        print("err")
        exit()
def G(n):
    if n ==1:
        return 1
    elif n>1:
        return F(n-1) + 3*G(n-1) - 3*n
    else:
        print("err")
        exit()
print(F(14) + G(14))
#37282721