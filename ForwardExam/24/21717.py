'''№ 21717 ЕГКР 19.04.25 (Уровень: Средний)

Текстовый файл состоит из символов F, G, Q, R, S и W.
 Определите в этом файле минимальное количество идущих подряд символов,
  среди которых подстрока RSQ встречается ровно 130 раз,
  при этом искомая последовательность не оканчивается символом Q.
Для выполнения этого задания следует написать программу.'''

ans = list()
with open("24_21717.txt") as file:
    line = file.readline().strip()
start = 0
RSQ = 0
for x in range(len(line)-2):
    fist= line[x]
    second= line[x+1]
    third= line[x+2]
    trio = fist+second+third
    if trio == "RSQ":
        RSQ +=1

    if RSQ == 130 and third != "Q":
        ans.append(len(line[start:x+4]))

    while RSQ > 130:
        start+=1
        current =  line[start:x+3]
        RSQ = current.count("RSQ")
        if start >=x:
            print("Что-то странное")
print(min(ans))
#500 -

