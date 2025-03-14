'''(№ 4871) Элементами множеств А, P и Q являются натуральные числа, причём P = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20} и
Q = { 3, 6, 9, 12, 15, 18, 21, 24, 27, 30 }. Известно, что выражение

((x ∈ A) → ¬(x ∈ P)) ∧ (¬(x ∈ Q) → ¬(x ∈ A))
истинно (т. е. принимает значение 1) при любом значении переменной х. Определите наибольшее возможное количество элементов множества A. '''




# ОБРАЗЕЦ:
# P = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# Q = { 5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
#
#
# A = set(range(1,1000))
# for x in range(1,1000): #ДОЛЖО СОВПАДАТЬ С А
#     if ((x in A) <= (x in P)) and ((x in Q) <= (not(x in A))):
#         None
#     else:
#         A.remove(x)
# print(len(A))

P = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = { 3, 6, 9, 12, 15, 18, 21, 24, 27, 30 }

A = set(range(1,10000))
for x in range(1,10000): #Должно совпадать с А
    if ((x in A) <= (not(x in P))) and ((not(x in Q)) <= (not(x in A))):
        None
    else:
        A.remove(x)
print(len(A))