'''

№ 17878 Демоверсия 2025 (Уровень: Сложный)

Текстовый файл состоит из цифр 0, 6, 7, 8, 9 и знаков арифметических операций «–» и «*» (вычитание и умножение).
 Определите максимальное количество символов в непрерывной последовательности, которая является корректным арифметическим выражением
  с целыми неотрицательными числами.
В этом выражении никакие два знака арифметических операций не стоят рядом,
 в записи чисел отсутствуют незначащие (ведущие) нули и число 0 не имеет знака.
В ответе укажите количество символов.'''


#ЭТО ТРЕТЬЕ РЕШЕНИЕ,оно просто не работает


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





max_id = 0
c_id = 0


for global_line in line_task: # берём условную -0-010110
    global_line = global_line.strip("-")
    global_line = global_line.strip("*")
    global_line = global_line.strip("-")# удаляем знаки по краям, так как они при любом случае нам не подходят из-за line.replace("--", " ")
    # имеем 0-010110

    #local_lines = global_line.split("*") #Подгоняем под наш шаблон,чтобы работал нормально. ( Чтобы не переписывать все if-ы)
    # имеем 0 - 010110
    local_posl = 0

    c = 0
    m = 0
    while m <= len(global_line)-1:

            t = global_line[m] + global_line[m+1]
            if t != "-0" and  t != "*0" and (global_line[m] != "0" ):
                c+=1
                max_id = max(max_id,c)
                m+=1
            elif t == "*0":
                r = global_line.find("1")
                if r != -1:
                    global_line= global_line[r::]
                    c = 0
                    m = 1

                else:
                    c = 0
                    m += 2



            else:
                max_id = max(max_id, c)
                c = 0
                m+=1


print(max_id)








#130



