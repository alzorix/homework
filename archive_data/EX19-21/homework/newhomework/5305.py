'''(№ 5305) (Е. Джобс) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя.
 За один ход игрок может увеличить количество камней в куче в целое число раз (но не более, чем на 80 камней)
 или добавить в кучу десять камней или добавить в кучу два камня.
  Например, из кучи из 10 камней можно получить кучу из 12, 20, 30, 40, 50, 60, 70, 80 и 90 камней. Для того чтобы делать ходы,
  у каждого игрока есть неограниченное количество камней. Выигрывает тот игрок, после хода которого количество камней в куче становится не менее 166.
В начальный момент в куче было S камней; 1 ≤ S ≤ 165. Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Ответьте на следующие вопросы:
  Вопрос 1. Известно, что Петя выиграл своим вторым ходом после неудачного хода Вани.
  При каком минимальном значении S такое возможно?
  Вопрос 2. Известно, что Петя имеет выигрышную стратегию. Укажите минимальное и максимальное значения при которых Петя не может победить первым ходом,
   но при любом ходе Вани Петя побеждает своим вторым ходом.
  Вопрос 3. Известно, что Ваня имеет выигрышную стратегию за один или два хода, при этом не имеет выигрышной стратегии в один ход.
   Найдите минимальное значение S, при котором это возможно.
'''
#Внимание,перед решением задачи,я узнал про существование yield. На этом всё
def F(A,H):

    if A >= 166 and H == 4:
        return True
    if A >= 166 :
        return False
    if H ==4:
        return False

    Flist = list()
    Flist.extend(ReturnListwithreturns(A,H))
    Flist.append(F(A+2,H+1))
    Flist.append(F(A + 10, H + 1))
    return any(Flist)


def ReturnsGenerator(A,H):
    x = 2
    while (A * x - A) <= 80:


        yield F(A*x,H+1)
        x+=1
def ReturnListwithreturns(A,H):
    ans = list()
    a = ReturnsGenerator(A,H)
    try:
        while True:
            ans.append(next(a))
    except StopIteration:
        return ans

for S in range(1,166):

    if F(S,1):
        print(S)
        break

'''Вопрос 2. Известно, что Петя имеет выигрышную стратегию. Укажите минимальное и максимальное значения при которых Петя не может победить первым ходом,
   но при любом ходе Вани Петя побеждает своим вторым ходом.'''
print("20:")
def F(A,H):

    if A >= 166 and H == 4:
        return True
    if A >= 166 :
        return False
    if H ==4:
        return False

    Flist = list()
    Flist.extend(ReturnListwithreturns(A,H))
    Flist.append(F(A+2,H+1))
    Flist.append(F(A + 10, H + 1))
    if H % 2 ==0:
        return all(Flist)
    if H % 2 !=0:
        return any(Flist)


for S in range(1, 166):

    if F(S, 1):
        print(S)
#77 153

'''  Вопрос 3. Известно, что Ваня имеет выигрышную стратегию за один или два хода, при этом не имеет выигрышной стратегии в один ход.
   Найдите минимальное значение S, при котором это возможно.'''


def F(A,H):

    if A >= 166 and H == 3:
        return True
    if A >= 166 :
        return False
    if H ==3:
        return False

    Flist = list()
    Flist.extend(ReturnListwithreturns(A,H))
    Flist.append(F(A+2,H+1))
    Flist.append(F(A + 10, H + 1))
    if H % 2 ==0:
        return any(Flist)
    if H % 2 !=0:
        return all(Flist)

def ReturnsGenerator_(A,H):
    x = 2
    while (A * x - A) <= 80:


        yield F_(A*x,H+1)
        x+=1
def ReturnListwithreturns_(A,H):
    ans = list()
    a = ReturnsGenerator_(A,H)
    try:
        while True:
            ans.append(next(a))
    except StopIteration:
        return ans
def F_(A,H):

    if A >= 166 and( H == 3 or H== 5):
        return True
    if A >= 166 :
        return False
    if H ==5:
        return False

    Flist = list()
    Flist.extend(ReturnListwithreturns_(A,H))
    Flist.append(F_(A+2,H+1))
    Flist.append(F_(A + 10, H + 1))
    if H % 2 ==0:
        return any(Flist)
    if H % 2 !=0:
        return all(Flist)
print("21:")
for S in range(1, 166):

    if F_(S, 1) and not(F(S, 1) ):
        print(S)
        break