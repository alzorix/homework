# Текстовый файл состоит из символов F, S и W. Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых подстрока WWF встречается не более 120 раз, а подстрока WSFWW не встречается совсем.
#
# Для выполнения этого задания следует написать программу.

with open("24_19489.txt") as file:
    line = file.readline().strip()
start = 0
WWF = 0
WSFWW = 0
ans = list()
for x in range(len(line)-2):
    fist= line[x]
    second= line[x+1]
    third = line[x+2]
    current = line[start:x + 3]

    trio = fist+second+third
    if trio == "WWF":
        WWF +=1


    if WWF <= 120 and "WSFWW" not in current :
        ans.append(len  (line[start:x+3]))

    while WWF > 120 or "WSFWW" in current:
        start+=1
        current =  line[start:x+3]
        WWF = current.count("WWF")
        if start >=x:
            print(current)
            exit()
            print("Что-то странное")
print(max(ans))
#3080 +