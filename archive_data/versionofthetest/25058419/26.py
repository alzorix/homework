with open("26.txt") as f:
    line  =f.readline().strip().split()
    numarbyz = int(line[0])
    balance = int(line[1])*1000

    line = f.readline().strip()
    VIP = list()
    while line!="":
        line = int(line)
        if 7000<= line <= 12000:
            VIP.append(line)
        line = f.readline().strip()

    VIP.sort(reverse=True)
    ansewers = list()
    for kg in VIP:
        if balance >= kg:
            balance -= kg
            ansewers.append(kg)




    print(len(ansewers),min(ansewers))

#С РНО: 75 9196