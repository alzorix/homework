'''(№ 7212) У исполнителя Калькулятор имеются четыре команды, которые обозначены латинскими буквами:

A. Вычесть 1
B. Вычесть 3
C. Прибавить 6
D. Умножить на 3

Найдите количество существующих программ, для которых при исходном числе 5 результатом является число 58,
 и при этом траектория вычислений содержит число 26 и не содержит чисел, оканчивающихся на 1,
  а программа не содержит двух команд вычитания подряд и не проходит дважды через конечное число. '''

def F(start,end,history_ansewer:bool,vichet:bool,twentySix:bool):
    if str(start)[-1] == ("1"):
        return 0

    if start == 26:
        twentySix = True
    # if start > end + 3:
    #     return 0
    if start > end:

        if history_ansewer:
            return 0
        else:
            history_ansewer = True

    if start == end:
        if twentySix:

            return 1

        else:
            return 0


    else:
        if vichet == False:

            return (F(start-1,end,history_ansewer,True,twentySix) + F(start-3,end,history_ansewer,True,twentySix)
                    + F(start+6,end,history_ansewer,False,twentySix) + F(start*3,end,history_ansewer,False,twentySix))
        else:
            return F(start+6,end,history_ansewer,False,twentySix) + F(start*3,end,history_ansewer,False,twentySix)


print(F(5,58,False,False,False))



