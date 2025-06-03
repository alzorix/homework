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
    ATM_stat = [0] * kolvo_bank
    fun_client =0
    last_ATM = 0

    for i in range(kolvo_client):

        start,end,time = queue_clients[i]


        for s in range(kolvo_bank):
            if ATM[s] <= start:
                ATM[s] = end
                if start <=1440:
                    fun_client+=1
                    last_ATM = s+1
                    ATM_stat[s] +=1
                break
        else:

            m = min(ATM)
            for x in range(len(ATM)):
                if ATM[x] ==m:
                    if ATM[x]<=1440:
                        last_ATM = x+1

                        ATM_stat[x] +=1
                        fun_client+=1
                    ATM[x] = ATM[x] +time
                    break
print( fun_client,last_ATM)



#1591 4 Верно
