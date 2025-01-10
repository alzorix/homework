'''(№ 7787) Текстовый файл 7787 состоит не более чем из 106 символов и содержит только цифры шестнадцатеричной системы
счисления, а также знаки «+» и «*» (сложения и умножения). Определите максимальное количество символов в непрерывной последовательности,
 которая начинается символами AFD, за которыми следует правильное арифметическое выражение с целыми неотрицательными числами (без знака),
 записанными в десятичной системе счисления. В этом выражении никакие два знака арифметических операций не стоят рядом.
 В записи чисел отсутствуют незначащие (ведущие) нули. В ответе укажите количество символов в найденном выражении. '''


def desit_system(num:str):
    for x in num:
        if x in alfabet:
            return (False,x)
    return (True,"")


with open("7787") as file:
    line = file.readline().strip()



line = line.replace("+","*")
line = line.split("AFD")

alfabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM" # Весь алфавит , так как я не помню буквы шестнадцатеричной системы


c = 0
Last_nice_c = 3 #Если предыдущий AFD_line не попал в else,тогда продолжаем считать и на новой. Тут 3 ,так как первый AFD
# тоже считается частью последовательности

for AFD_line in line[1::]:
    Nice_line_FLAG = True


    local_line = AFD_line.split("*")

    l_c = Last_nice_c
    Last_nice_c = 3


    for candidation_line in local_line:

            if candidation_line !="" and (candidation_line[0] !="0" or candidation_line == "0"):
                    res = desit_system(candidation_line)
                    if res[0]:

                        l_c+=len(candidation_line)+1
                        c = max(c,l_c-1)
                    else:
                        ost = candidation_line.find(res[1])
                        l_c+=len(candidation_line[:ost])

                        c = max(c,l_c)
                        l_c = 0
                        Nice_line_FLAG = False
                        break
            else:
                c = max(c, l_c-1)
                l_c = 0
                Nice_line_FLAG = False
                break
    if Nice_line_FLAG:
        Last_nice_c = l_c +3



print(c)


# 70 -
