from itertools import product
F = list()
F.append("")
for i in product("1234567890",repeat = 1):
    F.append("".join(i))
for i in product("1234567890",repeat = 2):
    F.append("".join(i))
# for i in product("1234567890",repeat = 3):
#     F.append("".join(i))
# for i in product("1234567890",repeat = 4):
#     F.append("".join(i))


S = list()
for quest in range(0,10):
    quest = str(quest)
    for quest2 in range(0, 10):
        quest2 = str(quest2)
        for quest3 in range(0, 10):
            quest3 = str(quest3)


            for star in F:

                    line = "89" + star + "4" +quest + "5" + quest2 + "7" + quest3


                    if int(line) % 8993 == 0:
                            S.append((int(line),int(line) // 8993))
S.sort()
for i in range(len(S)):
    d,f = S[i]

    print(d,f)

# 8912485671 991047
# 8915435375 991375
# 8917485779 991603
# 8934455570 993490
# 8937405274 993818
# 8939455678 994046
# 8958475873 996161
# 8961425577 996489
# 8980445772 998604