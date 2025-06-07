'''№ 21717 ЕГКР 19.04.25 (Уровень: Средний)

Текстовый файл состоит из символов F, G, Q, R, S и W.
 Определите в этом файле минимальное количество идущих подряд символов,
  среди которых подстрока RSQ встречается ровно 130 раз,
  при этом искомая последовательность не оканчивается символом Q.
Для выполнения этого задания следует написать программу.'''
#
ans = list()
with open("24_21717.txt") as file:
    line = file.readline().strip()
start = 0
RSQ = 0
for x in range(2,len(line)):
    x= x-2
    fist= line[x]
    second= line[x+1]
    third= line[x+2]
    trio = fist+second+third
    if trio == "RSQ":
        RSQ +=1
        if RSQ == 131 and third == "Q":
            ans.append(len(line[start:x + 2]))


    while RSQ == 130 and third !="Q":
        ans.append(len(line[start:x + 3]))
        start+=1

        current =  line[start:x+3]
        RSQ = current.count("RSQ")
        if start >=x:
            print("Что-то странное")

    if RSQ == 130 and third != "Q":
        ans.append(len(line[start:x+3]))
print(min(ans))
#497

smart_start = 0
RSQ =0
m = float("inf")
for r in range(2,len(line)):
    if line[r-2] +  line[r-1] +  line[r] == "RSQ":
        RSQ +=1
    while RSQ ==130 and line[r] !="Q":
        m = min(m,r-smart_start+1)
        if line[smart_start] + line[smart_start+1] + line[smart_start+2]== "RSQ":
            RSQ-=1
        smart_start+=1
print(m)
#497