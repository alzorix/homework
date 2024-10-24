'''(№ 5839) (C. Якунин) Дмитрий составляет слова, переставляя буквы в слове АМФИБРАХИЙ. Сколько слов, в которых есть, хотя бы, 2 подряд идущие гласные может составить Дмитрий? '''
from itertools import product,permutations
a = set()



for i in permutations('АМФИБРАХИЙ'):
    wr = "".join(i)




    if "АИ" in wr or "ИА" in wr or "ИИ" in wr or "АА" in wr:

             a.add(wr)

print(len(a))

print(756000)
