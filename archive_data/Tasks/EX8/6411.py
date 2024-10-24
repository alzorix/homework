'''(№ 6411) (М. Шагитов) Марат составляет 8-буквенные коды из букв, входящих в слово ЕСТЕСТВО.
 В коде должно быть не менее трех гласных и не менее четырех согласных букв.
  Каждая гласная буква в коде должна быть разделена от другой гласной буквы хотя бы одной согласной.
   Сколько различных кодов может составить Марат? '''


from itertools import  product,permutations
# for i in product("ЕО",repeat = 2):
#     i = "".join(i)
#     print(i)

score = set()

for i in product("ЕТСВО",repeat = 8):
    i = "".join(i)

    if "ЕЕ" not in i and  "ЕО" not in i and  "ОЕ" not in i and  "ОО" not in i:
        if i.count("Е") + i.count("О") >2:
            if i.count("С") + i.count("Т") + i.count("В") >3:
             score.add(i)
print(len(score))

print("Правильный ответ: 45360")