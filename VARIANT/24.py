with  open("24_21908.txt") as file:
    line = file.readline().strip()

blackline = "QWERTYUIOPSFGHJKLZXVNM"
new_list_line = list()
for bukva in line:
    if bukva not in blackline:
        new_list_line.append(bukva)
    else:
        new_list_line.append("#")
line = "".join(new_list_line)
data = line.split("#")
#print(data)
from  copy import deepcopy
def normalize(line):
    line = str(line)
    if line [0] == "0":
        l = line
        l = l.replace("2","1")
        l = l.replace("3", "1")
        l = l.replace("4", "1")
        l = l.replace("5", "1")
        l = l.replace("6", "1")
        l = l.replace("7", "1")
        l = l.replace("8", "1")
        l = l.replace("9", "1")
        l = l.replace("A", "1")
        l = l.replace("B", "1")
        l = l.replace("C", "1")
        l = l.replace("D", "1")
        l = l.replace("E", "1")
        l = l.replace("F", "1")
        r = l.find("1")
        if r>0:
            #print(line)
            line = line[r::]

            return str(line)
        else:
            return ""
    else:
        return line





ans = list()
for line in data:
    if line != "":
        line = normalize(line)
        if line !="":
            #print(line)
            ans.append((int(line,14),len(line)))
print(max(ans)[1])
#2599