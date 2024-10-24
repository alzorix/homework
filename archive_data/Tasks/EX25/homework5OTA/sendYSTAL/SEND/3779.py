''' 	(№ 3779) Найдите все натуральные числа, принадлежащие отрезку [78 000 000; 85 000 000],
 у которых ровно пять различных нечётных делителей (количество чётных делителей может быть любым).
  В ответе перечислите найденные числа, справа от каждого числа запишите его наибольший нечётный делитель.'''






from math import  sqrt



def delall(num):
    F = list()
    sqr = int(sqrt(num))
    for i in range(1,sqr+1):
        if num % i == 0:
            if i % 2 !=0:
                F.append(i)
            if num // i !=i:
                if (num // i) % 2 != 0:
                    F.append(num // i)

        if len(F)>5:
            return F
    return F





for i in range(78000000, 85000000):

    s = delall(i)
    if len(s) ==5:
            print(i,max(s))
