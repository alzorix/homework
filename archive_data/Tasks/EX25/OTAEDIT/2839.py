''' 	(№ 2839) Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу.
 Найдите все натуральные числа, принадлежащие отрезку [358633892; 535672891] и имеющие ровно три нетривиальных делителя.
  Для каждого найденного числа запишите в ответе само число и его наибольший нетривиальный делитель. Найденные числа расположите в порядке возрастания. '''

#
# def OTA(num):
#     F = list()
#     T = -1
#     Ft = list()
#     q = 2
#     while q**2 <= num:
#         if num % q == 0:
#             num = num // q
#             if q not in F:
#                 if T ==0:
#                     return F, Ft
#
#
#                 F.append(q)
#                 T +=1
#                 Ft.append(1)
#             else:
#                 Ft[T] +=1
#                 if Ft[T] >4:
#                     return F,Ft
#
#
#         else:
#
#             q +=1
#     if num in F:
#         Ft[T] += 1
#         if Ft[T] > 4:
#             return F, Ft
#
#     else:
#         return F, Ft
#         #
#         # Ft.append(1)
#         # F.append(num)
#
#     return F,Ft
from math import sqrt

def simplegit(num):

    K = int(sqrt(num))
    for i in range(2,K +1):
        if num % i == 0:
           return False
    return True

res = list()
for i in range(358633892, 535672891+1):
    if sqrt(i) == int(sqrt(i)):
        if sqrt(int(sqrt(i))) == int(sqrt(int(sqrt(i)))):
            if simplegit(int(sqrt(int(sqrt(i))))):
                print(i,int(sqrt(int(sqrt(i)))) **3)

#
#
#     S = OTA(i)
#     lenS= len(S)
#     if lenS ==3:
#         res.append((i,max(S)))
#
# res.sort()
#
# for i in range(len(res)):
#     r,s = res[i]
#     print(r,s)
