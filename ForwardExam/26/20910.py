
#Без понятия как это было рещать обычным способом. Загуглил,чтобы время не тратить
with open("26_20910.txt") as file:
    N,M,K = map(int,file.readline().strip().split())
    line = file.readline().strip()
    data = [M] * (K)
    print(data)
    while line !="":

        x,y = map(int,line.split())
        data[y-1] = min(data[y-1],int(x))

        line = file.readline().strip()
print(data)
min_mesto = 0
max_rid = 0

for mesta in range(1,K):
    para = min(data[mesta]-1,data[mesta-1]-1)
    if para > max_rid:
        max_rid = para
        min_mesto = mesta
print(max_rid,min_mesto)
