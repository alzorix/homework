
start = None
with open("24.txt") as f:
    line = f.readline().strip()
    f.close()

    while line != "":
        t = line.find("PRO")
        if t != -1 and t != 0:
            if line[t-1] == "O":

                if line[t - 2] == "R":
                    start = t-2
                else:
                    start = t-1
            else:
                start = t

#Нет идей по решению
