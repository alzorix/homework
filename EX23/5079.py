''' 	(№ 5079) Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера:

1. Прибавь 1
2. Прибавь 2
3. Умножь на 3

Первая команда увеличивает число на экране на 1, вторая увеличивает его на 2,
 третья – умножает на 3. Программа для исполнителя – это последовательность команд.
  Сколько существует программ, которые преобразуют исходное число 2 в число 38,
   и при этом траектория вычислений содержит числа 15 и 30, а также не содержит чисел 12 и 20.
    Также программа не должна содержать двух команд «Умножь на 3» подряд. '''


def F(start:int,end:int,pyatnadcat:bool= False,tridtat:bool= False):

    if start == 12 or start == 20:
        return 0

    if start == 15:
        pyatnadcat = True
    if start == 30:
        tridtat = True

    if start == end and tridtat and pyatnadcat:
        return 1
    elif start == end:
        return 0
    elif start > end :
        return 0
    else:
        return F(start+1,end,pyatnadcat,tridtat) + F(start+2,end,pyatnadcat,tridtat) + F(start*3,end,pyatnadcat,tridtat)


print(F(2,38))

#1243550