''' 	(№ 6836) (А. Богданов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300425.
Среди десятиразрядных чисел, кратных 2023 и соответствующих маске «1*1», найдите числа с максимальной суммой цифр.
 В ответ запишите найденные числа в порядке убывания, справа от каждого числа запишите частное от деления на 2023.
 '''
def summ(n:str):
    x = 0
    for i in n:
        x = x + int(i)
    return x

for i in range(10000000000-1,1000000000,-1):
    if i%2023==0:
        # print(i)
        # print((i-2*2023)%2023)
        break
from fnmatch import *

spis = []
var = 0
for i in range(9999998519,1000000000,-2023):
    if fnmatch(str(i),"1*1"):
        #print(i,i//2023)
        summm= summ(str(i))
        if summm > var:
            var = summm
            spis.clear()
            spis.append(i)
        elif summm == var:
            spis.append(i)
for i in spis:
    print(i,i//2023)


# Что за такие максимальные цифры и почему их несколько?

