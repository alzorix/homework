
def toNine(n):
    FutureLine = list()
    while n !=0:
        FutureLine.append(str(n%9))
        n = n//9
    FutureLine.reverse()
    return "".join(FutureLine)



magic_digits = 9**2024 + 9 **1987
c = 0
for x in range(2024,1,-1):
    magic_digits = magic_digits - x
    if toNine(magic_digits).count("8") == 1984:
        print(x)
        exit()



#2008
# Ошибок не обнаружено