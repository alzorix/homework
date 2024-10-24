'''(№ 5145) Пусть N(k) = 75 000 000 + k, где k – натуральное число. Найдите пять наименьших значений k, при которых N(k)
имеет нечётное количество различных чётных делителей. В ответе запишите найденные значения k в порядке возрастания,
 справа от каждого значения запишите число чётных делителей N(k). '''
from math import  sqrt


def delall(num):
    F = list()
    sqr = int(sqrt(num))
    for i in range(1,sqr+1):
        if num % i == 0:
            F.append(i)
            if num // i !=i:
                F.append(num // i)
    return F





import time
start_time = time.time()


s = 0
k = 2
while s !=5:
    a = 75000000  + k
    fun = delall(a)
    chet = list()
    for i in fun:
        if i %2 == 0:
            chet.append(i)
    if len(chet) % 2 !=0 :
        print(k,len(chet))
        s+=1
    k +=2
end_time = time.time()
programm_time = end_time - start_time
print(f"Время выполнения программы: {programm_time} секунд")
