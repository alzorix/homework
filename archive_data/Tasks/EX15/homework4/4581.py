''''(№ 4581) На числовой прямой даны два отрезка: P = [25, 38] и Q = [9, 44]. Найдите наименьшую возможную длину отрезка A, при котором формула

(x ∈ P) ∧ ¬(¬(x ∈ Q) ∨ (x ∈A))
тождественно ложна, то есть принимает значение 0 при любых x. '''
def P(x):
    return 25 <= x <= 38
def Q(x):
    return 9 <= x <= 44
a = list()
for a1 in range(1,100):
    for a2 in range(a1+1, 100):
        Flag = True

        for x in range(1,99):

            if (P(x)) and (not((not(Q(x))) or (a1<=x <=a2))):
                Flag = False
        if Flag:
            a.append(a2-a1)

print(min(a))

a = list()
for a1 in range(1,100):
    for a2 in range(a1+1,100):
        FLAG = 0
        x = -100
        while x<100:
            x = x + 0.5
            if (P(x)) and (not((not(Q(x))) or (a1<=x <=a2))):
                FLAG += 1
                break

        if FLAG ==0:
            a.append(a2-a1)


print(min(a))
#Я изначально ошибся с способом решения,но правильный в итоге оказался не рабочим/