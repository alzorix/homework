'''

№ 17878 Демоверсия 2025 (Уровень: Сложный)

Текстовый файл состоит из цифр 0, 6, 7, 8, 9 и знаков арифметических операций «–» и «*» (вычитание и умножение).
 Определите максимальное количество символов в непрерывной последовательности, которая является корректным арифметическим выражением
  с целыми неотрицательными числами.
В этом выражении никакие два знака арифметических операций не стоят рядом,
 в записи чисел отсутствуют незначащие (ведущие) нули и число 0 не имеет знака.
В ответе укажите количество символов.'''


with open("24_17878.txt") as f:
    line_task = f.readline().strip()

line_task = line_task.replace("6","1")
line_task = line_task.replace("7","1")
line_task = line_task.replace("8","1")
line_task = line_task.replace("9","1")

#line_task = line_task.replace("*","-") # идём противоположной дорогой. *0 нам так же не подходит,как и -0

# Вспоминаем про существование *0

line_task = line_task.replace("--", " ") # Убираем всякую дрянь
line_task = line_task.replace("*-", " ")
line_task = line_task.replace("-*", " ")
line_task = line_task.replace("**", " ")
line_task = line_task.split(" ")


maximum_posl = 0



def ysl(num):
    if "-0" in num:

        start_len = -1
        max_len = -1
        end_len = -1


        last_bad = -1
        for index in range(len(num)-1):
            if num[index] + num[index+1] == "-0":
                if last_bad == -1:
                    last_bad = index
                    start_len = index
                else:
                    max_len = max(max_len, index-last_bad+1)

                    end_len = len(num) - (index+1) -1
        return (False,start_len,end_len,max_len)





    else:
        return (True,0,0,0)








for global_line in line_task: # берём условную -0-010110
    global_line = global_line.strip("-")
    global_line = global_line.strip("*")
    global_line = global_line.strip("-")# удаляем знаки по краям, так как они при любом случае нам не подходят из-за line.replace("--", " ")
    # имеем 0-010110

    local_lines = global_line.split("*") #Подгоняем под наш шаблон,чтобы работал нормально. ( Чтобы не переписывать все if-ы)
    # имеем 0 , 010110
    local_posl = 0


    for line in local_lines:


            if line != "" and (line[0] != "0"):
                status,start,end,max_len = ysl(line)
                if status == True:

                    local_posl += len(line) + 1
                    maximum_posl = max(maximum_posl, local_posl - 1)
                else:
                    local_posl += start +1
                    maximum_posl = max(maximum_posl, local_posl - 1)

                    local_posl = max_len
                    maximum_posl = max(maximum_posl, local_posl)

                    local_posl = end + 1
                    maximum_posl = max(maximum_posl, local_posl - 1)






            elif line != "" and line[0] == "0":

                status, start, end, max_len = ysl(line)

                maximum_posl = max(maximum_posl, local_posl + 1)

                nice_index = line.find("1")
                if status == True:
                    if nice_index > -1:
                        local_posl = len(line[nice_index::]) + 1
                        maximum_posl = max(maximum_posl, local_posl - 1)

                    else:
                        local_posl = 2
                        maximum_posl = max(maximum_posl, local_posl - 1)
                else:
                    if nice_index > -1 and  start > nice_index + 1:
                        local_posl = len(line[nice_index:start])
                        maximum_posl = max(maximum_posl, local_posl )
                        local_posl = end + 1
                        maximum_posl = max(maximum_posl, local_posl - 1)
                    else:
                        local_posl = len(line[nice_index::])

                        if local_posl < end:
                            local_posl+=1
                            maximum_posl = max(maximum_posl, local_posl )
                        else:
                            local_posl = end + 1
                            maximum_posl = max(maximum_posl, local_posl - 1)

            else:
                local_posl = 0

print(maximum_posl)


#130






