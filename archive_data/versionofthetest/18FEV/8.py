from  itertools import product
last = None
id =0
for x in product("ГЕИНРСЯ",repeat = 6):
    id+=1
    l = "".join(x)
    if "ГИРЯ" in l:
        last = id
print(last)
#115381
