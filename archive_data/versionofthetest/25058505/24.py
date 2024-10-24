with open("24_17878.txt") as f:
    line = f.readline().strip()
    f.close()
line = line.replace("-", "*")

line = line.replace("**", "* *")

line = line.replace("*00", "*0 0")

text = line.split()

max_ = 0


ans = list()

for line in text:
    while len(line) >0 and line[0] in "*":
        line = line[1::]
    while len(line) >1 and line.startswith("0")and line[1].isnumeric():
        line = line[1::]
    while len(line) >0 and line[-1] in "*":
        line = line[:-1]


    if "*" in line:
        ans.append(len(line))
print(max(ans))