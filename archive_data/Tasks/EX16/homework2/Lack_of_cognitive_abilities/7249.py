'''(№ 7249) *Обозначим через a%b остаток от деления натурального числа a на натуральное число b, а через a//b – целую часть от деления a на b. Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 1, если n = 0,
F(n) = F(n // 8) · (n % 8), если n > 0 и n нечётно;
F(n) = F(n // 8), если n > 0 и n чётно.

Определите количество значений n, таких что 89 ≤ n ≤ 6·89, для которых F(n) = 35. '''

def F(n):
    if n == 0:
        return 1
    else:
        if n % 2 !=0:
            return F(n // 8) * (n % 8)
        else:
            return F(n//8)

alf = [1,2,3,4,5,6,7]
alf1 = [1,2,3,4,5,6,7]
c=0
for a in alf1:
    for a1 in alf:
        for a2 in alf:
            for a3 in alf:
                for a4 in alf:
                    for a5 in alf:
                        for a6 in alf:
                            for a7 in alf:
                                for a8 in alf:
                                    for a9 in alf:
                                        L =  a+   a1+   a2+   a3+     a4+    a5+   a6+   a7+    a8+  a9
                                        L = str(L)
                                        if "5" in L:
                                            if "7" in L:
                                                if int(L,8) < 6*8**9:
                                                    if F(int(L,8)) == 35:
                                                        c+=1

print(c)


