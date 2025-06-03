with open("26-115.txt") as file:
    fline = file.readline().strip().split()
    kolvo_trainers = int(fline[0])
    kolvo_clients = int(fline[1])

    fine_clients = 0
    last_trainer = 0

    list_clients = list()
    line = file.readline().strip()
    while line !="":

        start,end = line.split()

        list_clients.append((int(start),int(end)))

        line = file.readline().strip()


    list_clients.sort(key =lambda x:x[0])

    print(list_clients)


    trainers = [0]*kolvo_trainers

    for i in range(kolvo_clients):
        start,end = list_clients[i]
        for x in range(kolvo_trainers):
            if trainers[x] <start:
                trainers[x] = end
                fine_clients+=1
                last_trainer = x+1
                break
print(fine_clients,last_trainer)

#1269 41 ВЕРНО