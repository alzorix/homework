'''Пусть M (N) – сумма 2 наибольших различных натуральных делителей
натурального числа N, не считая самого числа и единицы. Если у числа N
меньше 2 таких делителей, то M (N) считается равным 0.
Найдите все такие числа N, что 110 250 000 ≤ N ≤ 110 300 000, а десятичная
запись числа M (N) заканчивается на 1002.
В ответе перечислите все найденные числа N в порядке возрастания.'''
def OTAs(num): #простфе множители
    F = list()
    q = 2
    while q**2 <= num:
        if num % q == 0:
            F.append(q)
            num = num//q
        else:
            q +=1
    F.append(num)

    return F

#Забыл функцию
def delitels(number):
    end = number //2
    delitel = list()
    for i in range(end+1,1,-1):
        if number% i ==0:
            delitel.append(i)
        if len(delitel) >=2:
            return delitel
    if len(delitel) >= 2: # Если вдруг каким-либо образом получится больше двух,всё равно вернуть список
        return delitel
    return 0
lim = list()
for N in range(110_250_000, 110_300_001):
    # S = delitels(N)
    # if S:
    #     if len(S) >2:
    #         print("ERROR")
    #     else:
    #         M = sum(S)
    #         #print(str(M)[-4::])
    #         if str(M)[-4::] == "1002":
    #             print(M)
    S = OTAs(N)
    if S:
        if len(S)>=2:
            S.sort()
            M = S[-1]+S[-2]
            #print(str(M)[-4::])
            if str(M)[-4::] == "1002":
                 lim.append(N)
lim.sort()
for i in lim:
    print(i)
#
# 110253248
# 110256430
# 110261942
# 110271001
# 110273085
# 110275397
# 110281591
# 110281994
# 110284534
# 110285355
# 110289512
# 110293385