from itertools import product
c = 0
lss = list()
for l in product("КОСУФ",repeat =5):
    line = "".join(l)
    c+=1
    if "Ф" not in line and line.count("У") == 2:
        lss.append(c)
print(max(lss))
