'''

№ 18285 (Уровень: Сложный)

(Л. Шастин) Текстовый файл состоит из десятичных цифр, знаков «+» и «*» (сложения и умножения).
 Рассматриваются непрерывные последовательности символов, которые являются корректными арифметическими выражениями
  с целыми положительными числами. В этих выражениях никакие два знака арифметических операций не стоят рядом,
   порядок действий определяется по правилам математики. В записи чисел отсутствуют незначащие (ведущие) нули.
    Определите максимальное количество чисел, входящих в одну из таких последовательностей.

Файлы к заданию:24.txt'''
with open("24_18285.txt") as f:
    g_line = f.readline().strip()


g_line = g_line.replace("1","1")
g_line = g_line.replace("2","1")
g_line = g_line.replace("3","1")
g_line = g_line.replace("4","1")
g_line = g_line.replace("5","1")
g_line = g_line.replace("6","1")
g_line = g_line.replace("7","1")
g_line = g_line.replace("8","1")
g_line = g_line.replace("9","1")


g_line = g_line.replace("+","*")
g_line = g_line.split("*0*")
L = list()
for x in g_line:
    s = x.split("*")
    #print(s)
    for f in s:
        L.append(f)
g_line = L





global_int = 0
local_int = 0

for line in g_line:
    if line != "" and (line == "0" or line[0] != "0"):
        local_int += len(line)+1
        global_int = max(global_int,local_int-1)
    elif line != "" and line[0] == "0":
        global_int = max(global_int, local_int + 1)
        r = line.find("1")
        if r > -1:
            local_int = len(line[r::]) +1
            global_int = max(global_int, local_int - 1)
        else:
            local_int =2
            global_int = max(global_int, local_int - 1)
    else:
        local_int =0

print(global_int)
#Неверно
