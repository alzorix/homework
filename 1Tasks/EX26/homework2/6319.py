with open("26-112.txt") as file:
    fline = file.readline().strip().split()

    count_ATM = int(fline[0])
    kolvo_clients =int(fline[1])
    line = file.readline().strip()


    list_clients = list()


    while line!="":

        start,time = line.split()

        list_clients.append((int(start),int(time),int(start)+int(time))) #СТАРТ ВРЕМЯ_ОБСЛ КОНЕЦ

        line = file.readline().strip()


    list_clients.sort(key = lambda x: x[0] )


    status_ATM = [0]*count_ATM
    ATM_STAT = [(0,0)] * count_ATM #колво обсл за 24ч и время нач обсл





    for i in range(kolvo_clients):
        start,time,end = list_clients[i]
        for x in range(count_ATM):
            if status_ATM[x] <= start:
                status_ATM[x] = end

                if start <= 1440:
                    ATM_STAT[x] = (ATM_STAT[x][0]+1,start)
                break
        else:
            m = min(status_ATM)
            for x in range(len(status_ATM)):
                if status_ATM[x] == m:
                    if m <= 1440:
                        ATM_STAT[x] = (ATM_STAT[x][0]+1,m)
                    status_ATM[x] = status_ATM[x] + time
                    break


print(min(ATM_STAT)) # (39, 1431) НЕВЕРНО