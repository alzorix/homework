data = list()
max_ysl = -float("inf")
with open("17.txt") as file:
    line = file.readline()
    while line !="":
        data.append(line)
        if len(str(abs(int(line)))) == 5 and line[-3::] == "43":
            max_ysl = max(max_ysl,int(line))
        else:
            print(line[-3::])
        line = file.readline()
print(max_ysl)