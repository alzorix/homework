'''(№ 2903) (Б.С. Михлин) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [573213; 575340]
число с минимальной суммой делителей, имеющее ровно четыре делителя. Для найденного числа выведите сумму делителей и наибольший нетривиальный делитель
 (не равный самому числу).'''

from math import sqrt

def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(1,KOREN +1):
        if num % i == 0:
            D.append(i)
            if num // i != i:
                D.append(num // i)
    D.sort()
    return D




S = dict()
S1key = list()
for Tempint in range(573213, 575340):
    if sqrt(Tempint) != int(sqrt(Tempint)):



        tem2 = simplegit(Tempint)
        ltem2 = len(tem2)
        if ltem2 == 4:

            S1key.append(sum(tem2))

            S[sum(tem2)] = tem2[-2]


S1key.sort()


print(S1key[0],S.get(S1key[0]) )