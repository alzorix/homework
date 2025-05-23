'''(№ 4725) (И. Осипов) Два игрока, Петя и Ваня, играют в следующую игру.
Перед игроками лежат три кучи камней. Игроки ходят по очереди,
 первый ход делает Петя.
 За один ход игрок может добавить в одну из куч (по своему выбору) три камня
  или увеличить количество камней в куче в два раза. Например, пусть в первой куче 10 камней,
   во второй 7, а в третьей 4 камня; такую позицию в игре будем обозначать (10, 7, 4).
   Тогда за один ход можно получить любую из шести позиций: (13, 7, 4), (20, 7, 4),
   (10, 10, 4), (10, 14, 4), (10, 7, 7), (10, 7, 8). Для того чтобы делать ходы,
    у каждого игрока есть неограниченное количество камней. Игра завершается в тот момент,
    когда суммарное количество камней в кучах становится не менее 71.
     Победителем считается игрок, сделавший последний ход, т. е. первым получивший такую позицию,
      что в кучах всего будет 71 или больше камней.
    В начальный момент в первой куче было семь камней, во второй куче пять камней,
    в третьей куче – S камней; 1 ≤ S ≤ 58.
Ответьте на следующие вопросы:
  Вопрос 1.При некотором значении S Ваня одержал победу свои первым ходом после неудачного хода Пети.
  Укажите минимальное значение S, при котором это возможно.
  Вопрос 2. Найдите минимальное и максимальное значения S, при которых Петя выигрывает вторым ходом при любом ходе Вани.
  Вопрос 3. Найдите значение S, при котором одновременно выполняются два условия:
  а) у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
   б) у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом. '''

print("19:")

def F_19(A,B,C,H):
    # 1 - START
    # 2 - PETYA
    # 3 - VANYA
    if A +B +C >= 71 and H ==3 :
        return True
    elif  A +B +C >= 71 and H !=3 :
        return False
    elif  A +B +C < 71 and H ==3 :
        return False

    if H % 2 == 0: # Был Петя,пошёл Ваня - Ваня побеждает после плохого хода Вани => or
        return F_19(A+3,B,C,H +1 ) or F_19(A,B+3,C,H +1 ) or F_19(A,B,C+3,H +1 ) or F_19(A*2,B,C,H +1 ) or F_19(A,B*2,C,H +1 ) or F_19(A,B,C*2,H +1 )
    else: # Тут в это ситуации тоже or,так как нам нужно перебрать все варианты ходов
        return F_19(A+3,B,C,H +1 ) or F_19(A,B+3,C,H +1 ) or F_19(A,B,C+3,H +1 ) or F_19(A*2,B,C,H +1 ) or F_19(A,B*2,C,H +1 ) or F_19(A,B,C*2,H +1 )

for  S in range(1,59):
    if F_19(7,5,S,1):
        print(S)
        break
#15
print("20:")
'''Вопрос 2. Найдите минимальное и максимальное значения S,
 при которых Петя выигрывает вторым ходом при любом ходе Вани.'''
def F_20(A,B,C,H):
    # 1 - START
    # 2 - PETYA
    # 3 - VANYA
    if A +B +C >= 71 and H ==4 :
        return True
    elif  A +B +C >= 71 and H !=4 :
        return False
    elif  A +B +C < 71 and H ==4 :
        return False

    if H % 2 == 0: # Был Петя,пошёл Ваня - Ваню побеждают всегда
        return F_20(A+3,B,C,H +1 ) and F_20(A,B+3,C,H +1 ) and F_20(A,B,C+3,H +1 ) and F_20(A*2,B,C,H +1 ) and F_20(A,B*2,C,H +1 ) and F_20(A,B,C*2,H +1 )

    else: # Петя - наилучший ход
        return F_20(A+3,B,C,H +1 ) or F_20(A,B+3,C,H +1 ) or F_20(A,B,C+3,H +1 ) or F_20(A*2,B,C,H +1 ) or F_20(A,B*2,C,H +1 ) or F_20(A,B,C*2,H +1 )




for  S in range(1,59):
    if F_20(7,5,S,1):
        print(S)
#14 27
print("21:")

'''Вопрос 3. Найдите значение S, при котором одновременно выполняются два условия:
  а) у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
   б) у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом. '''

def F_21(A,B,C,H):
    # 1 - START
    # 2 - PETYA
    # 3 - VANYA
    if A +B +C >= 71 and (H ==3 or   H == 5):
        return True
    elif  A +B +C >= 71 and H !=3 and H != 5 :
        return False
    elif  A +B +C < 71 and H ==5 :
        return False

    if H % 2 == 0:
        return F_21(A+3,B,C,H +1 ) or F_21(A,B+3,C,H +1 ) or F_21(A,B,C+3,H +1 ) or F_21(A*2,B,C,H +1 ) or F_21(A,B*2,C,H +1 ) or F_21(A,B,C*2,H +1 )

    else:
        return F_21(A+3,B,C,H +1 ) and F_21(A,B+3,C,H +1 ) and F_21(A,B,C+3,H +1 ) and F_21(A*2,B,C,H +1 ) and F_21(A,B*2,C,H +1 ) and F_21(A,B,C*2,H +1 )

def F_21_ch(A,B,C,H):
    # 1 - START
    # 2 - PETYA
    # 3 - VANYA
    if A +B +C >= 71 and H ==3 :
        return True
    elif  A +B +C >= 71 and H !=3 :
        return False
    elif  A +B +C < 71 and H ==3 :
        return False

    if H % 2 == 0:
        return F_21_ch(A+3,B,C,H +1 ) or F_21_ch(A,B+3,C,H +1 ) or F_21_ch(A,B,C+3,H +1 ) or F_21_ch(A*2,B,C,H +1 ) or F_21_ch(A,B*2,C,H +1 ) or F_21_ch(A,B,C*2,H +1 )

    else:
        return F_21_ch(A+3,B,C,H +1 ) and F_21_ch(A,B+3,C,H +1 ) and F_21_ch(A,B,C+3,H +1 ) and F_21_ch(A*2,B,C,H +1 ) and F_21_ch(A,B*2,C,H +1 ) and F_21_ch(A,B,C*2,H +1 )

for  S in range(1,59):
    if F_21(7,5,S,1):
        if not(F_21_ch(7,5,S,1)):
            print(S)
#24