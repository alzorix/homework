'''(№ 6999) (Е. Джобс) На вход алгоритма подается натуральное число N. Алгоритм строит
по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. В этой записи последний ноль заменяется на первые две цифры полученной записи.
Если нуля нет, алгоритм аварийно завершается.
3. Запись записывается справа налево (в обратную сторону).
Полученная таким образом запись является двоичной записью искомого числа R. Для
какого минимального значения N в результате работы алгоритма получится число 123?'''

for N in range(1,999):
    binN = bin(N)[2::]
    last = binN.rfind("0") #Не был уверен,что использую правильную функцию. Загуглил,что и как делает rfind
    if last == -1:
        None
    else:
        res = binN[:last] + binN[:2] + binN[last+1:]
        res = res[::-1]
        res = int(res,2)
        if res ==123:
            #print(res)
            print(N)
            break

