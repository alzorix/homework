'''(№ 2845) Рассматриваются целые числа, принадлежащих числовому отрезку [416782; 498324], которые представляют собой
 произведение трёх различных простых делителей, оканчивающихся на одну и ту же цифру.
  В ответе запишите количество таких чисел и разницу между максимальным и минимальным из них. '''
from math import sqrt

def OTAs(num):
    F = list()
    num = int(num)
    q = 2
    while q**2 <= num:

        if len(F) >3:
            return False

        if num % q == 0:
                F.append(q)
                num = num//q
        else:
                q +=1
    F.append(num)
    fset = set(F)
    if len(fset) !=len(F):
        return False
    else:
        if len(F) ==3:
            if str(F[0])[-1] == str(F[1])[-1] == str(F[2])[-1] :


                return True
            else:
                return False
        else:

            return False
def simplegits(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(2,KOREN +1):
        if num % i == 0:
            D.append(i)
            if num // i != i and (num // i) %2 ==0:
                D.append(num // i)
    D.sort()
    return D

globallist = list()
for i in range(416782, 498324):

    a = OTAs(i)
    if a:


                globallist.append(i)



print(len(globallist),max(globallist)-min(globallist))