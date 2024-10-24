'''(№ 5965) (Д. Муфаззалов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300405.

Найдите все натуральные числа, не превосходящие число 10∙2023 3, соответствующие маске *2??3*,
 записи которых в системах счисления с основаниями 3, 9 и 27 являются палиндромами.
   В ответе запишите все найденные числа в порядке возрастания, а справа от каждого числа — сумму цифр в его записи в системе счисления с основанием 8. '''



print("алфавит для калькулятора:")
ALFAVIT = dict()
FRUHURW = 10
for i in range(65,82):
    print(FRUHURW," ",chr(i))
    ALFAVIT[FRUHURW] = chr(i)
    FRUHURW +=1




def absolutesolver(num,R):
    F = list()
    num=num
    while num !=0:
        F.append((str(num%R)))
        num = num//R
    F.reverse()
    return "".join(F)

def convert27(num):
    F = list()
    num=num
    while num !=0:
        d = num%27
        if d <10:

                F.append((str(d)))
        else:
            F.append(ALFAVIT[d])
        num = num//27
    F.reverse()
    return "".join(F)






from itertools import product
a2 = list()
a2.append("")

for i in product("0246813579",repeat =1):
    a2.append("".join(i))

for i in product("0246813579",repeat =2):
    a2.append("".join(i))

for i in product("0246813579",repeat =3):
    a2.append("".join(i))

for i in product("0246813579",repeat =4):
    a2.append("".join(i))

for i in product("0246813579",repeat =5):
    a2.append("".join(i))

for i in product("0246813579",repeat =6):
    a2.append("".join(i))

for i in product("0246813579",repeat =7):
    a2.append("".join(i))


a1 = [0,1,2,3,4,5,6,7,8,9]
q = 10*2023**3

# for quest in a1:
#     for star in a2:
#         T = int(f"{star}2{quest}{quest}3{star}")
#         if T < q:
#             T3 = absolutesolver(T,3)
#             T9 = absolutesolver(T, 9)
#             T27 = 0
#             if T3 == T3[::-1]:
#                 if T9 == T9[::-1]:
#                     None
#
#
print(convert27(10*2023**3))