''' 	(№ 7191) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300425.
Среди натуральных чисел, меньших 10^9, найдите числа, удовлетворяющих маске 7*15?3*7 и делящиеся на 2267,
 у которых сумма цифр – простое число. Запишите в ответе найденные числа в порядке возрастания, справа от каждого числа запишите частное от его деления на 2267. '''
a = list()
a.append("")
L = list()
from itertools import product

for i in product("0123456789",repeat =  1):
    a.append("".join(i))
for i in product("0123456789",repeat =2):
    a.append("".join(i))
for i in product("0123456789",repeat =3):
    a.append("".join(i))




def simpledigitls(ss):
    summ = 0
    for i in ss:
        summ = summ + int(i)
    polovina = summ//2
    for i in range(2,polovina+1):
        if summ % i ==0:
            return 0
    return 1




for quest in range(0,9):
    quest = str(quest)
    for symv in a:
        for symv2 in a:


            s = int("7" + symv + "15" + quest + "3" + symv2 + "7")
            if s < 10 ** 9:

                if s % 2267 == 0:
                    if simpledigitls(str(s)):

                        L.append(s)

L.sort()

for i in L:
    print(i,i//2267)
