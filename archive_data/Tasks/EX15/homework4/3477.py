'''(№ 3477) (С.А. Скопинцева) Элементами множества А являются натуральные числа. Известно, что выражение

¬((x ∈ {2, 4, 9, 10, 15}) ≡ (x ∈ A)) → ((x ∈ {3, 8, 9, 10, 20}) ≡ (x ∈ A))
истинно (т.е. принимает значение 1 при любом значении переменной х. Определите наименьшее возможное значение произведения элементов множества A. '''


#ОБРАЗЕЦ: A = set()
# P = { 1, 2, 3, 4 }
# Q = { 1, 2, 3, 4, 5, 6 }
#
# for x in range(1,100):
#     if (not(x in A)) <= ((not(x in P)) or (not(x in Q))):
#         None
#     else:
#         A.add(x)
# print(len(A))
# print(A)
#

A= set()

for x in range(1,10000):
    if (not((x in {2, 4, 9, 10, 15})) == (x in A)) <= ((x in {3, 8, 9, 10, 20}) == (x in A)):
        None
    else:
        A.add(x)
x = 1
for i in A:
    x =  x*i
print(x)