'''Требуется написать функцию, которая будет принимать на вход число, а возвращать список из простых множителей:
Например, для числа 360 функция должна возвращать список [2, 2, 2, 3, 3, 5].'''
from math import sqrt


# def simplegit(num):
#
#     K = int(sqrt(num))
#     for i in range(2,K +1):
#         if num % i == 0:
#            return False
#     return True
#
#
# def OTAs(num):
#     ALL  = list()
#     for potentialdel in range(2,int(sqrt(num))+1):
#         if simplegit(potentialdel):
#             while num % potentialdel == 0:
#                 ALL.append(potentialdel)
#                 num = num //potentialdel
#     ALL.sort()
#     return ALL
#
#
# def OTA(num):
#     stepeni = list()
#     helps= -1
#
#     ALL  = list()
#     for potentialdel in range(2,int(sqrt(num))+1):
#         if simplegit(potentialdel):
#             while num % potentialdel == 0:
#                 if potentialdel not in ALL:
#
#                     ALL.append(potentialdel)
#                     stepeni.append(1)
#                     helps +=1
#                 else:
#                     stepeni[helps] +=1
#                 num = num //potentialdel
#     ALL.sort()
#     return ALL,stepeni


def OTAs(num): #простфе множители
    F = list()
    q = 2
    while q**2 <= num:
        if num % q == 0:
            F.append(q)
            num = num//q
        else:
            q +=1
    F.append(num)

    return F

def OTA(num):
    F = list()
    T = -1
    Ft = list()
    q = 2
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
            q +=1
    if num in F:
        Ft[T] += 1
    else:

        Ft.append(1)
        F.append(num)

    return F,Ft


if __name__ == "__main__" :
    while True:
        c = int(input("Число:"))
        print(OTAs(c))
        print(OTA(c))
        a, b = OTA(c)
        print(a,b)

