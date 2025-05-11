'''(№ 4207) (А. Богданов) Два игрока, Петя и Ваня, играют в следующую игру.
 Перед игроками лежит три кучи камней. Игроки ходят по очереди, первый ход делает Петя.
  За один ход игрок может добавить в одну из куч 3, 13 или 23 камня.
  Игра завершается в тот момент, когда в сумме в кучах будет не менее 73 камней.
   \Победителем считается игрок, сделавший последний ход. В начальный момент в кучах было (2, S, 2S) камней, 1 ≤ S ≤ 23.
Ответьте на следующие вопросы:
  Вопрос 1. При некотором значении S Ваня одержал победу свои первым ходом после неудачного хода Пети.
  Укажите минимальное значение S, при котором это возможно.
  Вопрос 2. Найдите минимальное и максимальное значения S, при которых Петя выигрывает вторым ходом при любом ходе Вани.
  Вопрос 3. Найдите два значения S, при которых выигрышная стратегия есть у Вани, но Петя может выбрать,
  каким ходом выиграет Ваня – первым или вторым. '''
print("19:")
def  F_19(A,B,C,H):
    #1 - start
    #2 - Petya
    #3 - Vanya
    if A+B+C >= 73 and H == 3:
        return True
    elif A+B+C >= 73 and H != 3:
        return False
    elif A+B+C < 73 and H == 3:
        return False

    if H % 2 ==0: # Был ход Пети,значит ходит Ваня. Ваня умный, Ваня побеждает
        return  F_19(A+3,B,C,H+1) or F_19(A,B+3,C,H+1) or F_19(A,B,C+3,H+1) or F_19(A+13,B,C,H+1) or F_19(A,B+13,C,H+1) or F_19(A,B,C+13,H+1)or F_19(A+23,B,C,H+1) or F_19(A,B+23,C,H+1) or F_19(A,B,C+23,H+1)
    else: # Был ход Вани, теперь очередь Пети. Петя глупый,Петя делает неудачных ход. => or - повторить почему
        return  F_19(A+3,B,C,H+1) or F_19(A,B+3,C,H+1) or F_19(A,B,C+3,H+1) or F_19(A+13,B,C,H+1) or F_19(A,B+13,C,H+1) or F_19(A,B,C+13,H+1) or F_19(A+23,B,C,H+1)  or F_19(A,B+23,C,H+1)  or F_19(A,B,C+23,H+1)

#9

for S in range(1,64):
    if F_19(2,S,2*S,1):
        print(S)
print("20:")
'''Вопрос 2. Найдите минимальное и максимальное значения S, 
при которых Петя выигрывает вторым ходом при любом ходе Вани.'''
def  F_20(A,B,C,H):
    #1 - start
    #2 - Petya
    #3 - Vanya
    if A+B+C >= 73 and H == 4:
        return True
    elif A+B+C >= 73 and H != 4:
        return False
    elif A+B+C < 73 and H == 4:
        return False

    if H % 2 ==0: # Был ход Пети,значит ходит Ваня. Ваня умный, Ваня побеждает всегда
        return  F_20(A+3,B,C,H+1)  and F_20(A,B+3,C,H+1)  and F_20(A,B,C+3,H+1) and  F_20(A+13,B,C,H+1)  and F_20(A,B+13,C,H+1)  and F_20(A,B,C+13,H+1) and F_20(A+23,B,C,H+1) and  F_20(A,B+23,C,H+1)  and F_20(A,B,C+23,H+1)
    else: # Был ход Вани, теперь очередь Пети. Петя вроде тоже умный,он делает самые крутые ходы
        return  F_20(A+3,B,C,H+1) or F_20(A,B+3,C,H+1) or F_20(A,B,C+3,H+1) or F_20(A+13,B,C,H+1) or F_20(A,B+13,C,H+1) or F_20(A,B,C+13,H+1) or F_20(A+23,B,C,H+1)  or F_20(A,B+23,C,H+1)  or F_20(A,B,C+23,H+1)

for S in range(1,64):
    if F_20(2,S,2*S,1):
        print(S)
#8 14
print("21:")
'''Вопрос 3. Найдите два значения S, при которых выигрышная стратегия есть у Вани, но Петя может выбрать,
  каким ходом выиграет Ваня – первым или вторым. '''

