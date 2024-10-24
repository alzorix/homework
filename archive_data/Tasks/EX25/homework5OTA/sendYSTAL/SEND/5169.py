''' 	(№ 5169) (Д. Муфаззалов) На отрезке [2; 14] найдите пять наибольших натуральных чисел,
факториал каждого из которых имеет нечетное количество простых делителей. Выведите найденные числа в порядке убывания,
справа от каждого числа – количество простых делителей его факториала. '''
def fact(n):
    a = 1
    for i in range(1, n+1):
        a *=i
    return a
from math import sqrt
def OTA(num):
    F = list()
    T = -1
    Ft = list()
    q = 2
    while q**2 <= num:
        if num % q == 0:
            num = num // q
            if q not in F:

                F.append(q)
                T +=1
                Ft.append(1)
            else:
                Ft[T] +=1


        else:
            q +=1
    if num in F:
        Ft[T] += 1
    else:

        Ft.append(1)
        F.append(num)

    return F
for otrezok in range(2,15):
    f = fact(otrezok)
    s = OTA(f)
    if len(s) % 2 != 0:
        print(otrezok,len(s))