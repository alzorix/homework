'''
№ 5677 Вариант 09.01.23 (Уровень: Средний)
(А. Игнатюк) В текстовом файле дана последовательность латинских букв.
 Необходимо найти в этой последовательности самую длинную подстроку,
 состоящую из комбинации DAD, при этом первый и последний элементы могут быть неполными.
 Например ADDADDADDADD.
В ответе укажите количество символов, составляющих наибольшую длину подходящей подстроки.'''
from copy import deepcopy

with open("24_5677.txt") as file:
    line = file.readline().strip()

blackline = "QWERTYUIOPSFGHJKLZXCVBNM"
new_line = "".join([p if p not in blackline else "!" for p in line])
#Почему нужно менять порядок в [] ?
new_line = new_line.replace("DAD","#")
data = new_line.split("!")
ans = list()
for x in data:
    if x !="":
        if "#" in x:
            #print(x) #D################################DA нашёл руками :D Ответ 99

            #Проверка на DD#D#D

            test = deepcopy(x)
            F =True
            while test.count("#") > 1:
                last = test
                test = test.replace("##","#")
                if test.count("#") !=1 and test == last:
                    F = False
                    break
            # if not(F):
            #     print(x) # вывод #D#D - т.е. работает
            if F:
                count = x.count("#") *3
                # if count ==96: ПРошла сюда
                #     print(1)
                temp = test.split("#")
                if count == 96:
                    print(temp)
                l_count = 0
                if len(temp) > 0:
                    if temp[0] == "D":
                        l_count+=1
                    if temp[0] == "AD":
                        l_count+=1
                    if temp[1] == "D":
                        l_count+=1
                    if temp[1] == "DA": #НАИглупейщая ошибка,здесь была единица заместо двойки
                        l_count+=2
                else:
                    print(test)

                ans.append(count + l_count)
print(max(ans))

#99 +
