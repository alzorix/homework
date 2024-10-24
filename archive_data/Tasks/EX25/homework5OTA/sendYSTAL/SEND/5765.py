'''(№ 5765) *(Д. Статный) Среди натуральных чисел, принадлежащих промежутку [35 000 000; 100 000 000],
 найдите все числа, имеющие ровно 3 делителя, отличных от 1 и самого числа.
  В ответ запишите найденные числа в порядке возрастания, справа от каждого числа запишите его максимальный делитель, отличный от самого числа. '''
from math import sqrt



def delall(num):
    F = list()
    sqr = int(sqrt(num))
    for i in range(2,sqr+1):
        if num % i == 0:
            F.append(i)
            if num // i !=i:
                F.append(num // i)

        if len(F)>3:
            return F
    return F





for i in range(int(sqrt(35000000)), int(sqrt(100000000))):
    i = i*i
    s = delall(i)
    if len(s) ==3:
            print(i,max(s))
