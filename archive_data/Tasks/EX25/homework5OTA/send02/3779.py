''' 	(№ 3779) Найдите все натуральные числа, принадлежащие отрезку [78 000 000; 85 000 000],
 у которых ровно пять различных нечётных делителей (количество чётных делителей может быть любым).
  В ответе перечислите найденные числа, справа от каждого числа запишите его наибольший нечётный делитель. '''

# from math import sqrt
#
#
# def simplegit(num):
#     K = int(sqrt(num))
#     for i in range(2, K + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# for i in range(78000000, 85000000):
#     t = i
#     while t % 2 == 0:
#         t = t // 2
#
#     sqr = sqrt(t)
#
#     if sqr == int(sqr):
#         sqr = sqrt(sqr)
#         if sqr == int(sqr):
#
#             if simplegit(sqr):
#                 print(i,t)
def OTA(num):
    F = list()
    T = -1
    Ft = list()
    q = 2

    while q**2 <= num:
        if num % q == 0:
            if len(F) > 5:
                return F,Ft
            num = num // q
            if q not in F:
                if q % 2 != 0:

                    F.append(q)
                    T +=1
                    Ft.append(1)
            else:
                if q % 2 != 0:
                    Ft[T] +=1


        else:

            q +=1
    if num in F:
        Ft[T] += 1
    else:

        Ft.append(1)
        F.append(num)

    return F,Ft
for i in range(78000000, 85000000):
    S = OTA(i)
    #None