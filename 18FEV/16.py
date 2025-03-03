from functools import lru_cache
F = dict()


for x in range(1,10):
    F[2000+x] = 16

for x in range(2000,0,-1):
    F[x] = 2* F[x+3]



def proiz(s:str):
    summ = 1
    for x in s:
        if int(x) != 0:
            summ =summ * int(x)
    return summ

print(proiz(str( F[50]// F[110])))
#6720