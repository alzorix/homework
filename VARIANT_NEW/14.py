
print(chr(ord("A")+15))
alfabet = dict()
for p in range(0,15) :
    alfabet[10+p] = chr(ord("A")+p)

def absolute_solver(num):
    num = int(num)
    F = list()
    while num!=0:
        t = num%25
        if t in alfabet.keys():
            F.append(alfabet[t])
        else:
            F.append(str(t))
        num = num//25
    F.reverse()
    return "".join(F)
line = 25**150+25**100
ans = list()
for x in range(1,2501):
    line = line-x
    t = absolute_solver(line)
    print(t)
    ans.append((t.count("0"),-x))

ans.sort(reverse=True)
print(ans)
print(ans[0])
#1249