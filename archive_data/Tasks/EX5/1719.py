'''(№ 1719) Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.
1. Из цифр, образующих десятичную запись N, строятся наибольшее и наименьшее возможные двузначные числа (числа не могут начинаться с нуля).
2. На экран выводится разность полученных двузначных чисел.
Пример. Дано число N = 351. Наибольшее двузначное число из заданных цифр – 53, наименьшее – 13. На экран выводится разность 53 – 13 = 40.
Чему равно количество чисел N на отрезке [300; 400], в результате обработки которых на экране автомата появится число 20? '''
s = 0
for N in range(300,401):
    a = list()
    N = str(N)
    for i in range(len(N)):
        a.append(N[i])

    a.sort()
    print(a)

    big=a.pop()
    med=a.pop()
    small=a.pop()

    naib = int(big + med)
    if small != "0":
        naim = int(small + med)
    elif med != "0":
        naim = int(med + small)
    else:
        naim = int(big + small)




    print()
    if naib - naim == 20:
        s= s + 1

print(s)
