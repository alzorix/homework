'''(№ 2895) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [2484292; 2484370], простые числа.
Выведите все найденные простые числа в порядке возрастания, слева от каждого числа выведите его номер по порядку. '''
from math import sqrt
def simplegit(num):

    K = int(sqrt(num))
    for i in range(2,K +1):
        if num % i == 0:
           return False
    return True

import time
start_time = time.time()
s = 1
for i in range(2484292, 2484371):
    if simplegit(i):
        print(s,i)
        s+=1
# import time
# start_time = time.time()
end_time = time.time()
programm_time = end_time - start_time
print(f"Время выполнения программы: {programm_time} секунд")