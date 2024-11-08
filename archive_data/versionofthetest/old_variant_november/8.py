from itertools  import product
count = 0
for i in product("АИМРЯ",repeat = 4):
    count +=1
    i = "".join(i)
    if i == "АРИЯ":
        print(count)