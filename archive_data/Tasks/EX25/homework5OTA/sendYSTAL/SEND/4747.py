'''(№ 4747) Пусть S (N) – сумма трёх наибольших нетривиальных делителей числа N (не считая единицы и самого числа).
 Если у числа N меньше трёх таких делителей, то S (N) считается равным 0.
 Найдите 5 наименьших натуральных чисел, превышающих 10 000 000, для которых десятичная запись S (N) содержит не менее четырёх цифр 7.
  В ответе запишите найденные числа в порядке возрастания, справа от каждого числа запишите соответствующее ему значение S(N). '''
import time
start_time = time.time()
from math import sqrt
def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(2,KOREN +1):
        if num % i == 0:
            D.append(i)
            if num // i != i:
                D.append(num // i)
    if len(D) < 3:
        return False,D
    D.sort()
    return True,D

k = 0
s = 0
while k!=5:
    R = 10000000 + s

    temp = simplegit(R)
    if temp[0]:

        SN = str(temp[1][-1]+temp[1][-2]+temp[1][-3])
        if SN.count("7") >3:
            print(R,SN)
            k +=1

    s = s+1


end_time = time.time()
programm_time = end_time - start_time
print(f"Время выполнения программы: {programm_time} секунд")