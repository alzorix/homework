'''Текстовый файл состоит из десятичных цифр, знаков «+» и «*» (сложения и умножения).
Определите максимальное количество символов в непрерывной последовательности,
 являющейся корректным арифметическим выражением с целыми неотрицательными чётными числами.
 В этом выражении никакие два знака арифметических операций не стоят рядом,
  порядок действий определяется по правилам математики.
  В записи чисел отсутствуют незначащие (ведущие) нули.'''

with open("24.txt") as file:
    line = file.readline().strip()


line = line.replace("+","*")
line = line.replace("2","2")
line = line.replace("3","1")
line = line.replace("4","2")
line = line.replace("5","1")
line = line.replace("6","2")
line = line.replace("7","1")
line = line.replace("8","2")
line = line.replace("9","1")



lines = line.split("*")

max_lenght = 0
global_max_lenght = 0
for local in lines:
    if local != "" and (local[0] !="0" or local == "0") :
        if int(local) % 2 ==0: # 222
            max_lenght += len(local)+1
            global_max_lenght = max(max_lenght-1,global_max_lenght)
        else: # 221
            global_max_lenght = max(max_lenght - 1, global_max_lenght)
            max_lenght = 0 #1+
    elif local != "" and local[0] == "0":
            global_max_lenght = max(max_lenght +1 , global_max_lenght)

            r = min(local.find("1"),local.find("2"))
            if r> -1:
                    if int(local[r::]) % 2 ==0:
                        max_lenght = len(local[r::]) +1
                        global_max_lenght = max(max_lenght - 1, global_max_lenght)
                    else:
                        max_lenght = 0


            else:
                    max_lenght = 2 # 0+


    else:
            max_lenght = 0
            global_max_lenght = max(max_lenght , global_max_lenght)
    global_max_lenght = max(max_lenght - 1, global_max_lenght)
global_max_lenght = max(max_lenght - 1, global_max_lenght)
print(global_max_lenght)
#127

