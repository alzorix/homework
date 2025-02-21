'''(№ 7966) Текстовый файл 24-310.txt состоит не более чем из 106 символов и содержит
 только цифры шестнадцатеричной системы счисления, а также знаки «+» и «*» (сложения и умножения).
  Определите максимальное количество символов в непрерывной последовательности,
   которая является корректным арифметическим выражением с целыми неотрицательными числами,
   записанными в троичной системе счисления.
В этом выражении никакие два знака арифметических операций не стоят рядом,
в записи чисел отсутствуют незначащие (ведущие) нули и число 0 не имеет знака. '''

with open("7966") as f:
    src_line = f.readline().strip()

temp = list()
true_alfabet = "+*012"
for src_number in src_line:

    if src_number in true_alfabet:
        temp.append(src_number)
    else:
        temp.append("#")
global_line = "".join(temp)
global_line = global_line.replace("2","1")
global_line = global_line.replace("+","*")
global_line = global_line.split("#")


max_dlina = 0
for x in global_line:
 r = x.split("*")

 dlina = 0

 for local_line in r:

    if local_line !="" and (local_line[0] !="0" or local_line == "0"):

        dlina += len(local_line) + 1
        max_dlina = max(max_dlina, dlina - 1)
    elif local_line != "" and local_line[0] =="0":
        max_dlina = max(max_dlina, dlina + 1)
        r = local_line.find("1")

        if r > -1:
            dlina = len(local_line[r::])+1
            max_dlina = max(max_dlina,dlina-1)
        else:
            dlina = 2
            max_dlina = max(max_dlina, dlina - 1)
    else:
        dlina = 0


print(max_dlina)

#11
