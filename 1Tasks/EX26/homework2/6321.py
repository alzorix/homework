all_time = list()
with open("26-112.txt") as file:
    fist_line = file.readline().strip().split()
    kolvo_bank = int(fist_line[0])
    kolvo_client =  int(fist_line[1])

    queue_clients = list()
    line = file.readline().strip()
    while line !="":
        time_start,time = line.split()

        queue_clients.append( (int(time_start),int(time)+int(time_start) ,int(time)  ))


        line = file.readline().strip()


    queue_clients.sort(key=lambda s: s[0])


    ATM = [0]*kolvo_bank
    ATM_stat = [(0,0)] * kolvo_bank
    last_client =0

    for i in range(kolvo_client):

        start,end,time = queue_clients[i]


        for s in range(kolvo_bank):
            if ATM[s] <= start:
                ATM[s] = end
                if start <=1440:

                    ATM_stat[s] = (ATM_stat[s][0]+1,start)
                break
        else:

            m = min(ATM)
            for x in range(len(ATM)):
                if ATM[x] ==m:
                    if ATM[x]<=1440:
                        all_time.append(m - start)

                        ATM_stat[x] = (ATM_stat[x][0] + 1, ATM[x])

                    ATM[x] = ATM[x] +time
                    break
print( max(all_time),max(ATM_stat)[1]) #50% : 663 1439










