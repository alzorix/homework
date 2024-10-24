'''(№ 4889) (П. Волгин) Значение выражения 9**81 + 27**729 – 4 записали в системе счисления с основанием 9.
 Затем все нули заменили на максимальную цифру в этой записи. Определите, сколько раз встречается максимальная цифра в этой записи после преобразования. '''

def ABSOLUTESOLVER(c,n):
    f = list()
    global max
    max = 0
    while c != 0:

        f.append(str(c%n))

        if c % n > max:
            max =  c % n
        c = c //n

    f.reverse()

    return "".join(f).replace("0",str(max))

print(ABSOLUTESOLVER(9**81 + 27**729 - 4,9).count(str(max)))


