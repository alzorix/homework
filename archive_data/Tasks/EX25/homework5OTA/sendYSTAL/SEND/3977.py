
'''(№ 3977) Найдите все натуральные числа, N, принадлежащие отрезку [150000000; 300 000 000], которые можно представить
в виде N = 2m•3n, где m – чётное число, n – нечётное число.
 В ответе запишите все найденные числа в порядке возрастания, а справа от каждого числа – сумму m+n'''
import time
start_time = time.time()


# s = list()
# for m in range(0,30,2):
#     for n in range(1, 30, 2):
#         q = 2**m * 7**n
#         if 100000000 <= q <= 300000000:
#             s.append((q,n+m))
#
#
# s.sort()
# for i in range(len(s)):
#         print(s[i][1],s[i][0])
#

print(2**30)

s = list()

for m in range(0,30,2):
    for n in range(1,30,2):
        N = 2**m * 3**n
        if 150000000 <= N <= 300000000:
            #print(N,m+n)
            s.append((N, n + m))

s.sort()
for i in range(len(s)):
        print(s[i][1],s[i][0])


end_time = time.time()
programm_time = end_time - start_time
print(f"Время выполнения программы: {programm_time} секунд")