'''(№ 6749) (ЕГЭ-2023) Для какого наибольшего целого неотрицательного A выражение
(x + 2 · y > A) ∨ (y < x) ∨ (x < 30)
тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных значениях переменных x и y? '''
all = list()
for A in range(0,9999):
    susmax = 0
    for x in range(999):
        for y in range(999):
            if not(((x + 2*y)> A ) or (y<x) or (x<30)):
                susmax +=1
                break
        if susmax >0:
            break

    if susmax==0:
        all.append(A)
print(max(all))


