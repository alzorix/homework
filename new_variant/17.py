data = list()
max_ysl = 0
with open("17.txt") as file:
    line = file.readline()
    while line !="":
        data.append(line)
        if len(str(abs(int(line)))) == 5 and line[-3::] == "43":
            print(1)
            max_ysl = max(max_ysl,int(line))

        line = file.readline()
print(max_ysl)