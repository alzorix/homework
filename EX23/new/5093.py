'''(№ 5079) Исполнитель Калькулятор преобразует число, записанное на экране.
У исполнителя есть три команды, которым присвоены номера:

1. Прибавь 1
2. Прибавь 2
3. Умножь на 3

Первая команда увеличивает число на экране на 1, вторая увеличивает его на 2, третья – умножает на 3.
 Программа для исполнителя – это последовательность команд. Сколько существует программ,
 которые преобразуют исходное число 2 в число 38,
  и при этом траектория вычислений содержит числа 15 и 30,
  а также не содержит чисел 12 и 20.
  Также программа не должна содержать двух команд «Умножь на 3» подряд. '''

def F(start,end,fifteen = False,thirty = False,ymnojThree = False):
    if start == 15:
        fifteen = True
    if start == 30:
        thirty = True
    if start == 12:
        return False
    if start == 20:
        return False


    if start == end and fifteen and thirty:
        return 1
    if start == end:
        return 0
    elif start>= end:
        return 0
    else:
        if ymnojThree :
            return F(start + 1, end, fifteen, thirty, False) + F(start + 2, end, fifteen, thirty, False)

        else:
            return F(start+1,end,fifteen,thirty,False) + F(start+2,end,fifteen,thirty,False) + F(start*3,end,fifteen,thirty,True)

print(F(2,38))

#1243550