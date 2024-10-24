

from fnmatch import *
termos = 0
for i in range(0,680_000):
    if i % 8 ==0:
        if fnmatch(str(i),"1*2*"):
            termos+=1
print(termos)