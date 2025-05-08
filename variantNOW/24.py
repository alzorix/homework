'''Текстовый файл состоит из десятичных цифр, знаков «+» и «*» (сложения и умножения).
Определите максимальное количество символов в непрерывной последовательности,
 являющейся корректным арифметическим выражением с целыми неотрицательными чётными числами.
 В этом выражении никакие два знака арифметических операций не стоят рядом,
  порядок действий определяется по правилам математики. В записи чисел отсутствуют незначащие (ведущие) нули.'''

with open("24.txt") as file:
    line = file.readline().strip()
    file.close()

line = line.replace("+","*")


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
    elif local != "" and local == "0":
            global_max_lenght = max(max_lenght +1 , global_max_lenght)
            temp = list()
            for ss in range(1,10):
                if local.rfind(f"{ss}") > 0:

                    temp.append(local.rfind(f"{ss}"))
            r = min(temp)
            if r> 0:
                if int(local[r::]) % 2 ==0:
                    max_lenght = len(local[r::]) +1
                    global_max_lenght = max(max_lenght - 1, global_max_lenght)

            else:
                max_lenght = 2
                global_max_lenght = max(max_lenght - 1, global_max_lenght)
    else:
            max_lenght = 0
print(global_max_lenght)
#216

