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

g_line = g_line.split("*")





normal_int_global = 0
normal_int = 0

for line in g_line:

    if line != "" and line[0] != "0":
        normal_int +=1 # Если число нормальное, прибавляем 1

        normal_int_global = max(normal_int,normal_int_global)
        #print(normal_int_global)
    elif line != "" and line[0] == "0":
        normal_int_global = max(normal_int,normal_int_global)


        r = line.find("1")



        if r > -1:
            normal_int = 1    # Так как есть проблемы,сбрасываем счётчик с учётом обрубка нормального числа
            normal_int_global = max(normal_int, normal_int_global)

        else:
            normal_int = 0 #Если обрубка нет,то сбрасываем, так как числа должны быть положительными

    else:
        normal_int = 0 #Нет числа,нет и последовательности


print(normal_int_global)
#Всё работает - 44