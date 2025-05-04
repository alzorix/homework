'''(№ 7177) (М. Шагитов) У исполнителя Калькулятор имеются три команды,
 которые обозначены латинскими буквами:

A. Прибавить 2
B. Прибавить 3
C. Умножить на 4

Найдите количество существующих программ, для которых при исходном числе 1 результатом является число 100,
и при этом траектория вычислений содержит строго больше чётных чисел, чем нечётных.
 В ответе запишите сумму цифр этого числа. '''
from functools import lru_cache

@lru_cache(None)
def F(start,end,chet=0,nechet=0):

    if start % 2 ==0:
        chet+=1
    else:
        nechet+=1

    if start == end and chet>nechet:
        return 1
    if start == end:
        return 0
    if start > end:
        return 0

    return F(start+2,end,chet,nechet) + F(start+3,end,chet,nechet)+ F(start*4,end,chet,nechet)

print(sum(int(x) for x in str(F(1,100))))
#58