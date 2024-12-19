'''(№ 6187) (Р. Сорокин) Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 5, если n ≤ 2
F(n) = F(n-2) + n, если n > 2.

Чему равно значение F(23023)? '''
class data():
    def __init__(self):
        self.data= dict()
    def push(self,n,res):
        self.data[n]=res
    def give(self,n):
        return self.data[n]

data = data()

def F(n):
    if n <=2:
        data.push(n,5)
    else:
        s = data.give(n-2)
        data.push(n,  s + n   )

for i in range(1,23024):
    F(i)

print(data.give(23023))
#132526148