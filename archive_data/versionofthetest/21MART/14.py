line = 7**170 + 7**100


data = list()
def toseven(num):
    F = list()

    while num != 0:
        F.append(str(num%7))
        num = num//7

    F.reverse()
    return "".join(F)

for x in range(1,2031):
    gog = line - x
    t = toseven(gog)
    data.append((t.count("0"),x))

print(max(data))
#(73, 1715)
#1715