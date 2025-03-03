s = 7 ** 270 + 7 ** 170 + 7**70

def absolutesolver(x):
    F = list()
    while x !=0:
        F.append(str(x%7))
        x = x//7
    F.reverse()
    return "".join(F)
res = list()
for x in range(1,10000+1):

    s  = s -x
    r = absolutesolver(s)
    res.append((r.count("0"), x) )
#res.sort()
print(max(res))
#9603

