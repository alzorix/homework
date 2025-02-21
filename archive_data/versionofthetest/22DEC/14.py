
def toNine(n):
    FutureLine = list()
    while n !=0:
        FutureLine.append(str(n%9))
        n = n//9
    FutureLine.reverse()
    return "".join(FutureLine)



magic_digits = 9**2024 + 9 **1987
c = 0
for x in range(2024,0,-1):
    fist = magic_digits - x
    if toNine(fist).count("8") == 1984:
        print(x)
        exit()



#2017
# Ошибок не обнаружено