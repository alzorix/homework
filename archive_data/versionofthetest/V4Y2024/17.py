'''Задача 17. В файле содержится последовательность натуральных чисел. Элемен-
ты последовательности могут принимать целые значения от 1 до 100 000 включительно.
Определите количество троек последовательности, в которых сумма элементов трой-
ки не меньше максимального элемента последовательности, делящегося на 16, и ровно
два элемента тройки четырехзначные. В ответе запишите количество найденных тро-
ек, затем максимальную из сумм элементов таких троек. В данной задаче под тройкой
подразумевается три идущих подряд элемента последовательности.'''
I = list() # Произносится как Я ем змея,но задом наперёд: яемз...

maxx = list()
with open("17.txt") as sup:
    line = sup.readline().strip()
    while line != "":
        I.append(int(line))
        #print(line[-2:])
        if int(line) % 16 ==0 :
            maxx.append(int(line))



        line = sup.readline().strip()
m = max(maxx)
print(m)
maxx.clear()


def ysl(num1,num2,num3):
    lnum1 = len(num1)
    lnum2 = len(num2)
    lnum3 = len(num3)
    if lnum1 ==4 or lnum2==4 or lnum3==4:
        if lnum1 == 4 and lnum2 == 4 and lnum3 == 4:
            return False
        if lnum1 ==4 and lnum2==4:
            return True

        if lnum2==4 and lnum3==4:
            return True

        if lnum3==4 and lnum1 ==4:
            return True

    return False

for i in range(len(I)-2):
    if ysl((str(abs(I[i]))),(str(abs(I[i + 1]))),(str(abs(I[i+ 2])))):
        if I[i]+I[i + 1]+I[i + 2] >= m:
            maxx.append(I[i] + I[i + 1] + I[i + 2])



print(len(maxx),max(maxx))
