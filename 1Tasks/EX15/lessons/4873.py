'''(№ 4873) На числовой прямой даны два отрезка: P=[5;30] и Q=[14;23]. Укажите наибольшую возможную длину такого отрезка A, что формула

((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)

тождественно истинна, то есть принимает значение 1 при любых x.'''
def one(x):
    return 5<=x<=30
def two(x):
    return  14<=x<=23
a = list()
for a1 in range(1,100):
    for a2 in range(a1+1,100):
        FLAG = 0
        x = -100
        while x<100:
            x = x + 0.2
            if (one(x) == two(x)) <= (not( a1<=x<=a2 )):
                None
            else:
                FLAG +=1
                break
        if FLAG ==0:
            a.append(a2-a1)

print(max(a))
#print(a)



