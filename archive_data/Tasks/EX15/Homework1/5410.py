'''(№ 5410) (А. Богданов) Для какого наибольшего целого неотрицательного A выражение

(7y + 5x < 1000) ∨ (x < y) ∨ (A < x)
тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y? '''
for A in range(999,-1,-1):
    num = 0
    for x in range(0,999):

        for y in range(0,999):
            if (7*y + 5*x < 1000) or (x < y) or (A < x):
                None
            else:
                num+=1
                break
        if num != 0:
            break

    if num == 0:
        print(A)
        break