with open("24.txt") as f:
    line = f.readline().strip()


line = line.replace("-","*")
line = line.replace("6","1")
line = line.replace("7","1")
line = line.replace("8","1")
line = line.replace("9","1")

line = line.split("*")


c = 0
F = False
for candidat in line:


     if candidat != "" and (candidat[0] != "0"):

           c+=1
     elif  candidat != "" and candidat[0] == "0":
            c+=1
            F = True
     else:
            c+=1
print(c,len(line))






