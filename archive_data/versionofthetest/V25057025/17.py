
maxx = -float("inf")

lines = list()
with open("17.txt") as file:
    line =file.readline().strip()
    while line != "":
        if int(line) > maxx and line[-1] == "7" and len(str(abs(int(line)))) == 4:
            maxx = int(line)
        lines.append(line)
        line = file.readline().strip()

#print(maxx)
good_lines = list()

def ysl(num):
    if len(str(abs(int(num)))) == 4:
        if num[-1] == "7":
            return True
    return False




for i in range(len(lines)-2):
    if ysl(lines[i]) +ysl(lines[i+ 1]) +ysl(lines[i+ 2])  >1:
        if int(lines[i]) +int(lines[i+ 1]) +int(lines[i+ 2]) > maxx:

            full = int(lines[i]) +int(lines[i+ 1]) +int(lines[i+ 2])
            good_lines.append(full)
print(len(good_lines), max(good_lines))


#6 84385

