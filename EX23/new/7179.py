'''(№ 7179) (М. Шагитов) У исполнителя Калькулятор имеются три команды, которые обозначены латинскими буквами:

A. Прибавить 1
B. Прибавить 4
C. Умножить на 3

Найдите количество существующих программ, для которых при исходном числе 1 результатом является число 180,
и при этом траектория вычислений содержит равное количество чисел, кратных трём, и чисел, кратных пяти.
 В ответе запишите сумму цифр этого числа. '''
from functools import lru_cache

@lru_cache(None)
def F(start=1,end=180,three=0,five=0):

    if start % 5 ==0:
        five+=1
    if start % 3 ==0:
        three+=1

    if start == end and five==three:
        return 1
    if start == end:
        return 0
    if start > end:
        return 0

    return F(start+1,end,three,five) + F(start+4,end,three,five)+ F(start*3,end,three,five)

print(sum(int(x) for x in str(F())))
#112