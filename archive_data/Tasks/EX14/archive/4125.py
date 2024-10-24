'''(№ 4125) (А. Богданов) Значение выражения 81**18 – (81**8 – 1)∙((8 + 1)**8 + 1) // 8 – 8 записали в системе счисления с основанием 3.
Найдите количество единиц в этой записи. '''

def ABSOLUTESOLVER(NUM,CHIL):
    F = list()
    while NUM != 0:
        F.append( str(NUM% CHIL))
        NUM = NUM // CHIL
    F.reverse()
    return "".join(F)

print(ABSOLUTESOLVER(81**18 - (81**8 - 1)*((8 + 1)**8 + 1) // 8 - 8,3).count("1"))