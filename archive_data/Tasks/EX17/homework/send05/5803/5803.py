'''(№ 5803 ) (П. Финкель) В файле 17-346.txt содержится последовательность целых чисел. Элементы последовательности могут
принимать целые значения от 1 до 200 000 включительно. Определите количество троек последовательности, для которых произведение
 всех чётных цифр трёх чисел не превосходит 2·109 и удовлетворяет маске «25*2*». В качестве ответа укажите количество таких троек
  и наибольшее произведение их чётных цифр. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности. '''
import re
yslovie1 = 2*109
def musk(num):
    print(num)

    #Реализация с re,библеотекой пользуюсь второй раз в жизни,косяк и тут может быть

    if re.match(r'25\d2\d',str(num)):
        print(1)
        return True
    else:
        return False

    # Flag = False
    # for x in range(0,10):
    #     ysl = "25" + str(x) + "2"+str(x)
    #     if ysl in str(num):
    #         print(1)
    #         Flag = True
    # return Flag


def work(num1,num2,num3):

    num1 = str(num1)
    num2 = str(num2)
    num3 = str(num3)
    num = num1 + num2 + num3
    nechet = 0
    chet = 1
    spis = []
    for i in str(num):
        spis.append(int(i))

    for i in range(len(spis)):
        if spis[i] % 2==0 and spis[i]!=0:
            chet = chet * spis[i]


    if musk(chet) and chet < yslovie1:
        print(1)


        return chet
    else:
            return 0

spisok = list()
with open("File") as file:
    line = file.readline().strip()
    while line!= "":
        line = int(line)



        spisok.append(int(line))
        line = file.readline().strip()





kolvo = list()




for m in range( len(spisok) -2):


    if work( spisok[m] , spisok[m+1] , spisok[m+2]) !=0: #Возможно ошибка здесь
        kolvo.append(work( spisok[m] , spisok[m+1] , spisok[m+2]))



print(len(kolvo))
