'''(№ 6384) (А. Богданов) Выражение

    ALExp + DANOVq

содержит числа, записанные в системах счисления с основаниями p и q (max(p,q) < 37). Буквой x обозначена некоторая цифра
 из алфавита системы счисления с основанием p, а заглавные буквы A..Z – это цифры со значениями от 10 до 35 соответственно.
  Определите значения x, p и q, при которых значение этого выражения делится на 2023. Запишите в ответе частное от деления
  значения этого выражения на 2023 в десятичной системе счисления. '''


print((ord("A") - 55))


for p in range(22,37):
    for q in range(32, 37):
        for x in range(0, p):
                summ = ((ord("A") - 55) * p **    3     +(ord("L") - 55) * p **    2     +(ord("E") - 55) * p **    1     +x )+ ((ord("D") - 55)  * q **  4   +(ord("A") - 55)  * q **  3   +(ord("N") - 55)  * q **  2   +(ord("O") - 55)  * q **   1  +(ord("V") - 55) )
                if summ % 2023 == 0:
                    print(summ//2023)

#???


