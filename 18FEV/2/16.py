F = dict()

for x in range(2001,2050):
    F[x] = 16
for x in range(2000,0,-1):
    F[x] = 2* F[x+3]

s = str(F[50]//F[110])
c = 1
for x in s:
    if x != "0":
        c*=int(x)
print(c)
#6720
