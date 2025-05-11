F = dict()
F[1] = 1

for n in range(2,2030):
    F[n] = (n-1)*F[n-1]

print( (F[2024] + 2* F[2023] ) // F[2022] )