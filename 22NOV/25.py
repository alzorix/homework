# s = 2025
ans = list()
# from fnmatch import fnmatch
# while s <= 10**10:
#     if fnmatch(str(s),"21?5846*?"):
#         ans.append((s,s//2025))
#     s+=1
#
# ans.sort()
#
# for n in ans:
#     s,r = n
#     print(s,r)



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

