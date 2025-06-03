'''(№ 3159) Рассмотрим произвольное натуральное число, представим его всеми возможными способами в виде произведения двух
 натуральных чисел и найдём для каждого такого произведения разность сомножителей. Например, для числа 18 получим: 18 = 18*1 = 9*2 = 6*3,
  множество разностей содержит числа 17, 7 и 3. Подходящей будем называть пару сомножителей, разность между которыми не превышает 90.
  Найдите все натуральные числа, принадлежащие отрезку [500000; 1000000], у которых есть не менее трёх подходящих пар сомножителей.
   В ответе перечислите найденные числа в порядке возрастания, справа от каждого запишите наибольший из всех сомножителей, образующих подходящие пары.'''

i = list(range(500000, 1000001))
print(len(i))
#print(i)
#Требуется перебрать 500001 чисел. Вроде не много,попробуем пойти напролом


from math import sqrt
def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(2,KOREN +1):
        if num % i == 0 and num // i != i:
            D.append((i,num // i))
    D.sort()
    return D


import time
start_time = time.time()

for x in i:
    s = simplegit(x)
    maxim_ab = float("-inf")

    good_ab = 0
    for i in range(0,len(s)):

        a,b = s[i]

        t = abs(a-b)
        if t <91:
            #print(1)
            good_ab += 1
            max_ab = max(a, b)
            if max_ab > maxim_ab:
                maxim_ab = max_ab


    if good_ab >2:

            print(x,maxim_ab)

    # print(len(s))
    # print(s)


end_time = time.time()
programm_time = end_time - start_time
print(f"Время выполнения программы: {programm_time} секунд")