'''(№ 3927) (А. Богданов) Найдите наименьшее натуральное число, которое имеет ровно 512 делителей.
 В ответе запишите сначала само число и затем его наибольший простой делитель.
  Подсказка: используйте основную теорему арифметики. '''
from math import sqrt
def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(1,KOREN +1):
        if num % i == 0:
            D.append(i)
            if num // i != i:
                D.append(num // i)
    D.sort()
    return D
def sg(num):

    KOREN = int(sqrt(num))
    for i in range(2,KOREN +1):
        if num % i == 0:
            return False

    return True

x = 10000
stop = True
while stop:

    s = simplegit(x)

    if len(s) ==512:
        s.reverse()
        for a in s:
            if sg(a):
                stop = False
                print(x,a)
                break

    x = x+1

