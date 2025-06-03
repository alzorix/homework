''' (№ 3981) Найдите все натуральные числа, N, принадлежащие отрезку [100 000 000; 300 000 000],
 которые можно представить в виде N = 2m•7n, где m – чётное число, n – нечётное число.
  В ответе запишите все найденные числа в порядке возрастания, а справа от каждого числа – сумму m+n. '''

def OTA(num):
    F = list()
    T = -1
    Ft = list()
    q = 2

    if num % q == 0:
        while num % 2 == 0:
            num = num // q
            if q not in F:

                F.append(q)
                T +=1
                Ft.append(1)
            else:
                Ft[T] +=1

    q = 7
    if num % q == 0:
        while num % 7 ==0:

            num = num // q
            if q not in F:

                F.append(q)
                T +=1
                Ft.append(1)
            else:
                Ft[T] +=1

    if num in F :
        Ft[T] += 1
    else:
        if num == 1:
            None
        else:

            Ft.append(1)
            F.append(num)

    return F,Ft

# i = 210827008
# chisla,stepemi = OTA(i)
# print(OTA(i))
# if len(chisla) == 2:
#         if chisla[0]==2 and chisla[1] == 7:
#             if stepemi[0]% 2 ==0:
#                 if stepemi[1]%2!=0:
#                     print(i,sum(stepemi))









for i in range(100000000, 300000000):
    chisla,stepemi = OTA(i)
    if len(chisla) == 2:
        if chisla[0]==2 and chisla[1] == 7:
            if stepemi[0]% 2 ==0:
                if stepemi[1]%2!=0:
                    print(i,sum(stepemi))

