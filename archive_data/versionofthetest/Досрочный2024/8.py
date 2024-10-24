from itertools import product
a = 1
for i in product("АПРСУ",repeat = 5):
    s = "".join(i)
    if s.count("АА") == 0:
        if s.count("У") <2:
            print(a)
            break
    a +=1