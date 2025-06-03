''' 	(№ 4939) Пусть D(N) – пятый по величине (считая с наибольшего) нетривиальный делитель натурального числа N
 (нетривиальными считаются все делители, кроме 1 и самого числа).
  Если у числа N меньше пяти различных нетривиальных делителей, о принимаем D(N) = 0.

  Найдите 5 наибольших натуральных чисел, меньших 100 000 000, для которых D(N) > 0.
   В ответе запишите для каждого найденного N сначала значение D(N),
    а затем общее количество нетривиальных делителей (в порядке возрастания соответствующих чисел N). '''
S = dict()
S1key = list()
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
    if len(D) < 5:
        return False,D
    D.sort()
    return True,D

k = 0
s = 0
while k!=5:
    R = 100000000-1 - s

    temp = simplegit(R)
    if temp[0]:
            #print(temp[-6],len(temp))
            S1key.append(R)
            S[R] = (temp[1][-5],len(temp[1]))
            k +=1

    s = s+1





S1key.sort()

for i in S1key:
    r,s = S.get(i)
    print(r,s)

end_time = time.time()
programm_time = end_time - start_time
print(f"Время выполнения программы: {programm_time} секунд")
