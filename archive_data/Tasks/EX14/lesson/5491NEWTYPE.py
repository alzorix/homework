'''(№ 5491) (А. Богданов) Операнды арифметического выражения записаны в системе счисления с основанием 15.

82x19₁₅ – 6x073₁₅

В записи чисел переменной x обозначена неизвестная цифра из алфавита 15-ричной системы счисления. Определите наименьшее
значение x, при котором значение данного арифметического выражения кратно 11. Для найденного значения x вычислите частное
 от деления значения арифметического выражения на 11 и укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно. '''
for x in range(15):
    a = 8 * 15**4 + 2 * 15**3 + x * 15**2 + 1 * 15**1 + 9 - (6 * 15**4 + x * 15**3 + 0 + 7 * 15**1 + 3)
    if a % 11 == 0:
        print(a // 11)