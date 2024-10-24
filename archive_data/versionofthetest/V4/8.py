from itertools import product
n = 0
num = 0
for i in product("АГЕИЛНРТ",repeat = 5):
    i = "".join(i)
    n +=1
    #print(n,i)
    if n %2 != 0:
        #print(1)
        if  i[0] != "Т":
           # print(2)
            if i.count("Н") < 3 :
                if  i.count("Н") > 0:

                    num +=1
print(num)

