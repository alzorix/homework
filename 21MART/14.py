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
    line = line - x
    t = toseven(line)
    data.append((t.count("0"),x))

print(max(data))
#(75, 1813)
#1813