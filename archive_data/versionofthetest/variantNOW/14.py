
def AbsoluteSolver(num):
    F = list()
    while num != 0:
        F.append(str(num%5))
        num = num//5

    F.reverse()

    return "".join(F)
data = list()

for x in range(1,2006):
    source = 5**150+5**98-x
    res = AbsoluteSolver(source)

    ysl = str(res).count("0")
    data.append((ysl,x))
print(max(data))
#1875