'''(№ 4875) На числовой прямой даны два отрезка: P = [12; 26] и Q = [30; 53]. Укажите наибольшую возможную длину такого отрезка A, что формула

((x ∈ A) → (x ∈ P)) ∨ (x ∈ Q)

тождественно истинна, то есть принимает значение 1 при любых x. '''

def one(x):
    return 12<=x<=26
def two(x):
    return  30<=x<=53
a = list()
for a1 in range(1,100):
    for a2 in range(a1+1,100):
        FLAG = 0
        x = -100
        while x<100:
            x = x + 0.5
            if (  (a1<=x<=a2) <= one(x)  ) or two(x):
                None
            else:
                FLAG +=1
                break
        if FLAG ==0:
            a.append(a2-a1)

print(max(a))
print(a)


