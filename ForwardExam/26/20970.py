data = list()
with open("26_20970.txt") as file:
    N,K = file.readline().strip().split()
    line = file.readline().strip()
    while line != "":
        time_start,repair,number = line.split()
        data.append((int(time_start),int(repair),int(number)-1))
        line = file.readline().strip()

masters = [[] for _ in range(int(K))]
data.sort()
#print(data)

utilisation = 0
repairs_count = 0
for time in range(2000):
    for master in masters:
        for time_ended in master:
            if time_ended <= time:
                repairs_count+=1
                master.remove(time_ended)
    for item in data:
        start_time =item[0]
        if start_time == time:
            current_item = item
            repair_time = current_item[1]
            if current_item[2] !=0:
                id =  current_item[2]
                #print(masters[id])
                if len(masters[id]) >=5:
                    utilisation+=1
                else:
                    if len(masters[id]) ==0:
                        masters[id] = [start_time+repair_time]
                    else:
                        masters[id].sort() #Такая запись не нужна,достаточно max(masters[id]) + repair_time
                        masters[id].append(max(max(masters[id]),start_time) + repair_time)
            else:
                masters.sort(key=lambda x:len(x))
                if masters[0] == min(masters):
                    id = 0
                    if len(masters[id]) >= 5:
                        utilisation += 1
                    else:
                        if len(masters[id]) == 0:
                            masters[id] = [start_time + repair_time]
                        else:
                            masters[id].sort()  # Такая запись не нужна,достаточно max(masters[id]) + repair_time
                            masters[id].append(max(max(masters[id]), start_time) + repair_time)
print(utilisation,repairs_count)