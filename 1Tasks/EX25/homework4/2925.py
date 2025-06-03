''' 	(№ 2925) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [150750; 150764],
 числа, имеющие ровно 4 различных делителя. Выведите для каждого найденного числа два наибольших делителя в порядке возрастания. '''


from math import sqrt

def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(1,KOREN +1):
        if num % i == 0 :
            D.append(i)
            if num // i != i:
                D.append(num // i)
    D.sort()
    return D





for Tempint in range(150750, 150764):
        tem2 = simplegit(Tempint)
        ltem2 = len(tem2)
        if ltem2 == 4:
            print(tem2[-2],Tempint)


