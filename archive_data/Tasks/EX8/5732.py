'''(№ 5732) (П. Финкель) Коля составляет 5-буквенные слова из букв Т, И, М, А, Ш, Е, В, С, К и записывает их в обратном алфавитном порядке. Вот начало списка:

1. ШШШШШ
2. ШШШШТ
3. ШШШШС
4. ШШШШМ
К
И
Е
В
А
...

Под каким номером в списке стоит первое слово-палиндром, в котором в середине стоит согласная буква, а все остальные – гласные? '''

#А что делать,если я не знаю алфавит?

from itertools import product

score = 0
for i in product("ШТСМКИЕВА",repeat = 5):
    score+= 1
    i = "".join(i)
    if i == i[::-1]:
        if i[2] == "Ш" or i[2] == "Т" or i[2] == "С" or i[2] == "М" or i[2] == "К" or i[2] == "В":
         if i.count("И") + i.count("Е ") + i.count("А") == 4 :
             print(score)
             break


a = ["Т", "И", "М", "А", "Ш", "Е", "В","С", "К"]
a.sort()
print(a)