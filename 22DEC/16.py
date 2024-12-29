F = dict()

for n in range(4):
    F[n] = n-1

for n in range(4,4970):
    if n % 2 ==0:
        F[n] = F[n-2] + n//2 - F[n-4]
    else:
        F[n] = F[n-1] * n + F[n-2]

print(F[4952] + 2* F[4958] + F[4964])
#9920
