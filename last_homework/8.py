from itertools  import product
count = 0
for i in product("АИМРЯ",repeat = 4):
    count +=1
    if i == "АРИЯ":
        print(count)
#42