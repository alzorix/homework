data =list()
with open("26_10107.txt") as file:
    N = file.readline().strip()
    line = file.readline().strip()
    while line !="":
        start,end = map(int,line.split())
        data.append((start,end))
        line = file.readline().strip()
data.sort(key=lambda x:x[1])
print(data)
current_end = 0
kolvo = 0

hist_end = list()
for sobitie in data:
        start, end = sobitie
        if start>=current_end:

                current_end = end
                hist_end.append(end)
                kolvo+=1

#опять на те же грабли.
#Как адекватно это посчитать?
#Товарищ из решения нашёл максимальную разницу между двумя последними,не трогая первую часть.
#Только после просмотра решения я вспомнил,что мы так делали.

max_raznica = 0


t = hist_end[-2]
for x in data:
    start, end = x
    if start >= t:
        max_raznica = max(max_raznica,start-t)
print(kolvo,max_raznica)