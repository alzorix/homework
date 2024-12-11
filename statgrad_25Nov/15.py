'''На числовой прямой даны три отрезка: P = [3; 43], Q = [18; 91], R = [72; 115].
Укажите наименьшую возможную длину такого отрезка A, для которого
логическое выражение
(x ∈ Q) → (¬(x ∈ P) → ((¬(x ∈ R) ∧ ¬(x ∈ A)) → ¬(x ∈ Q)))
истинно (т.е. принимает значение 1) при любом значении переменной x'''


#x ∈ Q) → (¬(x ∈ P) → ((¬(x ∈ R) ∧ ¬(x ∈ A)) → ¬(x ∈ Q)))

def Q(x):
    return 18<=x<=91
def P(x):
    return 3<=x<=43
def R(x):
    return 72<=x<=115
anns = list()
for a1 in range(0,150):
    for a2 in range(a1+1, a1+150):
        FLAG = True
        x =0
        while x <=300.0:
            #if (Q(x)) <= (not((P(x))) <=((not((R(x))) and (not((a1<= x <=a2)))) <= (not(Q(x))))):
            if (Q(x)) <= ((not(P(x))) <= (((not(R(x))) and (not(a1<=x<=a2)))   <= (not(Q(x)))        )):
                None
            else:
                FLAG = False
                break
            x+= 0.5
        if FLAG:
            anns.append(a2-a1)
anns.sort()


#Для красоты:
#print(anns)
print(min(anns))