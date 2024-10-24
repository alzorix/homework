'''В файле 17-384.txt содержится последовательность натуральных
чисел. Элементы последовательности могут принимать целые значения от 1 до 100 000
включительно. Определите количество элементов последовательности, которые больше
любой суммы пары элементов, в которой ровно одно число двухзначное. В ответе
запишите количество найденных элементов, затем минимальный из них. В данной задаче
под парой подразумевается два идущих подряд элемента последовательности'''
#Не помнил как решать,подсмотрел.
spis = list()
with open("File.txt") as sup:
    line = sup.readline().strip()
    while line != "":
        spis.append(str(line))
        line = sup.readline().strip()

max = -float("inf")
for n in range( len(spis) -1):
    if (len(spis[n]) == 2 and len(spis[n + 1]) != 2) or (len(spis[n + 1]) == 2 and len(spis[n])!= 2):
        if int(spis[n]) + int(spis[n+1]) >max:
            max = int(spis[n]) + int(spis[n+1])
print(max)
Variablerequired = list()

for reallyneed in range( len(spis) -1):
    if int(spis[reallyneed]) >max:
        Variablerequired.append(spis[reallyneed])

print(len(Variablerequired),min(Variablerequired))

# Мне кажется,что в два for-а реаллизовать всё это дело проблематично,по этому написал в три.