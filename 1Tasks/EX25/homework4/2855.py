'''(№ 2855) (Е. Джобс) Среди целых чисел, принадлежащих числовому отрезку [326496; 649632],
 найдите числа, у которых количество четных делителей равно количеству нечетных делителей.
  При этом в каждой из таких групп делителей не менее 70 элементов.
   Для каждого найденного числа запишите само число и минимальный делитель, больший 1000. '''
from math import sqrt

def sg(num):
    D = list()
    snum = int(sqrt(num))
    for i in range(1,snum+1):
        if num % i == 0:
            D.append(i)
            if num//i != i:
                D.append(num //i)
    D.sort()
    return D


for T in range(326496, 649632):
    t2 = sg(T)

    chet = 0
    nchet = 0
    for i in t2:
        if i % 2 == 0:
            chet+=1
        else:
            nchet+=1
    if chet == nchet:
     if chet >=70 and nchet>=70:

        for i in t2 :
            if int(i) >1000:
                print(T,i)
                break






