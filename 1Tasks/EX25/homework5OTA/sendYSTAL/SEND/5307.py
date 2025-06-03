''' 	(№ 5307) (Л. Шастин) Пусть P(N) – сумма всех простых делителей числа N, а E(N) - сумма всех его чётных делителей.
 Обозначим M(N) = | P(N) – E(N) | (модуль разности). Найдите 5 наименьших чисел, больших 100 000 000,
  у которых количество простых делителей совпадает с количеством чётных делителей.
   В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
    а во втором столбце — соответствующие им значения M(N). '''
from math import sqrt
def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(1,KOREN +1):
        if num % i == 0:
            if i % 2 ==0:

                D.append(i)


            if num // i != i:
                if (num// i) % 2 == 0:
                    D.append(num // i)
    D.sort()
    return D
#print(simplegit(40))
def delall(num):
    F = list()
    sqr = int(sqrt(num))
    for i in range(1,sqr+1):
        if num % i == 0:
            F.append(i)
            if num // i !=i:
                F.append(num // i)
    return F
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

t = 0
for XXX in range(100000001 , 100000000+1000):
    ENs=simplegit(XXX)
    PNs=OTA(XXX)



    EN = sum(ENs)
    PN  = sum(PNs)
    if len(PNs) == len(ENs):
        if t == 5:
            break
        MN =  abs(PN - EN)
        print(XXX,MN)
        t +=1
