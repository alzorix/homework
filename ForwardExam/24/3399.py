from fnmatch import fnmatch
c = 0
with open("24_3399.txt") as file:
    line = file.readline().strip()
    while line !="":
        if fnmatch(line,"195.2?.1?5.14"):
            c+=1
        line = file.readline().strip()
print(c)
#15629
#Самая быстрое решение задачи за 2 года обучения :D