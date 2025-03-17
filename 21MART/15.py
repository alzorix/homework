def DEL(n,m):
    return n%m == 0

last = 0
for A in range(1,10000):

    F = True
    x = 0.5

    while x<=300:

        if DEL(x,A) or ( (60<= x <= 80) <=  (not(   DEL(x,22)      ))          ):
            None
        else:

            F = False

        x+=0.5

    if F:
        last = A

print(last)
#Ответ 60 - неверный
