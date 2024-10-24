'''(№ 3753) Найдите все натуральные числа, принадлежащие отрезку [113 000 000; 114 000 000], у которых ровно три различных чётных делителя.
 В ответе перечислите найденные числа в порядке возрастания, справа от каждого числа запишите его второй по величине нетривиальный делитель
 (не равный 1 и самому числу). Первым по величине считается меньший из нетривиальных делителей числа. '''

a = list(range(113000000, 114000001,2))
from math import  sqrt


import time
start_time = time.time()

for num in a:
    F = list()
    q = 1
    ysl = list()
    while q ** 2 <= num:


        if num % q == 0 :
            ysl.append(q)


            if q % 2 ==0:
                F.append(q)
            if  (num // q) != q:
                ysl.append(num // q)
                if (num // q) % 2 == 0:
                    F.append(num // q)


        q +=1

        if len(F) >3:
            break
    F.sort()
    ysl.sort()
    if len(F) == 3:
        print(num,ysl[2])




end_time = time.time()
programm_time = end_time - start_time
print(f"Время выполнения программы: {programm_time} секунд")

