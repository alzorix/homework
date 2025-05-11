'''(№ 3101) У исполнителя Калькулятор три команды, которым присвоены номера:

1. прибавь 1
2. умножь на 2
3. умножь на 3

Сколько есть программ, которые число 1 преобразуют в число 14? '''

def F(start,end):
    if start == end:
        return 1
    elif start > end:
        return  0
    else:
        return F(start+1,end) + F(start*2,end) + F(start*3,end)

print(F(1,14))
#48