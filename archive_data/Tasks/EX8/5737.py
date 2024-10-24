'''(№ 5373) (П. Финкель) Маша составляет шестибуквенные слова из букв Т, И, М, А, Ш, Е, В, С, К. Она выбирает только те слова,
в которых количество гласных и согласных одинаково, и гласная буква не стоит рядом с Ш. Сколько таких слов может составить Маша? '''

from itertools import product,permutations
a = set()
s = set()

for i in product('ИАЕШ',repeat = 2):
    wr = "".join(i)
    if "Ш" in wr:
        if "ШШ" not in wr:
            s.add(wr)
print(s)



for i in product('ТИМАШЕВСК',repeat = 6):
    wr = "".join(i)

    if wr.count("Т") + wr.count("М") + wr.count("Ш") + wr.count("С") + wr.count("В") + wr.count("К") == wr.count("И") + wr.count("А") + wr.count("Е"):
       if "ШЕ" not in wr and "ЕШ" not in wr and "АШ" not in wr and "ШИ" not in wr and "ША" not in wr and "ИШ" not in wr:
               a.add(wr)

print(len(a))

print(75870)