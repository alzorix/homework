'''(№ 6779) (ЕГЭ-2023) У исполнителя Калькулятор имеются три команды, которым присвоены номера:

1. Вычесть 1
2. Вычесть 2
3. Найти целую часть от деления на 3

Выполняя первую из них, исполнитель уменьшает число на экране на 1, выполняя вторую – уменьшает на 2,
 выполняя третью – делит на 3 нацело, отбрасывая остаток. Сколько существует программ,
 для которых при исходном числе 19 результатом является число 3,
  и при этом траектория вычислений не содержит чисел 9 и 16? '''


def F(start,end):
    if start == end:
        return 1
    elif start<end:
        return 0
    elif start == 9 or start == 16:
        return 0
    else:
        return F(start-1,end) + F(start-2,end) + F(start//3,end)

print(F(19,3))
#180