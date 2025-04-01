'''(№ 2396) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней. Игроки ходят по очереди,
первый ход делает Петя. За один ход игрок может добавить в одну из куч один камень или увеличить количество камней в куче в два раза.
 Чтобы делать ходы, у каждого игрока есть неограниченное количество камней. Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее 69. Победителем считается игрок, сделавший последний ход, т. е. первым получивший позицию, в которой в кучах будет 69 или больше камней.
В начальный момент в первой куче было 5 камней, во второй куче – S камней, 1 ≤ S ≤ 63. Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Ответьте на следующие вопросы:
  Вопрос 1. Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Назовите минимальное значение S, при котором это возможно.
  Вопрос 2. Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём Петя не может выиграть первым ходом, но может выиграть своим вторым ходом независимо от того, как будет ходить Ваня. Найденные значения запишите в ответе в порядке возрастания.
  Вопрос 3. Укажите минимальное значение S, при котором у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети, и при этом у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом. '''
from  functools import lru_cache

print("19:")
@lru_cache(None)
def F_19(kamni_a,kamni_b,hod_num): # hod_num - номер хода
    #1 - начала игры
    #2 - Первый ход (Петя) ЧЁТ
    #3 - Первый ход Вани Нечёт

    if kamni_a + kamni_b >= 69 and hod_num ==3:
        return True

    elif kamni_a + kamni_b < 69 and hod_num ==3:
        return False

    elif  kamni_a + kamni_b >= 69 and hod_num <3:
        return False

    return F_19(kamni_a+1,kamni_b,hod_num+1) or F_19(kamni_a,kamni_b+1,hod_num+1)  or F_19(kamni_a*2,kamni_b,hod_num+1) or F_19(kamni_a,kamni_b*2,hod_num+1)

for S in range(1,64):
    if F_19(5,S,1):
        print(S)
        break

print("20:")
@lru_cache(None)
def F_20(kamni_a,kamni_b,hod_num): # hod_num - номер хода
    #1 - начала игры
    #2 - Первый ход (Петя) ЧЁТ
    #3 - Первый ход Вани Нечёт

    if kamni_a + kamni_b >= 69 and hod_num ==4:
        return True

    elif kamni_a + kamni_b < 69 and hod_num ==4:
        return False

    elif  kamni_a + kamni_b >= 69 and hod_num <4:
        return False

    if hod_num % 2 !=0: # Сейчас ход Вани,но ретёрн для хода Пети


        return F_20(kamni_a+1,kamni_b,hod_num+1) or F_20(kamni_a,kamni_b+1,hod_num+1)  or F_20(kamni_a*2,kamni_b,hod_num+1) or F_20(kamni_a,kamni_b*2,hod_num+1)

    else: # Сейчас ход Пети,но ретёрн для хода Вани
        return F_20(kamni_a + 1, kamni_b, hod_num + 1) and F_20(kamni_a, kamni_b + 1, hod_num + 1) and F_20(kamni_a * 2,kamni_b,hod_num + 1) and F_20(kamni_a, kamni_b * 2, hod_num + 1)

for S in range(1,64):
    if F_20(5,S,1):
        print(S)



print("21:")

@lru_cache(None)
def F_21(kamni_a,kamni_b,hod_num): # hod_num - номер хода
    #1 - начала игры
    #2 - Первый ход (Петя) ЧЁТ
    #3 - Первый ход Вани Нечёт

    if kamni_a + kamni_b >= 69 and (hod_num ==5 or hod_num == 3):
        return True

    elif kamni_a + kamni_b < 69 and hod_num ==5:
        return False

    elif  kamni_a + kamni_b >= 69 and hod_num <5:
        return False

    if hod_num % 2 ==0:  # Сейчас ход Пети,но ретёрн для хода Вани


        return F_21(kamni_a+1,kamni_b,hod_num+1) or F_21(kamni_a,kamni_b+1,hod_num+1)  or F_21(kamni_a*2,kamni_b,hod_num+1) or F_21(kamni_a,kamni_b*2,hod_num+1)

    else: # Сейчас ход Вани,но ретёрн для хода Пети
        return F_21(kamni_a + 1, kamni_b, hod_num + 1) and F_21(kamni_a, kamni_b + 1, hod_num + 1) and F_21(kamni_a * 2,kamni_b,hod_num + 1) and F_21(kamni_a, kamni_b * 2, hod_num + 1)

for S in range(1,64):
    if F_21(5,S,1):
        print(S)





