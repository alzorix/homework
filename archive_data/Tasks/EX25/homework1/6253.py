'''(№ 6253) (PRO100 ЕГЭ) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Среди натуральных чисел, не превышающих 1010, найдите все числа, соответствующие маске 9?979*8, делящиеся на 50068 без
 остатка и содержащие хотя бы одну цифру 0. В ответе запишите все найденные числа в порядке возрастания, справа от каждого числа – результат его деления на 50068. '''

from fnmatch import *

for i in range(50068,10**10,50068):
    if "0" in str(i):
        if fnmatch(str(i),"9?979*8"):
            print(i,i//50068)





