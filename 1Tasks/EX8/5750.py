'''(№ 5750) (М. Байрамгулов) Ваня составляет 6-буквенные слова из букв слова КОМПЬЮТЕР так, что в них можно убрать три
 буквы и получить слово КОТ. Сколько различных слов может составить Ваня? '''
from itertools import  product,permutations

a = 0

for i in product("КОМПЬЮТЕР",repeat = 6):

    i = "".join(i)
    if  "К" in i  and "О" in i and "Т" in i :

        if  i[i.find("К"):i.rfind("Т")].count("О") != 0:

            # print(i)
            # print(i.find("К") , i.find("О") ,i.find("Т"))

            a += 1

print(a)
#print("11249")



