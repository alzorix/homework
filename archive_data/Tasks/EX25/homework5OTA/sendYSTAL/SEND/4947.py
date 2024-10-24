'''(№ 4947) Особыми будем называть нетривиальные делители числа, все цифры которых нечётные. Нетривиальными считаются все делители,
кроме 1 и самого числа.
 Пусть D(N) – пятый по величине (считая с наибольшего) особый делитель натурального числа N.
 Если у числа N меньше пяти различных особых делителей, то принимаем D(N) = 0.
 Найдите 5 наибольших натуральных чисел,  меньших 300 000 000, для которых D(N) > 0.
 В ответе запишите для каждого найденного N сначала значение D(N),
  а затем общее количество особых делителей (в порядке возрастания соответствующих чисел N). '''

import time
start_time = time.time()
from math import sqrt




S = dict()
S1key = list()


def realspecial(num):

    num = str(num)
    for i in num:
        if int(i) % 2 ==0:
            return False


    return True

def special(num):
    F = list()
    ser = int(sqrt(num))
    for i in range(2,ser+1):
        if num % i ==0:
            if realspecial(i):
                F.append(i)
            if num//i != i:
                if realspecial(num//i):
                    F.append(num//i)
    F.sort()
    return F





k = 0
s = -1
while k!=5:
    R = 300000000 + s
    temp = special(R)
    if len(temp)>=5:

        DN = temp[-5]









        S1key.append(R)
        S[R] = (DN,len(temp))
        k +=1

    s = s-1
S1key.sort()
for i in S1key:
    r,s = S.get(i)
    print(r,s)
end_time = time.time()
programm_time = end_time - start_time
print(f"Время выполнения программы: {programm_time} секунд")
