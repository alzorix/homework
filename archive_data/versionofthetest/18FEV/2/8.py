from itertools import product, repeat
l = 0
c=0
for x in product("ГЕИНРСЯ",repeat=6):
    c+=1
    line = "".join(x)
    if "ГИРЯ"  in line:
        l = c
print(l)
#115381