'''(№ 6557) (А. Богданов) Два игрока, Папа и Ваня, играют в следующую игру. Перед игроками лежит куча камней.
 Игроки ходят по очереди,
 первый ход делает Папа. За один ход игрок может добавить в кучу семь камней или увеличить количество камней в куче
 в два раза.
  Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней. Игра завершается в тот момент,
   когда количество камней в куче становится не менее 100. Победителем считается игрок, сделавший последний ход,
    т.е. первым получивший кучу из 100 или больше камней. В начальный момент в куче было S камней, 1 ≤ S ≤ 99.
Ответьте на следующие вопросы:
  Вопрос 1. Укажите максимальное значение S, при котором Папа может выиграть своим первым ходом, но поддается,
   и Ваня выигрывает своим первым ходом.
  Вопрос 2. Найдите два наименьших значения S, при которых у Папы нет выигрышной стратегии, а у Вани есть.
   Но Ваня ошибается и у Папы нет возможности еще раз поддаться он вынужден выиграть.
   Найденные значения запишите в ответе в порядке возрастания.
  Вопрос 3. Найдите минимальное значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Папы;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом. '''


print("19:")
def F(A,H):
    if A >=100 and H == 3:
        return True
    elif A >= 100 and H != 3:
        return False
    elif A < 100 and H == 3:
        return False


    return F(A+7,H+1) or F(A*2,H+1)
#92
def F_(A,H):
    if A >= 100 and H == 2:
        return True
    elif A >= 100 and H != 2:
        return False

    elif A < 100 and H == 2:
        return False

    return F(A + 7, H + 1) or F(A * 2, H + 1)

for S in range(1,100):
    if F(S,1) and F_(S,1):
        print(S)
        #92

#Как ответить на второй вопрос?

'''  Вопрос 2. Найдите два наименьших значения S, при которых у Папы нет выигрышной стратегии, а у Вани есть.
   Но Ваня ошибается и у Папы нет возможности еще раз поддаться он вынужден выиграть.
   Найденные значения запишите в ответе в порядке возрастания.'''

print("20:")
def F(A,H):
    #Papa
    #Vanya
    if A >=100 and H == 3:
        return True
    elif A >= 100 and H != 3:
        return False
    elif A < 100 and H == 3:
        return False

    if H % 2 == 0:
        return F(A+7,H+1) or F(A*2,H+1)
    else:
        return F(A+7,H+1) and F(A*2,H+1)
def F_(A,H):
    #Papa
    #Vanya
    if A >=100 and H == 4:
        return True
    elif A >= 100 and H != 4:
        return False
    elif A < 100 and H == 4:
        return False


    if H % 2 == 0:
        return F_(A+7,H+1) or F_(A*2,H+1)
    else:
        if H != 1:
            return F_(A+7,H+1) and F_(A*2,H+1)
        else:
            return F_(A + 7, H + 1) or F_(A * 2, H + 1)

for S in range(1,100):
    if F(S,1) :
        print(S,F_(S,1))



# 43 44




'''  Вопрос 3. Найдите минимальное значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Папы;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом. '''


print("21:")
def F_(A, H):
    if A >= 100 and H == 3:
        return True
    elif A >= 100:
        return False
    if H % 2 == 0:
        return F_(A + 7, H + 1) or F_(A * 2, H + 1)
    else:
        return F_(A + 7, H + 1) and F_(A * 2, H + 1)

def F(A, H):
    if A >= 100 and (H == 3 or H == 5):
        return True
    elif A >= 100:
        return False
    if H % 2 == 0:
        return F(A + 7, H + 1) or F(A * 2, H + 1)
    else:
        return F(A + 7, H + 1) and F(A * 2, H + 1)

for S in range(1, 100):
    if F(S, 1) and not F_(S, 1):
        print(S)
#29