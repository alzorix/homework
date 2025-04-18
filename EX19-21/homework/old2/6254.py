'''(№ 6254) (PRO100 ЕГЭ) Два игрока, Петя и Ваня, играют в следующую игру.
 Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя.
  За один ход игрок может добавить в кучу один камень или три камня или одиннадцать камней.
  Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
Игра завершается в тот момент, когда количество камней в куче становится числом, оканчивающимся на ноль.
 Победителем считается игрок, сделавший последний ход, т.е. первым получивший кучу,
  количество камней в которой оканчивается на ноль. К примеру, игра заканчивается,
   когда в куче стало 10, 200, 6800 камней. В начальный момент в куче было S камней,
   где S – двузначное число, не оканчивающиеся на ноль.
Ответьте на следующие вопросы:
  Вопрос 1. Укажите минимальное значение S, при котором Петя не может выиграть за один ход,
   но при любом ходе Пети Ваня может выиграть своим первым ходом.
  Вопрос 2. Найдите количество значений S, при которых у Пети есть выигрышная стратегия,
   причём одновременно выполняются два условия:
– Петя не может выиграть за один ход;
– Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
  Вопрос 3. Найдите сумму значений S, при которых у Вани есть выигрышная стратегия,
   причём одновременно выполняются два условия:
— у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
— у Вани нет стратегии, которая позddволит ему гарантированно выиграть первым ходом. '''
#print("19:")
# def F_19(A,H):
#     # 1 - START
#     # 2 - Petya
#     # 3 - Vanya
#     if str(A)[-1] == "0" and H == 3:
#         return True
#     elif str(A)[-1] != "0" and H == 3:
#         return False
#     elif str(A)[-1] == "0" and H != 3:
#         return False
#
#     if H % 2 == 0: #Ход вани
#         return F_19(A+3,H+1) or  F_19(A+1,H+1) or  F_19(A+11,H+1)
#     else:
#         return F_19(A+3,H+1) and  F_19(A+1,H+1) and  F_19(A+11,H+1)
#
# for S in range(11,100):
#     if str(S)[-1] != "0":
#         if F_19(S,1):
#             print(S)
#             break
#16

'''  Вопрос 2. Найдите количество значений S, при которых у Пети есть выигрышная стратегия,
   причём одновременно выполняются два условия:
– Петя не может выиграть за один ход;
-Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.'''

#print("20:")
# def F_20(A,H):
#     # 1 - START
#     # 2 - Petya
#     # 3 - Vanya
#     if str(A)[-1] == "0" and H == 4:
#         return True
#     elif str(A)[-1] != "0" and H == 4:
#         return False
#     elif str(A)[-1] == "0" and H != 4:
#         return False
#
#     if H % 2 == 0: #Ход вани
#         return F_20(A+3,H+1) and  F_20(A+1,H+1) and  F_20(A+11,H+1)
#     else:
#         return F_20(A+3,H+1) or  F_20(A+1,H+1) or  F_20(A+11,H+1)
# c = 0
# for S in range(11,100):
#     if str(S)[-1] != "0":
#         if F_20(S,1):
#             c+=1
# print(c)
#18
'''
Вопрос 3. Найдите сумму значений S, при которых у Вани есть выигрышная стратегия,
   причём одновременно выполняются два условия:
— у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом
 при любой игре Пети;
— у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом. '''
print("21:")
c = 0
def F_21(A,H):
    # 1 - START
    # 2 - Petya
    # 3 - Vanya
    if str(A)[-1] == "0" and (H == 3 or H == 5):
        return True
    elif str(A)[-1] != "0" and H == 5:
        return False
    elif str(A)[-1] == "0" and (H != 3 or H !=5):
        return False

    if H % 2 == 0: #Ход вани
        return F_21(A+3,H+1) or  F_21(A+1,H+1) or  F_21(A+11,H+1)
    else:
        return F_21(A+3,H+1) and  F_21(A+1,H+1) and  F_21(A+11,H+1)
def F_21_ch(A,H):
    # 1 - START
    # 2 - Petya
    # 3 - Vanya
    if str(A)[-1] == "0" and (H == 3 ):
        return True
    elif str(A)[-1] != "0" and H == 3:
        return False
    elif str(A)[-1] == "0" and (H != 3):
        return False

    if H % 2 == 0: #Ход вани
        return F_21_ch(A+3,H+1) or  F_21_ch(A+1,H+1) or  F_21_ch(A+11,H+1)
    else:
        return F_21_ch(A+3,H+1) and  F_21_ch(A+1,H+1) and  F_21_ch(A+11,H+1)
for S in range(11,100):

    if str(S)[-1] != "0":
        if F_21(S,1):
            if not(F_21_ch(S,1)):
                c+=S
print(c)
#954