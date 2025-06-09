alfabet = dict()
for p in range(0,20) :
    alfabet[10+p] = chr(ord("A")+p)
with open("24_20010.txt") as  file:
    line = file.readline().strip()
    t = list()
    for x in line:
        if x not in "0*+":

            t.append("1")
        else:
            t.append(x)
    line = "".join(t)

    line = line.replace("+", "1")
    line = line.replace("+", "1")
    line = line.replace("+", "1")
    line = line.replace("+", "1")




    line = line.replace("+","*")
    line = line.replace("**","!")

data = line.split("!")

print(data)
ans = list()
for viraj in data:
    viraj = viraj.strip("*")
    dlina = 0
    Sline = viraj.split("*")
    for local_line in Sline:


        if local_line !="" and (local_line == "0" or local_line[0] != "0" ):
            if len(local_line) ==3:

                dlina+=len(local_line) +1
                ans.append(dlina-1)
            else:
                ans.append(dlina - 1)
                dlina = 0
        elif local_line !="" and local_line[0] == "0":
            r = local_line.find("1")
            if r >0:
                if len(local_line[r::]) == 3:
                    dlina= len(local_line[r::]) +1
                #Не факт,что дальше есть ещё число
            else:
                dlina = 0
        else:
            dlina =0
    ans.append(dlina - 1)
print(max(ans))


