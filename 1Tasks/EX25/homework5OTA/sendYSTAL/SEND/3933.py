'''(№ 3933) (Е. Джобс) Напишите программу, которая находит 6 простых чисел наиболее приближенные к числу 10000000 (10 миллионов).
 Причем 3 найденных числа должны быть меньше 10000000, остальные 3 числа – больше. Найденные числа расположите в порядке возрастания.
  В качестве ответа выведите пары чисел – расстояние от найденного числа до 10000000 и само число. '''


import time
start_time = time.time()
from  math import sqrt
def simplegit(num):

    K = int(sqrt(num))
    for i in range(2,K +1):
        if num % i == 0:
           return False
    return True
D = 0
SDO = 0
L = 0
for DO in range( 10000000,10000000 - 1000,-1):
    if L ==3:
        break

    SDO = SDO-1
    if simplegit(DO):
        print(DO,abs(SDO)-1) #Почему-то выводит номер на 1 больше,хотя логика такая-же
        L += 1


L = 0
SPOSL = 0
for POSL in range( 10000001,10000000 + 1000):
    if L ==3:
        break
    SPOSL = SPOSL-1
    if simplegit(POSL):
        print(POSL,abs(SPOSL))
        L += 1


end_time = time.time()
programm_time = end_time - start_time
print(f"Время выполнения программы: {programm_time} секунд")