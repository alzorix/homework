'''(№ 6501) У исполнителя Калькулятор имеются три команды, которым присвоены номера:

1. прибавь 1
2. прибавь 2
3. умножь на 3

Выполняя первую из них, исполнитель увеличивает число на экране на 1, выполняя вторую – увеличивает на 2,
 выполняя третью – умножает на 3. Сколько существует различных программ, преобразующих число 1 в число 43
 и содержащих не более трёх команд 1, при выполнении которых траектория вычислений содержит число 25 и не
 содержит чисел 10 и 38? '''

def F(start=1,end=43,fist=0,twentyfive=0):
    if start == 10 or start == 38:
        return 0
    if start == 25:
        twentyfive+=1


    if start == end and fist<= 3 and twentyfive:
        return 1

    if fist >3:
        return 0
    if start == end:
        return 0
    if start > end:
        return 0
    return F(start+1,end,fist+1,twentyfive) + F(start+2,end,fist,twentyfive) + F(start*3,end,fist,twentyfive)

print(F())
#434 Намного дольше обычного
