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
    last_client =0

    for i in range(kolvo_client):

        start,end,time = queue_clients[i]


        for s in range(kolvo_bank):
            if ATM[s] <= start:
                ATM[s] = end
                if start <=1440:
                    last_client =start
                    ATM_stat[s] +=1
                break
        else:
            #Заходим сюда, если из цикла мы вышли без break
            #Человек отправлятеся в очередь,так как человек не нашёл ни одного свободного банкомата
            m = min(ATM)
            for x in range(len(ATM)):
                if ATM[x] ==m:
                    if ATM[x]<=1440:

                        ATM_stat[x] +=1
                        last_client = ATM[x]
                    ATM[x] = ATM[x] +time
                    break
print(max(ATM_stat), last_client)











