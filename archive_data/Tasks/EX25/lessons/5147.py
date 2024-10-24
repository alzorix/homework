'''(№ 5147) Пусть N(k) = 1 850 000 000 + k, где k – натуральное число. Найдите пять наименьших значений k,
 при которых N(k) имеет нечётное количество различных чётных делителей. В ответе запишите найденные значения k
  в порядке возрастания, справа от каждого значения запишите число чётных делителей N(k). '''


from math import  sqrt

def OTA(num):
    F = list()
    T = -1
    Ft = list()
    temp = 0
    while num %2 ==0:
        temp +=1
        num = num//2
    if temp %2 ==0:
        return (False,0)
    q = 3
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
            if T != -1 and Ft[T] % 2 != 0:
                return (False, 0)

            q +=2
    if num in F:
        Ft[T] += 1
        if T != -1 and Ft[T] % 2 != 0:
            return (False, 0)
    else:
        return (False, 0)


    kolvochet = temp
    for x in Ft:
        kolvochet = kolvochet * (x +1)


    return True,kolvochet


import time
start_time = time.time()


s = 0
k = 2
while s !=5:
    a = 1850000000  + k
    fun = OTA(a)
    if fun[0]:

        print(k,fun[1])
        s+=1
    k +=2



end_time = time.time()
programm_time = end_time - start_time
print(f"Время выполнения программы: {programm_time} секунд")
