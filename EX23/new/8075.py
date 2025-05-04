'''(№ 8075) (Досрочный ЕГЭ-2025) У исполнителя имеются три команды, которые обозначены латинскими буквами:

A. Прибавь 1
B. Прибавь 2
C. Умножь на 2

Программа для исполнителя – это последовательность команд. Сколько существует программ,
 которые преобразуют число 7 в число 51,
 и при этом траектория вычислений содержит числа 13 и 15, но не содержит числа 35? '''
from functools import lru_cache
@lru_cache(None)
def F(start=7,end=51,onethree=0,onefive=0):
    if start == end and onethree and onefive:
        return 1
    if start >= end:
        return 0
    if start == 13:
        onethree +=1
    if start == 15:
        onefive +=1
    if start == 35:
        return 0
    '''A. Прибавь 1
B. Прибавь 2
C. Умножь на 2'''
    return F(start+1,end,onethree,onefive) + F(start+2,end,onethree,onefive) + F(start*2,end,onethree,onefive)

print(F())
#174034068


