'''(№ 6039) (А. Рогов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Среди натуральных чисел, не превышающих 108, найдите все числа,
 соответствующие маске 1?58*129, которые делятся без остатка только на одно из чисел 117, 119, 121.
В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, справа от каждого числа запишите результат
 его деления на то из чисел 117, 119, 121, на которое это число делится без остатка. '''


def ysl(n):
    if int(n % 117 ==0) + int(n % 119 ==0) + int(n % 121 ==0) ==1:
        return True
    else:
        return False


from fnmatch import *

for i in range(1,10**8):
    if fnmatch(str(i),"1?58*129"):

        if ysl(i):
            if i % 117 ==0:
              print(i,i // 117)
            elif i % 119 ==0:
                print(i,i // 119)
            else:
                print(i,i // 121)
