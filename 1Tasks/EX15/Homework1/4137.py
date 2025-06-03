'''(№ 4137) (А. Богданов) На числовой прямой дан отрезок Q = [29; 47]. Обозначим через ДЕЛ(n, m) утверждение «натуральное число
n делится без остатка на натуральное число m». Определите наименьшее натуральное число A, такое что выражение

(¬ДЕЛ(x, 3) ∧ x ∉ {48, 52, 56}) → ((|x – 50| ≤ 7) → (x ∈ Q)) ∨ (x & A = 0)
тождественно истинна, то есть принимает значение 1 при любом значении переменной х. '''
Q = set()



def DEL(n,m):
    return n%m==0
def simbol(x):
    return x !=48 and x !=52 and x !=56
def simbol2(x):
    Q.clear()
    for i in range(29, 48):
        Q.add(i)
    c = len(Q)

    Q.add(x)
    return len(Q) == c

for A in range(1,999):
    num = 0
    for x in range(1,99):
        if (not(DEL(x, 3)) and (simbol(x))) <= ((    (abs(x - 50))    <= 7) <= (simbol2(x))) or (x & A == 0):
            None
        else:
            num +=1
    if num ==0:
        print(A)
        break







