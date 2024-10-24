a = ["0","1","2","3","4","5","6","7","8","9"]
a2 = ["0","1","2","3","4","5","6","7","8","9",""]
count = 0

from math import sqrt
def isdel(num):
    num = int(num)
    sqrtnunm = int(sqrt(num))
    for i in range(2,sqrtnunm+1):
        if num%i == 0:
            return True
    return False


F = list()


for a1 in a:
    for star in a2:
        line = "3"+a1+"1111"+ star
        if isdel(line):
            None
        else:
            F.append(int(line))
F.sort()
for i in F:
    print(i)

# 311111
# 361111
# 3011117
# 3011119
# 3311117
# 3611119
# 3811117
# 3911111

#Ответ верный