'''(№ 5545) (К. Багдасарян) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 1, если n < 3
F(n) = F(n – 1) + F(n – 2), если n > 2.

Чему равно значение выражения (F(1006) – F(1004)) / F(1005)? '''

class Database:
    def __init__(self):
        self.data = dict()

    def push(self,n,result):
        self.data[n] = result

    def give_info(self,n):
        return self.data.get(n)

data = Database()

'''F(n) = 1, если n < 3
F(n) = F(n – 1) + F(n – 2), если n > 2.'''

def F(n):
    if n<3:
        return 1
    else:
        return (data.give_info(n-1) +data.give_info(n-2))



for i in range(-5,1007):
    data.push(i,F(i))
'''Чему равно значение выражения (F(1006) – F(1004)) / F(1005)?'''
print((data.give_info(1006) - data.give_info(1004))//data.give_info(1005))
#1