def  F_21(A,B,C,H):
    #1 - start
    #2 - Petya
    #3 - Vanya
    if A+B+C >= 73 and (H == 3 or H == 5):

        return True
    elif A+B+C >= 73 and (H != 3 or H != 5):
        return False
    elif A+B+C < 73 and H == 5:
        return False

    if H % 2 ==0: # Был ход Пети,значит ходит Ваня.
        return  F_21(A+3,B,C,H+1)  or F_21(A,B+3,C,H+1)  or F_21(A,B,C+3,H+1) or  F_21(A+13,B,C,H+1)  or F_21(A,B+13,C,H+1)  or F_21(A,B,C+13,H+1) or F_21(A+23,B,C,H+1) or  F_21(A,B+23,C,H+1)  or F_21(A,B,C+23,H+1)
    else: # Был ход Вани, теперь очередь Пети.
        return  F_21(A+3,B,C,H+1) and F_21(A,B+3,C,H+1) and F_21(A,B,C+3,H+1) and F_21(A+13,B,C,H+1) and F_21(A,B+13,C,H+1) and F_21(A,B,C+13,H+1) and F_21(A+23,B,C,H+1)  and F_21(A,B+23,C,H+1)  and F_21(A,B,C+23,H+1)


def  F_21_check(A,B,C,H):
    #1 - start
    #2 - Petya
    #3 - Vanya
    if A+B+C >= 73 and (H == 3):
        return True
    elif A+B+C >= 73 and (H != 3):
        return False
    elif A+B+C < 73 and H == 3:
        return False

    if H % 2 ==0: # Был ход Пети,значит ходит Ваня.
        return  F_21_check(A+3,B,C,H+1)  or F_21_check(A,B+3,C,H+1)  or F_21_check(A,B,C+3,H+1) or  F_21_check(A+13,B,C,H+1)  or F_21_check(A,B+13,C,H+1)  or F_21_check(A,B,C+13,H+1) or F_21_check(A+23,B,C,H+1) or  F_21_check(A,B+23,C,H+1)  or F_21_check(A,B,C+23,H+1)
    else: # Был ход Вани, теперь очередь Пети.
        return  F_21_check(A+3,B,C,H+1) and F_21_check(A,B+3,C,H+1) and F_21_check(A,B,C+3,H+1) and F_21_check(A+13,B,C,H+1) and F_21_check(A,B+13,C,H+1) and F_21_check(A,B,C+13,H+1) and F_21_check(A+23,B,C,H+1)  and F_21_check(A,B+23,C,H+1)  and F_21_check(A,B,C+23,H+1)

def  F_21_check_2(A,B,C,H):
    #1 - start
    #2 - Petya
    #3 - Vanya
    if A+B+C >= 73 and (H == 5):
        return True
    elif A+B+C >= 73 and (H != 5):
        return False
    elif A+B+C < 73 and H == 5:
        return False

    if H % 2 ==0: # Был ход Пети,значит ходит Ваня.
        return  F_21_check_2(A+3,B,C,H+1)  or F_21_check_2(A,B+3,C,H+1)  or F_21_check_2(A,B,C+3,H+1) or  F_21_check_2(A+13,B,C,H+1)  or F_21_check_2(A,B+13,C,H+1)  or F_21_check_2(A,B,C+13,H+1) or F_21_check_2(A+23,B,C,H+1) or  F_21_check_2(A,B+23,C,H+1)  or F_21_check_2(A,B,C+23,H+1)
    else: # Был ход Вани, теперь очередь Пети.
        return  F_21_check_2(A+3,B,C,H+1) and F_21_check_2(A,B+3,C,H+1) and F_21_check_2(A,B,C+3,H+1) and F_21_check_2(A+13,B,C,H+1) and F_21_check_2(A,B+13,C,H+1) and F_21_check_2(A,B,C+13,H+1) and F_21_check_2(A+23,B,C,H+1)  and F_21_check_2(A,B+23,C,H+1)  and F_21_check_2(A,B,C+23,H+1)

for S in range(1,64):
    # true_21_3 = False
    # true_21_5 = False

    if F_21(2,S,2*S,1) :
        print(S,F_21_check(2,S,2*S,1),F_21_check_2(2,S,2*S,1))
        #print(S)
#10 13