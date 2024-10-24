
count = 0




with open("2555") as file:
    line = file.readline().strip()
    while line != "":
        if line.count("S") == line.count("X"):
            count+=1
        line = file.readline().strip()
print(count)