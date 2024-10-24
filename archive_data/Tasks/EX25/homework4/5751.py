''' 	(№ 5751) (М. Ишимов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300405. Среди натуральных чисел, превышающих 109, найдите 5 наименьших чисел,
 соответствующие маске 1*2*7*04 и имеющих ровно 45 делителей. В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,

  а во втором столбце – соответствующие им максимальные делители, не считая самого числа. '''


F = list()
from fnmatch import fnmatch
from math import sqrt
from itertools import product
F.append("")
for i in product("1234567890",repeat = 1):
    F.append("".join(i))
for i in product("1234567890",repeat = 2):
    F.append("".join(i))
for i in product("1234567890",repeat = 3):
    F.append("".join(i))
for i in product("1234567890",repeat = 4):
    F.append("".join(i))





print(len(F) * len(F)* len(F))
print("Чисел очень много,проще перебрать! Даже с if-ами долго")

def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))

    for i in range(1,KOREN +1):
        if num % i == 0 :
            D.append(i)
            if num // i != i:
                D.append(num // i)
    D.sort()
    return D



POSLUS = 0
FLAG = False
for i in range(10**9+1,10**10):
            Temp = str(i)
            if FLAG:
                break
            if fnmatch( Temp,"1*2*7*04"):

                Tempint = i
                if sqrt(Tempint) == int(sqrt(Tempint)):

                    tem2 = simplegit(Tempint)
                    if len(tem2) == 45:
                        print(Tempint,tem2[-2])
                        POSLUS +=1


                    if POSLUS == 5:
                        FLAG = True
                        break

# POSLUS = 0
# FLAG = False
#
# S = dict()
# S1key = list()
# for star in F:
#     if FLAG:
#         break
#     for star2 in F:
#         if FLAG:
#             break
#
#         for star3 in F:
#             if len(star) >=2 and len(star2) >=2 and len(star3) >=2:
#                 break
#             if POSLUS == 5:
#                 FLAG = True
#                 break
#             Temp = "1"+ star +"2"+ star2 +"7"+ star3 +"04"
#             Tempint = int(Temp)
#             mainysl = 10**9
#             if len(Temp) < 9:
#
#
#                 tem2 = simplegit(Tempint)
#                 if len(tem2) == 45:
#                     S1key.append(Tempint)
#                     S[Tempint] = tem2[-2]
#                     POSLUS +=1

