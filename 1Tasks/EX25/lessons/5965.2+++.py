'''Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300405. Найдите все натуральные числа, не превосходящие
число 10∙2023^3, соответствующие маске *2??3*, записи которых в системах счисления с основаниями 3, 9 и 27 являются палиндромами.
В ответе запишите все найденные числа в порядке возрастания, а справа от каждого числа — сумму цифр в его записи в системе счисления с основанием 8.'''
from itertools import *
from fnmatch import *

def convert3(n):
    q = []
    while n != 0:
        q.append(str(n % 3))
        n = n // 3
    z = "".join(q)
    return z[::-1]


def convert9(n):
    q = []
    while n != 0:
        q.append(str(n % 9))
        n = n // 9
    z = "".join(q)
    return z[::-1]




#Функция формирования словаря с буквами соответствующих остатков в системе счисления с основанием base
def get_mod_dict(base):
    index_A = ord("A")
    w = {}
    for i in range(10, base):
        w[i] = chr(index_A + (i - 10))
    return w


def convert27(n, w):#n - само число w - словарь
    q = []
    while n != 0:
        if n % 27 < 10:
            q.append(str(n % 27))
        else:
            q.append(w[n % 27])
        n = n // 27
    z = "".join(q)
    return z[::-1]


def product_list(chars, repeat_num): #fast product
    q = []
    for i in product(chars, repeat=repeat_num):
        w = "".join(i)
        q.append(w)
    return q


w = get_mod_dict(27)
a = 10*2023**3
print(convert27(a, w))
chars_27 = '0123456789' + ''.join(list(w.values()))
print(chars_27)

l_3 = product_list(chars_27, 3)
l_2 = product_list(chars_27, 2)
l_1 = list(chars_27)

def ss():
    b = int(s, base=27)
    if b < a and fnmatch(str(b), '*2??3*'):
        b_9 = convert9(b)
        if b_9 == b_9[::-1]:
            b_3 = convert3(b)
            if b_3 == b_3[::-1]:
                d.append(b)
d = []
for i in '1234567':
    for j in l_3:
        s = i + j + j[::-1] + i
        ss()
for i in l_1:
    for j in l_3:
        s = j + i + j[::-1]
        ss()
for j in l_3:
        s = j + j[::-1]
        ss()
for i in l_1:
    for j in l_2:
        s = j + i + j[::-1]
        ss()
for j in l_2:
        s = j + j[::-1]
        ss()
for i in l_1:
    for j in l_1:
        s = j + i + j
        ss()
for j in l_1:
        s = j + j
        ss()


d.sort()

def summ(n): #а справа от каждого числа — сумму цифр в его записи в системе счисления с основанием 8.
    a = oct(n)[2:]
    s = 0
    for i in range(0, len(a)):
        s = s + int(a[i])
    return s

for i in d:
    print(i, summ(i))
