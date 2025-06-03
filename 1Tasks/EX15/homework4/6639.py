'''(№ 6639) (Е. Джобс) На числовой прямой даны два отрезка: P = [5; 54], Q = [50; 93]. Найдите минимальное целое значение А, при котором выражение

(x ∉ P) ∧ (x ∈ Q) → (x > A)
ложно (принимает значение 0) ровно для 20 целых значений x'''


def P(x):
    return (not(5 <= x <= 54))
def Q(x):
    return 50 <= x <= 93

for A in range(1,999):
    indicator=0
    for x in range(1, 999):
        if (( P(x)) and ( Q(x))) <= (x > A):

            None
        else:
            indicator += 1
    if indicator == 20:
        print(A)
        break