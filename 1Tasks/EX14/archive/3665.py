"""(№ 3665) Число 804 записали в системах счисления с основаниями от 2 до 10 включительно. При каких основаниях в записи
 этого числа есть цифра 1? В ответе укажите сумму всех подходящих оснований. """

def ABSOLUTESOLVER(N,chislenie):
        F = list()
        while N != 0:
            F.append(str(N % chislenie))
            N = N // chislenie

        F.reverse()
        Z = "".join(F)
        return Z

if __name__ == '__main__':
    sum = 0
    a = 2
    while a < 11:
        temp = ABSOLUTESOLVER(N =804,chislenie= a )

        if temp.count("1") !=0:
            print(a)
            sum = sum + int(a)

        a += 1
print(sum)