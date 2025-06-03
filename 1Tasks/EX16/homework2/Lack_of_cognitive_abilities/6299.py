'''(№ 6299) Алгоритм вычисления функции F(a, b), где a и b – неотрицательные числа, задан следующими соотношениями:

F(a, 0) = a;
F(a, b) = F(a–b, b), если a ≥ b > 0;
F(a, b) = F(b, a), если a < b.

Определите количество таких чисел n, принадлежащих отрезку 100 000 000 ≤ n ≤ 200 000 000, для которых F(n, 15) = 3. '''


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

for s in range(100):
    print(s,F(s,15))





f = 0
for x in range(100000000,200000001):
    if x % 5 != 0 and x % 3 == 0:

            f+=1
print(f)



#26666666
