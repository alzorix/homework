from  itertools import product
a1 = list()
for x in product("13579",repeat= 2):
    a1.append("".join(x))
for x in product("24680",repeat= 2):
    a1.append("".join(x))
c = 0
for x in range(1000,10_000):

    flag = False

    temp = [t for t in str(x)]

    if len(temp) == len((list(set(temp)))):
        flag = True

    for s in a1:
        if s in str(x):
            flag = False
    if flag == True:
        c+=1
print(c)
#720