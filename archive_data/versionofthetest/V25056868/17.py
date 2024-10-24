
minn = float("inf")

lines = list()
with open("17.txt") as file:
    line =file.readline().strip()
    while line != "":
        if int(line) < minn:
            minn = int(line)
        lines.append(int(line))
        line = file.readline().strip()

#print("1 step ready")
good_lines = list()
for i in range(len(lines)-1):
    if lines[i] % 55 == minn or lines[i+1] % 55== minn:
        full = lines[i]+lines[i+1]
        good_lines.append(full)
print(len(good_lines),min(good_lines))