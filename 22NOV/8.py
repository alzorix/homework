from itertools import product
count = 0
for n in product("ВЬЮГА", repeat = 6):
    s = "".join(n)
    if s.count("ЮГ"):
        count+=1
print(count)

count = 0
for n in product("ВЬЮГА", repeat = 6):
    s = "".join(n)
    if "ЮГ" in s:
        count+=1
print(count)


#2976
# Ошибок не обнаружено