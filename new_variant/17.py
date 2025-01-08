data = list()
max_ysl = 0
with open("17.txt") as file:
    line = file.readline().strip()
    while line !="":
        data.append(line)
        if len(str(abs(int(line)))) == 5 and line[-2::] == "43":
            print(1)
            max_ysl = max(max_ysl,int(line))

        line = file.readline().strip()
print(max_ysl)