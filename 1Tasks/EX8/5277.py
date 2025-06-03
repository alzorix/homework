'''(№ 5277) (Р. Тукеев) Марат составляет шестибуквенные слова из букв слова А, И, К, Л, М, Ь и записывает их в алфавитном порядке в список. Вот начало списка:

1. АААААА
2. АААААИ
3. АААААК
4. АААААЛ
5. АААААМ
6. АААААЬ
7. ААААИА
...
Найдите номер первого слова в списке, начинающегося на К и заканчивающегося на Ь, в котором каждая буква встречается всего лишь раз,
 а разница между номерами этого слова и его перевёртыша составляет 26655. В ответе укажите сумму цифр этого номера. (Пример перевёртыша: питон – нотип)
'''

#ПРОГРАММА НЕ ОПТИМИЗИРОВАННA,ГОРЕ-ПРОГРАММИСТА К СТЕНКЕ!!!

from  itertools import permutations,product
allwords = dict() #Тут будут все возможные слова подходящие под условие
numberdicts = 0


def summer(num):
    num = str(num)
    a = 0
    for i in num:
        a = a + int(i)

    return a




# Этот фор запихивает всё в allwords:
for i in product("АИКЛМЬ",repeat = 6):
    numberdicts += 1
    i = "".join(i)

    if i[0] == "К" and i[5] == "Ь":

        a = set(i)

        if len(a) == len(i):

            #numberdicts += 1
            allwords[i] = numberdicts

    if i[0] == "Ь" and i[5] == "К":
        a = set(i)

        if len(a) == len(i):
            revers_i = i[::-1]


            if abs(numberdicts - allwords.get(revers_i)) == 26655:
                    print(summer(allwords.get(revers_i)))
                    break



# #Этот фор ищет нужный номер
# number2= 0
# for i in product("АИКЛМЬ",repeat = 6):
#
#
#     i = "".join(i)
#     if i[0] == "К" and i[5] == "Ь":
#         #Повторение говнокода
#         a = set(i)
#
#         if len(a) == len(i):
#
#
#
#             revers_i = i[::-1]
#             number2 += 1
#
#             try: # СРАЗУ ВИДНО,ПРОГРАММИСТУ ЛЕНЬ НОРМАЛЬНО ПИСАТЬ НОРМАЛЬНЫЙ КОД,КТО ЕГО НАНЯЛ? HR-а тоже к стенке!
#
#                 if abs(allwords.get(i) - allwords.get(revers_i)) == 26655:
#                     print(number2)
#                     break
#             except:
#                 None




