'''Текстовый файл состоит из десятичных цифр, знаков «+» и «*» (сложения и умножения).
Определите максимальное количество символов в непрерывной последовательности, являющейся корректным арифметическим выражением
с целыми неотрицательными числами (без знака), значение которого равно нулю. В этом выражении никакие два знака арифметических операций не стоят рядом,
порядок действий определяется по правилам математики. В записи чисел отсутствуют незначащие (ведущие) нули.

В ответе укажите количество символов.'''


with open("24_17685.txt") as f:
    line = f.readline().strip()

line=  line.replace("++","#")

line=  line.replace("+*","#")

line=  line.replace("*+","#")

line=  line.replace("**","#")

zero_true_max = 0

for local_line in line.split("#"):

    if len(local_line) > zero_true_max:
        for index_local_line in range(len(local_line)-1):
            if local_line[index_local_line] != "+" and local_line[index_local_line] != "*" and not (local_line[index_local_line] == "0" and local_line[index_local_line+1].isdigit()):
                line_perebor = local_line[index_local_line]

                for id_current_digit in range(index_local_line + 1,len(local_line)):
                    line_perebor += local_line[id_current_digit]

                    if line_perebor[-1] != "+" and line_perebor[-1] != "*" and eval(line_perebor) == 0:
                        zero_true_max = max(zero_true_max,len(line_perebor))
print(zero_true_max)

#169