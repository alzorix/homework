'''(№ 5603) (А. Куканова) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = n - 10000, если n > 10000,
F(n) = F(n + 1) + F(n + 2), если 1 ≤ n ≤ 10000.

Чему равно значение выражения F(12345)·(F(10) − F(12)) / F(11) + F(10101)? '''


class Data:
    def __init__(self):
        self.data = dict()
    def push(self,n,res):
        self.data[n] = res
    def get_info(self,n):
        return self.data[n]


'''F(n) = n - 10000, если n > 10000,
F(n) = F(n + 1) + F(n + 2), если 1 ≤ n ≤ 10000.
'''
data = Data()
def F(n):
    if n > 10_000:
        return n-10_000
    else:
        return   data.get_info(n+1) + data.get_info(n+2)       # n - и так натуральное, проверка на 1 не нужна

'''F(12_345)·(F(10) − F(12)) / F(11) + F(10_101)'''
for i in range(12_350,0,-1): #n - натуральное
    data.push(i,F(i))

print(data.get_info(12_345) * (data.get_info(10) - data.get_info(12)) // data.get_info(11) + data.get_info(10101)    )

#2446