'''(№ 149) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое
число R следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы на 2
дописывается в конец числа (справа). Например, запись 11100 преобразуется в запись
111001;
б) над этой записью производятся те же действия – справа дописывается остаток от
деления суммы цифр на 2.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного
числа N) является двоичной записью искомого числа R. Укажите такое наименьшее число
R, которое превышает 118 и может являться результатом работы алгоритма. В ответе это
число запишите в десятичной системе счисления'''
f =  list()
def ss(num):
    num = str(num)
    F = 0
    for i in num:
        F = F + int(i)
    return F
for N in range(1,9000):
    binN = bin(N)[2::]
    #print(binN)
    binN = binN +  str(ss(binN) %2)
    binN = binN + str(ss(binN) % 2)
    if int(binN,2) >118:
        f.append(int(binN,2))
print(min(f))
