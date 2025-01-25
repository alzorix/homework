F = dict()
for x in range(5):
    F[x] = x
for x in range(5,14000):
    F[x] = 2*x * F[x-4]

print(  ( F[13766] - 9* F[13762]                  ) // F[13758]                          )

#757543052
