'''(№ 5225) Пусть N(k) = 9 500 000 + k, где k – натуральное число. Найдите пять наименьших значений k,
 при которых N(k) нельзя представить в виде произведения трёх натуральных чисел, больших 1.
  В ответе запишите найденные значения k в порядке убывания, справа от каждого значения запишите наибольший делитель N(k), не равный самому числу. '''


from math import sqrt
def delall(num):
    F = list()
    sqr = int(sqrt(num))
    for i in range(2,sqr+1):
        if num % i == 0:
            F.append(i)
            if num // i !=i:
                F.append(num // i)
    return F




s = 0
k = 0
while s !=5:
    a = 9500000 + k
    if len(delall(a)) !=3:
        print(k,max(delall(a)))
        print(delall(a))
        s+=1
    k +=1
# s = (9500000//3)+1
# for a1 in range(2,s):
#     for a2 in range(2, s):
#         for a3 in range(2, s):
#             None
#             # F = a1*a2*a3
#             # if F > 9500000