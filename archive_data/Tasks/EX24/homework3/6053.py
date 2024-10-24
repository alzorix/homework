'''(№ 6053) Текстовый файл 24-241.txt состоит не более чем из 106 символов и содержит только латинские буквы A, B, C, D, E, F, O.
Определите длину самой длинной цепочки символов, которая начинается и заканчивается буквой O,
 а между двумя последовательными буквами O содержит не более двух букв F и произвольное количество других букв. '''


start_ananlyze = None
start = True
str_all = list()
count_F = 0
last_F = None
with open("6053") as lines:
    line = lines.readline().strip()
    for l in  range(0,len(line)):
        if line[l] =="O":
            if start:
                start_index = l
                count_F =0
                start = False


            else:
                if count_F < 3:
                    last_F = l

                else:
                    if last_F != None:

                        str_all.append(last_F-start_index+1)
                        start_index = l
                        count_F = 0
                        #start = True
                        last_F = None
            count_F = 0



        else:
            if line[l] == "F":
                count_F +=1




print(max(str_all))



