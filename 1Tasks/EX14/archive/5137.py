'''(№ 5137) (П. Волгин) Значение выражения 8**888 + 15·15**1515 – 2**444 записали в системе счисления с основанием 8. Определите количество комбинаций цифр 7# в этой записи,
где # – любая цифра от 1 до 6. '''

def ABSOLUTESOLVER(NUMBER,SYSTEM):
    F = list()
    while NUMBER != 0:
        F.append(str(NUMBER%SYSTEM))
        NUMBER = NUMBER//SYSTEM
    F.reverse()
    return "".join(F)
a = ABSOLUTESOLVER(8**888 + 15*15**1515 - 2**444,8)
print(a.count("71") + a.count("72") + a.count("73") + a.count("74") + a.count("75") + a.count("76"))