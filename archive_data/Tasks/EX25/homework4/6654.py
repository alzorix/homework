''' 	(№ 6654) (Е. Джобс) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300425.
Найдите все числа, меньшие 106, которые имеют ровно 24 делителя, соответствующих маске 4*, и максимальный делитель таких чисел, соответствующий маске.
В ответе укажите найденные числа в порядке возрастания, справа от каждого числа выведите его максимальный делитель, соответствующий маске 4*. '''

from itertools import product
from math import sqrt
from fnmatch import fnmatch
from fnmatch import fnmatch






def sg(x):
    delList= list()
    sx = int(sqrt(x))
    for i in range(1,sx+1):
        if x % i == 0:
                if fnmatch(str(i), "4*"):
                    delList.append( i)
                if i != x // i:
                    if fnmatch(str(x // i), "4*"):
                        delList.append(x // i)
    return delList







for i in range(1,10**6):


    func= sg(i)
    if len(func) == 24:
        #if "4" in str(max(func)):
        print(i,max(func))






