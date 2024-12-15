'''(№ 6641) (Е. Джобс) Алгоритм вычисления функций F(n) и G(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 1 , если n ≥ 3210,
G(n) = n, если n < 10.
F(n) = F(n+3) + 7, если n<3210,
G(n) = G(n–3) + 5, если n ≥ 10.

Чему равно значение выражения F(15) – G(3000)? '''

class Data:
    def __init__(self):
        self.data = dict()
    def push(self,n,res):
        self.data[n] = res
    def get(self,n):
        return self.data[n]

F = Data()
G = Data()

for i in range(3210,3300):
    F.push(i,1)

for i in range(3209,14,-1):
    F.push(i, F.get(i+3) + 7    )

for n in range(1,10):
    G.push(n,n)

for n in range(10,3001):
    G.push(n, G.get(n-3) +5    )

print(F.get(15)- G.get(3000))

#2462
