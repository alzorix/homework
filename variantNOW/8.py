from itertools import product
c = 0
for cortege in product("АКМС",repeat=4):
    true_string = "".join(cortege)
    c+=1
    if "М" not in true_string and "С" not in true_string and "КК" not in true_string:
        print(true_string)
        last = c
print(c)
#256