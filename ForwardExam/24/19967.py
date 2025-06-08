
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
with open("24_19967(1).txt") as file:
    line = file.readline().strip()

data =line.split("AFD")
data = data[1::]# первая не начинается c AFD
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
    line = line.replace("A", "!")
    line = line.replace("B", "!")
    line = line.replace("C", "!")
    line = line.replace("D", "!")
    line = line.replace("E", "!")
    line = line.replace("F", "!")
    line = line.replace("*", "+")
    #print(line[0:300]) #111+111+111+111+111+111+111+0111+111+111+0111+1000111+111111+111+111111+111+111+111+0111+!111111+11+
    line = line.split("!")
    line = line[0] #111+111+111+111+111+111+111+0111+111+111+0111+1000111+111111+111+111111+111+111+111+0111+
    #print(line)
    line = line.split("+")
    #print(line) #['111', '111', '111', '111', '111', '111', '111', '0111', '111', '111', '0111', '1000111',
    current_dlina =0
    for chislo in line:
        if chislo != "" and (chislo[0] != "0" or chislo == "0"):
            current_dlina += len(chislo) + 1
            ans.append(current_dlina - 1)
        elif chislo != "" and chislo[0] == "0":
            ans.append(current_dlina + 1)
            break
        else:
            ans.append(current_dlina - 1)
            break
    print(current_dlina)
print(max(ans)+3) #за AFD
#72
