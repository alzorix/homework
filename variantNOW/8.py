from itertools import product
chet = set()
nechet = set()
for x in product("02468",repeat =2):
    chet.add("".join(x))
for y in product("13579",repeat =2):
    nechet.add("".join(y))
c = 0
for chislo in range(1000,10000):
    FLAG = True
    str_chislo = str(chislo)
    for test in chet:
        if test in str_chislo:
            FLAG = False
            break
    for test in nechet:
        if test in str_chislo:
            FLAG = False
            break

    s = [n for n in str_chislo]
    s.sort()
    ss = set(s)
    ss = list(ss)
    ss.sort()
    if s == ss:
        if FLAG:
            c+=1
print(c)
#720
