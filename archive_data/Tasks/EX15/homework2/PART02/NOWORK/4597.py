'''(№ 4597) На числовой прямой даны два отрезка: P = [15, 40] и Q = [35, 60]. Найдите наибольшую возможную длину отрезка A, при котором формула

(¬(x ∈ Q) ∨ (x ∈ P)) ∧ (x ∈ A)
тождественно ложна, то есть принимает значение 0 при любых x. '''
# def P():
#     return 15<=x<=40
# def Q():
#     return 35<=x<=60
# def A():
#     return a1<=x<=a2
#
# from itertools import combinations
#
# def f(x):
#     return (  ( not( Q() )   ) or   (P())       ) and (A())
# a = [x/10 for x in range(10*10,70*10 + 1)]
# print(a)
#
# superl = list()
# for a1,a2 in combinations(a,2):
#     flag = 0
#
#     for x in a:
#         if f(x):
#             flag += 1
#             break
#     if flag >0:
#         None
#     else:
#
#         superl.append(a2-a1)
#         print(a1,a2)
#
# print(max(superl))
