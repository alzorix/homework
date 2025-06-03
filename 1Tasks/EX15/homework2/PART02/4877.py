'''(№ 4877) На числовой прямой даны два отрезка: P = [44; 49] и Q = [28; 53]. Укажите наибольшую возможную длину такого отрезка A, что формула

((x ∈ A) → (x ∈ P)) ∨ (x ∈ Q)

тождественно истинна, то есть принимает значение 1 при любых x. '''

def P():
    return 44<=x<=49
def Q():
    return 28<=x<=53
def A():
    return a1 <= x <= a2
a = list()

for a1 in range(1,100):
    for a2 in range(a1+1,100):
            FLAG = 0
            x = -100
            while x<100:
                x = x + 0.5
                if ((A()) <= ((P())) or (Q())):
                    None
                else:
                    FLAG +=1
                    break
            if FLAG ==0:
                a.append(a2-a1)
print(max(a))