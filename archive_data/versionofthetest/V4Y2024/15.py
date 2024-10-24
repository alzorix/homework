'''Для какого наименьшего целого неотрицательного числа А выражение
(2x + 3y ≤ 95) ∧ (x ≥ A) ∧ (y ≥ A)
тождественно ложно, т.е. принимает значение 0 при любых целых неотрицательных x и y?'''

for A in range(0,999):
    FLAG = True
    for x in range(0,999):
        for y in range(0, 999):
            if ((2*x + 3*y) <= 95) and (x >= A) and (y >= A):
                FLAG = False
                break
    if FLAG:
        print(A)
        break