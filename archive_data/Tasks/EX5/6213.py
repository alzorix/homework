'''(№ 6213) (А. Богданов) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом:
1. Строится двоичная запись числа N.
2. К этой записи дописываются еще несколько разрядов по следующему правилу:
а) если N четное, то к нему справа приписываются два нуля, а слева единица;
б) если N нечетное, то к нему справа приписывается в двоичном виде сумма цифр его двоичной записи;
3. Полученная таким образом запись (в ней как минимум на один разряд больше, чем в записи исходного числа N) является двоичной записью искомого числа R.
Полученная таким образом запись является двоичной записью искомого числа R. Например, исходное число 410=1002
преобразуется число 110002 = 4810, а исходное число 1310 = 11012 преобразуется в число 1101112 = 5510.
Укажите такое число N большее 8, для которого число R является наименьшим среди чисел, превышающих 88.
В ответе это число запишите в десятичной системе счисления. '''

a = set() # Все R
b = dict() # N из R

for N in range(9,999):
    binN = bin(N)[2::]
    if N % 2 ==0:
        R = "1" + binN + "00"
    else:
        R = binN + bin(bin(N)[2::].count("1"))[2::]


    if int(R,base =2) > 88:
        a.add(int(R,base =2))
        #print(R,N)
        b[int(R,base =2)] = N

print(b.get(min(a)))



