database = list()
max_time = -float("inf")
with open("26.txt") as file:
    int_parks,int_orders = file.readline().strip().split()
    line = file.readline().strip()
    while line != "":
        start,time,paks_start,parks_end = line.split()
        end = int(start)+int(time)
        database.append((int(start),end,int(paks_start)-1,int(parks_end)-1)) # start, end, paks_start,parks_end
        if end >= max_time:
            max_time = end
        line = file.readline().strip()

database.sort(key= lambda  x:x[0])
parks = [0]* int(int_parks)

need_parks = [0]* int(int_parks)

count_realtime = 0

max_realtime = list()

for time in range(0,max_time+1):
    for id in range(len(database)):
        start, end, paks_start, parks_end = database[id]


        if start == time:

            count_realtime+=1



            if parks[paks_start] == 0:
                need_parks[paks_start] +=1
            elif parks[paks_start] > 0:
                parks[paks_start]-=1
            else:
                print("ERROR")
                exit()

        if end == time:
            parks[parks_end] += 1
            count_realtime-=1

        max_realtime.append((count_realtime,-time))







find = max(need_parks)
for i in range(len(need_parks)):
    if need_parks[i] == find:
        print(abs(max(max_realtime)[1]),i+1)
        exit()

