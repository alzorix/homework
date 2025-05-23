'''(№ 5884) (В. Петров) Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть три команды,
 которым присвоены номера:
1. Прибавь 1
2. Умножь на 2
3. Умножь на 3
Первая команда увеличивает число на экране на 1, вторая умножает его на 2, третья – умножает на 3.
Программа для исполнителя – это последовательность команд.
 Определите длину самой короткой программы, которая преобразует число 1 в число 9217
  и содержит ровно 30 команд "Прибавь 1".
 Под длиной программы понимается количество команд, входящих в неё. '''
from functools import lru_cache
s = set()
@lru_cache(None)
def F(start,end,history=0,count = 0):
    if history >30:
        return 0



    if start == end and history == 30:
        s.add(count)
        return 1
    elif start >= end:
        return 0
    else:
        return F(start+1,end,history+1,count+1) + F(start*2,end,history,count+1) + F(start*3,end,history,count+1)
print(F(1,9217))
print(min(s))
#Ошибка. Я так понимаю,тут нужно писать как-то по-другому?