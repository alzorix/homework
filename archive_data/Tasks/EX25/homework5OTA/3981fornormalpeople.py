''' (№ 3981) Найдите все натуральные числа, N, принадлежащие отрезку [100 000 000; 300 000 000],
 которые можно представить в виде N = 2m•7n, где m – чётное число, n – нечётное число.
  В ответе запишите все найденные числа в порядке возрастания, а справа от каждого числа – сумму m+n. '''

s = list()
for m in range(0,30,2):
    for n in range(1, 30, 2):
        q = 2**m * 7**n
        if 100000000 <= q <= 300000000:
            s.append((q,n+m))


s.sort()
for i in range(len(s)):
        print(s[i][1],s[i][0])


