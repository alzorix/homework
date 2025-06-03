'''(№ 4813) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1) Вычисляется сумма S1 всех нечётных цифр десятичной записи числа N. Если нечётных цифр нет, сумма S1 считается равной 0.
2) Вычисляется сумма S2 всех цифр десятичной записи числа N, стоящих в чётных разрядах. Разряды нумеруются справа налево, начиная с 0.
3) Вычисляется результат R как модуль разности S1 и S2.
Например, N = 1234. Сумма нечётных цифр S1 = 1 + 3 = 4. Сумма цифр в чётных разрядах S2 = 2 + 4 = 6. Результат работы алгоритма R = 6 – 4 = 2.
Укажите наименьшее число, в результате обработки которого по данному алгоритму получится число 29. '''

for N in range(1,9999):
    resnechet = 0
    reschet = 0
    tempshet = list()
    tempnchet = list()
    strN = str(N)
    for i in range(len(strN)):

        if int(strN[i]) % 2 != 0:
            tempnchet.append(strN[i])
        else:
            tempshet.append(strN[i])



    if len(tempnchet) == 0:
        resnechet = 0


    else:
        for i in range(len(tempnchet)):
            resnechet = int(tempnchet[i]) + resnechet

    for i in range(len(tempshet)):
        reschet = int(tempshet[i]) + reschet

    result = resnechet - reschet
    if result < 0:
        result = -result
