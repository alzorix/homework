print("* 16 **    +".join("x1x"))
print("* 8 **    +".join("x3x3"))


def ThisTwo(two):
    while two % 2 == 0:
        two = two  //2
    if two ==1:
        return True
    return False
TwoList = list()



for i in range(0,9999):
    TwoList.append(2**i)
#print(len(TwoList))


for x in range(1,8):
    R = (x* 16 ** 2   +1* 16 **   1 +x) + (x* 8 **  3  +3* 8 **  2  +x* 8 **   1 +3)
    if ThisTwo(R):
        print(x)
    if R in TwoList:
        print(x)
    #print(R)

# В чем проблема?