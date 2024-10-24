from itertools import product as p
count = 0
for i in p("БЕНРСТЬЯ",repeat = 5):
    count +=1

    if i[0] == "Р" and "Ь" not in i:
        if count % 2 ==0:
            print(count)

#С РНО 16384