'''(№ 6917) (Е. Джобс) Маша выписывает в алфавитном порядке буквенные слова длиной 4
символа, составленные из букв М, А, Р, И, Я. Начало списка выглядит так::
1. АААА
2. АААИ
3. АААМ
4. АААР
5. АААЯ
...
Под каким номером в списке стоит слово АРИЯ?'''
#Тут всё по памяти.
from itertools import product as prod
n = 0
for i in prod("АИМРЯ",repeat = 4):
    i = "".join(i)
    n +=1
    if i == "АРИЯ":
        print(n)


