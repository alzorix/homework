'''(№ 6297) Алгоритм вычисления функции F(a, b), где a и b – неотрицательные числа, задан следующими соотношениями:

F(a, 0) = a;
F(a, b) = F(a–b, b), если a ≥ b > 0;
F(a, b) = F(b, a), если a < b.

Определите количество таких чисел n, принадлежащих отрезку 100 000 000 ≤ n ≤ 200 000 000, для которых F(n, 21) = 1.


Показать ответ'''

from functools import lru_cache
@lru_cache()
def F(a,b):
    if b ==0:
        return a
    elif b > 0 and a >=b:
        return F(a-b,b)
    elif a<b:
        return F(b,a)
    else:
        print("E")

# c=0
# for i in range(100000003, 200000001,3):
#     c+=1
# for i in range(100000007, 200000001,7):
#     c+=1
#
# print(100000000+1-c)
f = 0
for x in range(100000000,200000001):
    if x % 7 ==0 or x % 3 ==0:
        None
    else:
        f+=1
print(f)
#57142859