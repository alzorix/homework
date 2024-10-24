
def find_combination(line:str):

    while line != "":
        last = line



        start_combo = line.find("Z")
        if start_combo != -1:
            if len(line)>=  start_combo+3 + 1:# +1 так как index начинается с 0
                if line[start_combo+2] == "R" and line[start_combo+3] == "O":

                    return True
                else:
                    line = line[start_combo + 1::]
            else:
                line = line[start_combo+1::]

        if last == line:
            return False
    return False
#Ответ: 59





count = 0


with open("2559") as file:
    line = file.readline().strip()
    while line!="":
        if find_combination(line):
            count+=1




        line = file.readline().strip()
print(count)
