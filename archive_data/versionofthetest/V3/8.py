from itertools import product
n = 0
s = 0
for i in product("АГИЛМНОФ",repeat = 5):
    i = "".join(i)
    n +=1
    if n %2!=0:
        if i[0]!= "Н":
            if i.count("О")<=1:
                s +=1
print(s)


