''' 	(№ 3673) (П.М. Волгин) Значение арифметического выражения 26**2 + 169 - 11 записали в системе счисления с основанием
13. В этой записи помимо цифр от 0 до 9 могут встречаться цифры из списка: А, B, С,
 которые имеют числовые значения от 10 до 12 соответственно. Сколько цифр C и цифр
 2 встречается в этой записи? '''

def ABSOLUTESOLVER(NUM,CHISLO):
    dic = {10: "a", 11: "b", 12: "c"}
    F = list()
    while NUM != 0:

        if NUM % CHISLO > 9:
            F.append(dic.get(NUM % CHISLO))
        else:
            F.append(str(NUM % CHISLO))
        NUM = NUM // CHISLO

    return "".join(F)







a = 13

temp = ABSOLUTESOLVER(26**2 + 169 - 11,a)
print(temp.count("c") + temp.count("2"))