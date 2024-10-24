''' 	(№ 5225) Пусть N(k) = 9 500 000 + k, где k – натуральное число. Найдите пять наименьших значений k,
 при которых N(k) нельзя представить в виде произведения трёх натуральных чисел, больших 1.
  В ответе запишите найденные значения k в порядке убывания, справа от каждого значения запишите наибольший делитель N(k),
   не равный самому числу. '''
from math import sqrt
def simple(num):

    K = int(sqrt(num))
    for i in range(2,K +1):
        if num % i == 0:
           return True
    return False
def simplegit(num):
    D = list()
    fist = True
    KOREN = int(sqrt(num))
    for i in range(2, KOREN + 1):
        if num % i == 0:
            D.append(i)
            if num // i != i:
                if fist:
                    if simple(num // i):
                        return 0,D
                    fist = False


                D.append(num // i)
    D.sort()
    return 1,D
s3 = 0
S = dict()
S1key = list()
for Nk in range(9500001,9500000 + 10000):
    if s3 == 5:
        break
    s = simplegit(Nk)
    if s[0]:
        #print(Nk -9500000 ,max(s[1]))
        S1key.append(Nk -9500000)
        S[Nk -9500000] = max(s[1])
        s3+=1



S1key.sort()
S1key.reverse()
for i in S1key:
    r = S.get(i)
    print(i,r)