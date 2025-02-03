''' 	(№ 7789) Текстовый файл 24-307.txt состоит не более чем из 106 символов и содержит только цифры шестнадцатеричной системы счисления,
 а также знаки «+» и «*» (сложения и умножения). Определите максимальное количество символов в непрерывной последовательности,
  которая заканчивается символами CB, перед которыми следует правильное арифметическое выражение с целыми неотрицательными числами (без знака),
  записанными в десятичной системе счисления. В этом выражении никакие два знака арифметических операций не стоят рядом.
  В записи чисел отсутствуют незначащие (ведущие) нули. В ответе укажите количество символов в найденном выражении.'''


alfabet = "1234567890!+*"



with open("7789") as f:
    src_line = f.readline().strip()
    f.close()




src_line = src_line.replace("CB","!")
temp = list()
for x in src_line:
    if x in alfabet:
        temp.append(x)
    else:
        temp.append("#")

join_line = "".join(temp)
join_line = join_line.replace("+","*")
join_line = join_line.replace("**","#")
join_line = join_line.replace("2","1")
join_line = join_line.replace("3","1")
join_line = join_line.replace("4","1")
join_line = join_line.replace("5","1")
join_line = join_line.replace("6","1")
join_line = join_line.replace("7","1")
join_line = join_line.replace("8","1")
join_line = join_line.replace("9","1")




line_input_src = join_line.split("!") # 0123456789#*

#print(line_input_src[0])
all = 0
for input_line in line_input_src:
    lines_input_data = input_line.split("#")
    input_line_from_lines = lines_input_data[-1]

    infl = input_line_from_lines
    infl = infl.split("*")
    #print(input_line)
    #print(input_line_from_lines)


    local = 0
    print(infl)

    for symbols in infl:

        if symbols !="" and (symbols =="0" or symbols[0] !="0" ):
            local+=len(symbols) +1

        elif symbols !="" and symbols[0] =="0" :
            r = symbols.rfind("1")
            if r> 0:
                local = len(symbols[r::]) +1
            else:
                local = 2
        else:
            local = 0


    all = max(all,local-1)
print(all)

