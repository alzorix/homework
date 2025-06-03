'''(№ 2597) (К. Амеличев) Среди целых чисел, принадлежащих числовому отрезку [3159; 31584], найдите числа, которые являются простыми. Ответом будет сумма цифр найденных чисел. '''
from math import sqrt
def simplegit(num):

    K = int(sqrt(num))
    for i in range(2,K +1):
        if num % i == 0:
           return False
    return True

F = 0
for i in range(3159, 31584):

    if simplegit(i):
        S = 0
        for x in str(i):
            S = S + int(x)
        F+=S
        print(F,S)
print(F)
