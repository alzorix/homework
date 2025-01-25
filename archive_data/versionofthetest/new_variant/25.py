# 7 занятых 3 свободных

alfabet_simple = list()
alfabet = list()
for i in range(10):
    alfabet_simple.append(str(i))
    alfabet.append(str(i))

from itertools import product


for x in product("1234567890",repeat = 2):
    alfabet.append("".join(x))
for x in product("1234567890",repeat = 3):
    alfabet.append("".join(x))
print(alfabet)


ans = list()

for a1 in alfabet_simple:
    for a2 in alfabet_simple:
        for q in alfabet:
            line = int(f"54{a1}1{a2}3{q}7")
            if line % 18579 ==0 :



                ans.append((line,line//18579))

ans.sort()

for x in ans:
    s,r = x
    print(s,r)


# 545163597 29343
# 5411932647 291293
# 5421036357 291783
# 5451134337 293403
# 5461538577 293963
# 5481232317 295023
# 5491636557 295583