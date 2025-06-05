F = [0]*3000
for x in range(2025,2050):
    F[x] = x

for x in range(2024,-1,-1):
    F[x] = 2*x +F[x+2]

print(F[82] - F[81])
#1945
