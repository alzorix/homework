'''(№ 7379) (М. Шагитов) У исполнителя Калькулятор имеются три команды,
 которые обозначены латинскими буквами:

A. Прибавить 1
B. Прибавить 4
C. Умножить на 2

Программа для исполнителя – это последовательность команд, каждая из которых изменяет число.
 Требуется найти количество таких программ, которые преобразуют исходное число 1 в число 50,
  и при этом траектория вычислений содержит ровно одно из чисел 8, 16, или 32. '''


def F(start=1,end=50,chislo=False):
    if (start == 8 or start == 16 or start == 32) and chislo:
        return 0
    if start == 8 or start == 16 or start == 32:
        chislo = start

    if start == end and chislo:
        return 1
    if start == end:
        return 0
    if start >end:
        return 0
    return F(start+1,end,chislo) + F(start+4,end,chislo) + F(start*2,end,chislo)
print(F())
#6370599