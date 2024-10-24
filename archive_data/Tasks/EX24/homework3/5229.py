
A = [    "A"    ,    "B"      ,      "X"    ]


maxx = list()
count_maxx = 0
count = 0

with open("5229") as lines:
    line = lines.readline().strip()

    for i in line:
        count_maxx += 1
        if i in A:
            count+=1


        if count > 5:
            count = 0
            maxx.append(count_maxx)
            count_maxx = 0
print(max(maxx))
# почему отличается на 1



