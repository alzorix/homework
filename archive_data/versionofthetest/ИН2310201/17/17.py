'''Файл содержит последовательность натуральных чисел, не превышающих
100 000. Назовём тройкой три идущих подряд элемента последовательности.
Определите количество троек, для которых выполняются следующие условия:
– хотя бы два числа в тройке пятизначные;
– ровно одно число в тройке делится на 3;
– сумма элементов тройки больше максимального элемента
последовательности, запись которого заканчивается на 123. (Гарантируется,
что в последовательности есть хотя бы один элемент, запись которого
заканчивается на 123.)
В ответе запишите два числа: сначала количество найденных троек, затем
максимальную величину суммы элементов этих троек'''


lines = list()
list123 = list()

with open("17.txt") as file:
    line = file.readline().strip()
    while line != "":
        lines.append(str(line))
        if line[-3::] == "123":

            list123.append(int(line))


        line = file.readline().strip()

troiki = list()
amxt =max(list123)
F = list()
for i in range(len(lines)-2):
    #if str(3) in str(lines[i]) and str(3) in str(lines[i +1 ]) and str(3) in str(lines[i + 2]) :
    if int(lines[i]) + int(lines[i+1]) +int(lines[i+2]) > amxt:

        if (len(lines[i]) == 5 and len(lines[i+1])== 5) or (len(lines[i+1]) == 5 and len(lines[i+2])== 5) or (len(lines[i+2]) == 5 and len(lines[i])== 5):
            if (int(lines[i]) % 3 == 0 and  int(lines[i+1]) % 3 != 0 and int(lines[i+2]) % 3 != 0) or (int(lines[i]) % 3 != 0 and  int(lines[i+1]) % 3 == 0 and int(lines[i+2]) % 3 != 0) or (int(lines[i]) % 3 != 0 and  int(lines[i+1]) % 3 != 0 and int(lines[i+2]) % 3 == 0):
                troiki.append((int(lines[i]) + int(lines[i+1]) +int(lines[i+2])))
print(len(troiki),max(troiki))





