'''(№ 4555) На числовой прямой даны два отрезка: P = [10, 20] и Q = [25, 36]. Найдите наибольшую возможную длину отрезка A, при котором формула

( (x ∈ А) ∧ (x ∉ P) ) → (x ∈ Q)
тождественно истинна, то есть принимает значение 1 при любых x. '''

def P(x):
    return (not(10<=x<=20))
def Q(x):
    return 25<=x<=36
def A(x):
    return a1<=x<=a2

a = list()
for a1 in range(1,100):
    for a2 in range(a1+1,100):
        FLAG = 0
        x = -100
        while x<100:
            x = x + 0.5
            if ( (A(x)) and (P(x)) ) <= (Q(x)):
                None
            else:
                FLAG +=1
                break
        if FLAG ==0:
            a.append(a2-a1)

print(max(a))
