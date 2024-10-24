'''(№ 4551) На числовой прямой даны три интервала: P=[10,15], Q=[5,20] и R=(15,25]. Определите наименьшую возможную длину отрезка A,
 при выборе которого выражения

(x ∉ A) → (x ∈ P) и (x ∈ Q) → (x ∈ R)
принимают различные значения при любых x. '''
def P(x):
    return 10<=x<=15
def Q(x):
    return 5<=x<=20
def R(x):
    return 15<x<=25
def A(x):
    return (not(a1<=x<=a2))


a = list()
for a1 in range(1,100):
    for a2 in range(a1+1,100):
        FLAG = 0
        x = -100
        while x<100:
            x = x + 0.5
            if ((A(x)) <= (P(x))) !=     ((Q(x)) <= (R(x))):
                None
            else:
                FLAG +=1
                break
        if FLAG ==0:
            a.append(a2-a1)

print(min(a))
