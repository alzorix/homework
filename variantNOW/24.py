'''Текстовый файл состоит из десятичных цифр, знаков «+» и «*» (сложения и умножения).
Определите максимальное количество символов в непрерывной последовательности,
 являющейся корректным арифметическим выражением с целыми неотрицательными чётными числами.
 В этом выражении никакие два знака арифметических операций не стоят рядом,
  порядок действий определяется по правилам математики.
  В записи чисел отсутствуют незначащие (ведущие) нули.'''

with open("24.txt") as file:
    line = file.readline().strip()
    file.close()

line = line.replace("+","*")
line = line.replace("2","1")
line = line.replace("3","1")
line = line.replace("4","1")
line = line.replace("5","1")
line = line.replace("6","1")
line = line.replace("7","1")
line = line.replace("8","1")
line = line.replace("9","1")



lines = line.split("*")

max_lenght = 0
global_max_lenght = 0
for local in lines:
    if local != "" and (local[0] !="0" or local == "0") :
        if int(local) % 2 ==0:
            max_lenght += len(local)+1
            global_max_lenght = max(max_lenght-1,global_max_lenght)
        else:
            max_lenght = 0
    elif local != "" and local[0] == "0":
            global_max_lenght = max(max_lenght +1 , global_max_lenght)
            r = local.find("1")
            if r> 0:
                    if int(local[r::]) % 2 ==0:
                        max_lenght = len(local[r::]) +1
                        global_max_lenght = max(max_lenght - 1, global_max_lenght)
                    else:
                        max_lenght = 0


            else:
                    max_lenght = 2 # 0+


    else:
            max_lenght = 0 # 0+
    global_max_lenght = max(max_lenght - 1, global_max_lenght)
global_max_lenght = max(max_lenght - 1, global_max_lenght)
print(global_max_lenght)
#216

