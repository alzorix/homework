from itertools import product

alfabet = list()
alfabet.append("")
for x in product("0123456789",repeat=1):
    alfabet.append("".join(x))
for x in product("0123456789",repeat=2):
    alfabet.append("".join(x))
for x in product("0123456789",repeat=3):
    alfabet.append("".join(x))
for x in product("0123456789",repeat=4):
    alfabet.append("".join(x))
for x in product("0123456789",repeat=5):
    alfabet.append("".join(x))

alfabet0 = list()
alfabet0.append("")
for x in product("123456789",repeat=1):
    alfabet0.append("".join(x))
for x in product("123456789",repeat=2):
    alfabet0.append("".join(x))
for x in product("123456789",repeat=3):
    alfabet0.append("".join(x))
for x in product("123456789",repeat=4):
    alfabet0.append("".join(x))
for x in product("123456789",repeat=5):
    alfabet0.append("".join(x))
FLAG = False
result = list()
chisl = 10**11
for star1 in alfabet0:
    for star2 in alfabet:
        if FLAG:
            FLAG = False
            break
        for quest in range(10):
            stroka = star1+ "192" + str(quest) + "3" + star2 + "68"

            if stroka[0] !="0":
                int_stroka =  int(stroka)
                if int_stroka < chisl:
                    if int_stroka % 154682 == 0:
                        result.append((int_stroka,int_stroka//154682))
                else:
                    FLAG = True
                    break

result.sort()
for x in result:
    s1,s2 = x
    print(s1,s2)

# 11419243968 73824
# 19253887268 124474
# 31922343068 206374
# 65519273468 423574
# 76192331468 492574



