'''(№ 5004) Вася составляет слова из букв слова АВТОМАТ. Код должен состоять из 7 букв, и каждая буква в нём должна встречаться столько же раз,
 сколько в заданном слове. Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы. Сколько различных слов может составить Вася? '''

from itertools import permutations as perm
a = set()
for i in perm('АВТОМАТ'):
    wr = "".join(i)

    if "АА"not in wr and "ОА"not in wr and "АО" not in wr and "ВТ"not in wr and "ТВ"not in wr and "ТТ" not in wr and"ВМ"not in wr and "ТМ"not in wr and "МТ" not in wr and "МВ"not in wr :
        a.add(wr)
print(len(a))