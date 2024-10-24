''' 	(№ 6900) (П. Финкель) Оля составляет слова путём перестановки букв слова «ТИМАШЕВСК».
Она выбирает слова, которые начинаются и заканчиваются согласной буквой и три гласные стоят рядом. Сколько таких слов может написать Оля? '''

from itertools import product,permutations
a = set()
s = set()

allchar = set("ТМВШСК")

for i in permutations('ИАЕ'):
    wr = "".join(i)
    s.add(wr)
print(s)



for i in permutations('ТИМАШЕВСК'):
    wr = "".join(i)




    if "АЕИ" in wr or "ИЕА" in wr or "АИЕ" in wr or "ЕИА" in wr or "ЕАИ" in wr or "ИАЕ" in wr:
        if wr[0] in allchar:
            # C этим условием неправильный ответ,почему?
         if wr[-1] in allchar:
               a.add(wr)

print(len(a))


