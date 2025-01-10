'''(№ 4969) Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:

F(0) = 3
F(n) = 1 + F(n / 2), если n > 0 и n чётное
F(n) = F(n // 2) в остальных случаях

Здесь // означает деление нацело. Определите количество значений n на отрезке [1, 1 000 000 000], для которых F(n) = 7. '''
from functools import lru_cache


# @lru_cache
# def F(n):
#     if n == 0:
#         return 3
#     else:
#         if n % 2 ==0:
#             return 1+ F(n/2)
#         else:
#             return F(n//2)
# c = 0
# for n in range(1,1_000):
#     print(n,F(n),bin(n)[2::])
#     if F(n) ==7:
#         c+=1
# print(c)
print(len(bin(1_000_000_000)[2::]))
c = 0
for x in range(1,27):
    line = "1" * x + "0000"
    if len(line)< 30:
        c+= 1*2**(len(line)-1)
        print(line,len(line)-1)
    else:
        print(1)
print(c)
# 536870896 не сходится
c = 0
c+=1




# from itertools import permutations
# print(len(bin(1_000_000_000)[2::]))
# #0001
# c = 0
# c+=1
#
# for x in range(1,26):
#     line = "0000"+"1"*x
#     for i in permutations(line):
#         s = "".join(i)
#         if s[0] !="0":
#                 c+=1
#
#
# print(c)
#
#
#
#
# # c = 0
# # for n in range(1,1_000_000_001):
# #     if bin(n)[2::].count("0") == 4:
# #         c+=1
# # print(c)
# #долго всё