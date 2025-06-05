from math import sqrt
def delitels(num):

    delitels = set()

    K = int(sqrt(num))+1
    for n in range(1,K+1):
        if num % n == 0:
            delitels.add(n)
            delitels.add(num//n)
    return sum(delitels)

ans = list()
for INTiche in range(500_001,1_700_000):
    if len(ans) < 5:
        R = delitels(INTiche)
        if str(R)[-1] == "6":
            ans.append((INTiche,R))
    else:
        break

for x,y in ans:
    print(x,y)
#500032 1070356
#500035 606816
#500039 501456
#500050 949716
#500052 1333696