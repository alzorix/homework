'''В числах F29x8EAD6_37 и BAxDE0C1B_37 переменная x обозначает некоторую
цифру из алфавита системы счисления с основанием 37. Определите
наибольшее значение x, при котором произведение приведённых чисел
кратно 36. В ответе запишите значение числа 1x2_37 в десятичной системе
счисления'''


#проверено

for x in range(36,-1,-1):
    l=(ord("F")-55) * 37 ** 7     + 2*37 **   6  +9*37 **    5 +     x * 37 **  4    + 8 * 37 ** 4    + (ord("E")-55) * 37 **  3     + (ord("A")-55) * 37 **    2   + (ord("D")-55) * 37 **     1  + 6 * 37 ** 0
    l2 =(ord("B")-55) * 37 **  8   +    (ord("A")-55) * 37 ** 7    +    x *37**6  + (ord("D")-55) * 37 **  5   +    (ord("E")-55) * 37 **  4   +    0 * 37 ** 3+   (ord("C")-55) * 37 **    2 +    1 *37 **1 +   (ord("B")-55) * 37 **  0
    line = l * l2
    if line % 36 == 0:
        print(x)
        print(1 * 37** 2+ x * 37** 1  + 2 *37 ** 0)
        exit()
#2703