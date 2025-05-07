'''(№ 7213) У исполнителя Калькулятор имеются четыре команды, которые обозначены латинскими буквами:

A. Вычесть 1
B. Вычесть 5
C. Прибавить 7
D. Умножить на 2

Найдите количество существующих программ, для которых при исходном числе 9 результатом является число 84,
 и при этом траектория вычислений содержит число 60 и не содержит чисел,
 оканчивающихся на 3,
 а программа не содержит двух команд вычитания подряд и не проходит дважды через конечное число. '''

from functools import lru_cache

@lru_cache(None)
def F(start=9,end=84,sixteen=0,vichet= False,passreturn= False):
    if start-end >5:
        return 0
    if str(start)[-1] == "3":
        return 0

    # if start < end and passreturn:
    #     return 0
    # if start > end:
    #     passreturn = True

    if start == 60:
        sixteen+=1

    if start == end and sixteen:
        return 1
    if start == end:
        return 0


    '''A. Вычесть 1
B. Вычесть 5
C. Прибавить 7
D. Умножить на 2'''

    if vichet:
        return F(start + 7, end, sixteen, False, passreturn) + F(start * 2, end, sixteen, False, passreturn)
    else:
        return  F(start-1,end,sixteen,True,passreturn)+ F(start-5,end,sixteen,True,passreturn)+ F(start+7,end,sixteen,False,passreturn)+ F(start*2,end,sixteen,False,passreturn)





print(F())

