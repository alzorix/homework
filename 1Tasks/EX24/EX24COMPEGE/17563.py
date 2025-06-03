'''Текстовый файл состоит из символов, обозначающих знаки « – », « * » и цифры 0, 7, 8, 9.
Определите в прилагаемом файле максимальное количество идущих подряд символов, которые образуют математически правильную последовательность, в которую входят знаки « – » или « * » и натуральные числа без незначащих нулей.

Файлы к заданию:24.txt'''

with open("24_17563.txt") as f:
    global_line = f.readline().strip()

global_line = global_line.replace("7","1")

global_line = global_line.replace("9","1")
global_line = global_line.replace("8","1")
global_line = global_line.replace("-","*")

global_line = global_line.split("*")


maximum_posl =0
local_posl = 0
for line in global_line:


    if line !="" and (line[0] !="0"):


            local_posl+=len(line) +1
            maximum_posl = max(maximum_posl,local_posl-1)


    elif line !="" and line[0] =="0":
        maximum_posl = max(maximum_posl, local_posl + 1)

        nice_index = line.find("1")
        if nice_index > -1:
            local_posl = len(line[nice_index::]) +1
            maximum_posl = max(maximum_posl, local_posl - 1)

        else:
            local_posl = 2
            maximum_posl = max(maximum_posl, local_posl - 1)

    else:
        local_posl = 0

print(maximum_posl)


#40


