from itertools import product
c = 0
for cortege in product("АКМС",repeat=6): #Тут было 4
    true_string = "".join(cortege)
    c+=1
    if "М" not in true_string and "С" not in true_string and "КК" not in true_string:

        last = c
print(last) #Тут был с

#Я без понятия почему я не увидел ошибки,они на виду.