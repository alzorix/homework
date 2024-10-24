'''(№ 5681) (А. Богданов) Оля составляет слова перестановкой букв слова СПОРТЛОТО, оставляя только слова с тремя буквами О рядом. Сколько различных слов может составить Оля?'''

from itertools import permutations
a = set()
for i in permutations("СПОРТЛОТО"):
    wr = "".join(i)
    print(wr)
    if "ООО" in wr:
        a.add(wr)
print(len(a))