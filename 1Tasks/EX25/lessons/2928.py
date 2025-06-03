'''(№ 2928) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [126849; 126871], числа,
имеющие ровно 4 различных делителя. Выведите для каждого найденного числа два наибольших делителя в порядке возрастания. '''

from math import sqrt

def simplegittalscastratorededition(num):
    D = list()


    KOREN = int(sqrt(num))
    for i in range(1,KOREN +1):


        if num % i == 0:
            D.append(i)
            if num // i != i:
                D.append(num // i)
    D.sort()


    return D



for i in range(126849, 126872):
    F = simplegittalscastratorededition(i)
    if len(F) ==4:
        print(F[-2],max(F))


