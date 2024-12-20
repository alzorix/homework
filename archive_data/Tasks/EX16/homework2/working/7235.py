'''(№ 7235) (М. Паршиков) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = n, если n ≥ 3000,
F(n) = n + 2x  + F(n + 2), если n < 3000.

При каком целом значении x выполняется равенство F(28) – F(34) = 324?


Показать ответ'''


F = dict()

for n in range(3000,3005):
    F[n] = (n,0)
    print(F[n])
for n in range(2999,25,-1):
    c = F[n+2]
    x_count = c[1] +2
    F[n] = (n + c[0],x_count)


for x in range(0,1000):
    xS = (F[28][1] - F[34][1])*x
    line = F[28][0] - F[34][0] +xS
    if line == 324:
        print(x)
        exit()

#39
