'''Задача 25. На отрезке [2, 10000000] найдите все простые числа. Пусть p1, p2, p3, ...
- все найденные простые числа, тогда в ответе укажите каждое стотысячное, то есть
p1, p100000, p200000, ...'''
#print(664578// 100000)




ALLPROSTIE = list()
from math import sqrt
def simple(num):

    snum = int(sqrt(num))
    for i in range(2,snum+1):
        if num % i == 0 :
                return False


    return True
ALLPROSTIE.append(2)
for i in range(3,10000001,2):
    if simple(i):
        ALLPROSTIE.append(i)

lenn = len(ALLPROSTIE)

#print(lenn)
print(ALLPROSTIE[0])
for i in range(1,(lenn// 100000)+1):
    print(ALLPROSTIE[i*100000-1])