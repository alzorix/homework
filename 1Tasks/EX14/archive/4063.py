'''(№ 4063) (В. Шелудько) Значение выражения 7**103 + 6∙7**104 – 3∙7**57 + 98 записали в системе счисления с основанием 7. Сколько цифр 6 содержится в этой записи? '''

def ABSOLUTESOLVER(num,shisla):
    F = list()
    while num != 0:
        F.append(str(num % shisla))
        num = num // shisla
    F.reverse()
    return "".join(F)



a = 7**103 + 6*7**104 -3*7**57 + 98
print(ABSOLUTESOLVER(a,7).count("6"))