'''(№ 7189) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300425.
Среди натуральных чисел, меньших 109, найдите числа, удовлетворяющих маске 9*31?5*7 и делящиеся на 2801, у которых сумма цифр – простое число.
 Запишите в ответе найденные числа в порядке возрастания, справа от каждого числа запишите частное от его деления на 2801. '''

from itertools import product
from math import sqrt
L = list()
L.append("")
for i in product("0123456789",repeat = 1):
    L.append("".join(i))
for i in product("0123456789",repeat = 2):
    L.append("".join(i))
for i in product("0123456789",repeat = 3):
    L.append("".join(i))


D = list()
temp = 931057
def simplegit(num):

    KOREN = int(sqrt(num))
    for i in range(2,KOREN +1):
        if num % i == 0:
           return False
    return True



def suum(x):
    F = 0
    for i in str(x):
        F = F + int(i)
    return F







E = dict()
Ekey = list()


#
# for quest in range(0,10):
#     #print(1)
#         a1 = ""
#
#         for a2 in L:
#             T ="9" +   a1  + "31"+   str(quest)  +"5" +  a2   + "7"
#             if len(T)<=9:
#              Tint= int(T)
#
#              if Tint%2801==0:
#
#                 if simplegit(suum(Tint)):
#                     Ekey.append(Tint)
#                     E[Tint] = Tint//2801
#
#
#
# for quest in range(0,10):
#     #print(1)
#         a2 = ""
#
#         for a1 in L:
#             T ="9" +   a1  + "31"+   str(quest)  +"5" +  a2   + "7"
#             if len(T)<=9:
#              Tint= int(T)
#
#              if Tint%2801==0:
#
#                 if simplegit(suum(Tint)):
#                     Ekey.append(Tint)
#                     E[Tint] = Tint//2801



# L.clear()
# for i in product("0123456789",repeat = 1):
#     L.append("".join(i))
# for i in product("0123456789",repeat = 2):
#     L.append("".join(i))
# for i in product("0123456789",repeat = 3):
#     L.append("".join(i))

for quest in range(0,10):
    #print(1)
    for a1 in L:
        for a2 in L:
            T ="9" +   a1  + "31"+   str(quest)  +"5" +  a2   + "7"
            if len(T)<=9:
             Tint= int(T)

             if Tint%2801==0:

                if simplegit(suum(Tint)):
                    Ekey.append(Tint)
                    E[Tint] = Tint//2801




Ekey.sort()

for i in Ekey:

    print(i,E.get(i))