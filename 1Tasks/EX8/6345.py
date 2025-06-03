'''(№ 6345) *Варфоломей составляет коды из букв, входящих в слово ВАРФОЛОМЕЙ. Код должен состоять из 6 букв,
 буквы в коде не должны повторяться, согласных в коде должно быть больше, чем гласных, две гласные буквы нельзя ставить рядом. Сколько различных кодов может составить Варфоломей? '''

from  itertools import  permutations,product
score = 0

# for i in product("АОЕ",repeat = 2):
#     print("".join(i))


for i in permutations("ВАРФОЛМЕЙ",6 ):
    i = "".join(i)

    i = i.replace("В","1").replace("Р","1").replace("Ф","1").replace("Л","1").replace("М","1").replace("Й","1")
    i = i.replace("А","0").replace("О","0").replace("Е","0")





    if "00" not in i:
        if i.count("1") > i.count("0"):
            #print(i)
            score += 1
print(score)


