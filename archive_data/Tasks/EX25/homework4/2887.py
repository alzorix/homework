'''(№ 2887) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [5408238; 5408389],
 простые числа. Выведите все найденные простые числа в порядке возрастания, слева от каждого числа выведите его номер по порядку. '''
from math import sqrt

def sg(num):

    snum = int(sqrt(num))
    for i in range(2,snum+1):
        if num % i == 0 :
                return False


    return True



S = list()
for T in range(5408238, 5408389):


        tem2 = sg(T)
        if tem2:

            S.append(T)




S.sort()

for i in range(len(S)):
    print(i+1,S[i])