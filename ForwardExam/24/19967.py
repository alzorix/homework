with open("24_19967(1).txt") as file:
    line = file.readline().strip()

line = line.replace("","")

data =line.split("AFD")
data.pop()# первая не начинается
# print(data)
# maxx = 0
# for line in data:
#     for bukva in range(len(line)):
#         try:
#             s = line[0:bukva]
#             maxx = max(maxx,len(s))
#         except:
#             None
# print(maxx) #Почему это вообще выдаёт ответ
'''Текстовый файл состоит не более чем из 106 символов и содержит 
только цифры шестнадцатеричной системы счисления, 
а также знаки «+» и «*» (сложения и умножения).
 Определите максимальное количество символов в непрерывной последовательности, 
 которая начинается символами AFD, 
 за которыми следует правильное арифметическое выражение с целыми неотрицательными числами 
 (без знака), записанными в десятичной системе счисления. В этом выражении никакие два
  знака арифметических операций не стоят рядом.
   В записи чисел отсутствуют незначащие (ведущие) нули.
    В ответе укажите количество символов в найденном выражении.'''
ans = list()
for line in data:

    line = line.replace("2", "1")
    line = line.replace("3", "1")
    line = line.replace("4", "1")
    line = line.replace("5", "1")
    line = line.replace("6", "1")
    line = line.replace("7", "1")
    line = line.replace("8", "1")
    line = line.replace("9", "1")
    line = line.replace("A", "1")
    line = line.replace("B", "1")
    line = line.replace("C", "1")
    line = line.replace("D", "1")
    line = line.replace("E", "1")
    line = line.replace("F", "1")
    line = line.replace("*", "+")
    line = line.split("+")

    current_dlina =0
    for chislo in line:
        if chislo != "" and (chislo[0] != "0" or chislo == "0"):
            current_dlina += len(chislo) + 1
            ans.append(current_dlina - 1)
        elif chislo[0] == "0":
            ans.append(current_dlina + 1)
            break
        else:
            ans.append((current_dlina - 1))
            break
print(max(ans))
#69