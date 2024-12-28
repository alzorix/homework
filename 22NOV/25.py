
ans = list()

print(str(10**10).count("0"))

'''6 чисел и 4 своб членов'''

alfabet = list()
from itertools import product
for i in product("0123456789",repeat = 1):
    alfabet.append("".join(i))
for i in product("0123456789",repeat = 2):
    alfabet.append("".join(i))
for i in product("0123456789",repeat = 3):
    alfabet.append("".join(i))


a_alfabet = list()

for i in product("0123456789",repeat = 1):
    a_alfabet.append("".join(i))

for x1 in a_alfabet:
    for a2 in alfabet:
        for x in a_alfabet:
            s = int("21" + x1 + "5846" +a2 + x)
            r = 10**10
            if int(s) <=r:
                if s % 2025 ==0:
                    ans.append((s,s//2025))

ans.sort()
for n in ans:
    s,r = n
    print(s,r)

#2105846100 1039924
# 2135846475 1054739
# 2165846850 1069554
# 2175846300 1074492

# Ошибок не обнаружено