with open("24_20909.txt") as file:
    line = file.readline().strip()
start = 0
AB = 0
ans = list()
for x in range(len(line)-2):
    fist= line[x]
    second= line[x+1]

    duo = fist+second
    if duo == "AB":
        AB +=1

    if AB == 100:
        ans.append(len(line[start:x+2]))

    while AB > 100:
        start+=1
        current =  line[start:x+2]
        AB = current.count("AB")
        if start >=x:
            print("Что-то странное")
print(max(ans))
#750+