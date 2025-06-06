with open("24_16269.txt") as file:
    line = file.readline().strip()
start = 0

XX=0
YY=0
ZZ=0


ans = list()
for x in range(len(line)-2):
    fist= line[x]
    second= line[x+1]

    current = line[start:x + 2]

    duo = fist+second
    if duo == "XX":
        XX+=1

    if duo == "YY":
        YY+=1
    if duo == "ZZ":
        ZZ+=1


    if XX ==1 and YY ==1 and ZZ ==1:
        ans.append(len  (line[start:x+2]))

    while XX >1 or  YY >1 or    ZZ >1 :
        start+=1

        current =  line[start:x+2]
        XX = current.count("XX")
        YY = current.count("YY")
        ZZ = current.count("ZZ")
        if start >=x:
            print(current,ZZ)
            exit()
print(max(ans))
#Почему ответ неверный? #11