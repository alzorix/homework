'''(№ 4192) (П. Волгин) Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:

F(0) = 1
F(n) = F(n–1) + F(n–2), при чётном n > 0
F(n) = 1,5*F(n–1), при нечётном n > 0

Сколько различных цифр встречается в целой части значения функции F(15)?
'''

def F(n):
    if n==0:
        print(1)
        return 1
    elif n>0 and n% 2 ==0:
        print(n)
        return F(n-1) + F(n-2)
    elif n>0 and n% 2 !=0:
        print(n)
        return 1.5*F(n-1)
    else:
        print("#")
        exit()

line = F(15)
check,trash= str(line).split(".")
print(check)
#3