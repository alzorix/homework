from itertools import product

starlist = list()
starlist.append("")
for i in product("0123456789",repeat= 1):
    starlist.append("".join(i))
for i in product("0123456789",repeat= 2):
    starlist.append("".join(i))
for i in product("0123456789", repeat=3):
    starlist.append("".join(i))

res = list()
for quest in range(0,10):
    for star in starlist:
        S = "1" + star + "2322"+ str(quest) +"2"
        S = int(S)
        if S % 2024 ==0:
            res.append((S, S // 2024))
res.sort()
for i in range(len(res)):
    r,s = res[i]
    print(r,s)
