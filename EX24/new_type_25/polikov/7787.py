'''(№ 7787) Текстовый файл 7787 состоит не более чем из 106 символов и содержит только цифры шестнадцатеричной системы
счисления, а также знаки «+» и «*» (сложения и умножения). Определите максимальное количество символов в непрерывной последовательности,
 которая начинается символами AFD, за которыми следует правильное арифметическое выражение с целыми неотрицательными числами (без знака),
 записанными в десятичной системе счисления. В этом выражении никакие два знака арифметических операций не стоят рядом.
 В записи чисел отсутствуют незначащие (ведущие) нули. В ответе укажите количество символов в найденном выражении. '''




with open("7787") as file:
    sline = file.readline().strip()



sline = sline.replace("+","*")


sline = sline.replace("2","1")
sline = sline.replace("3","1")
sline = sline.replace("4","1")
sline = sline.replace("5","1")
sline = sline.replace("6","1")
sline = sline.replace("7","1")
sline = sline.replace("8","1")
sline = sline.replace("9","1")

sline = sline.replace("AFD","!")

whitelist= "1234567890*!"
S = list()
for l in sline:
    if l in whitelist:
        S.append(l)
    else:
        S.append("#")


line = "".join(S)

line = line.split("!")

F = list()

maximum_posl = 0

def C():
    return input()

for local_line in line:
    local_line = C()

    c  = 0
    F = True

    src = local_line.split("#")[0]

    clear_lines = src.split("*")

    local_posl = 0

    for line in clear_lines:
        if F:

            if line != "" and (line[0] != "0" or line =="0"):

                local_posl += len(line) + 1
                maximum_posl = max(maximum_posl, local_posl - 1)
            else:
                F = False



        else:
            break
    break


print(maximum_posl)
#163 :/
