from  itertools import  product
a = 0
for i in product("АВЕСТ",repeat = 5):
    a = a + 1
    if "".join(i) == "СВЕТА":
        print(a)