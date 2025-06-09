

F = [0]

for n in range(1,30000):
    r = 3*n + F[n-1]
    F.append(r)
    if r > 17505321:
        print(r)
        print(n)
        exit()
#3416