with open("26-75.txt") as f:
    line = f.readline().strip()
    time = list()
    times_opimize = set()
    line = f.readline().strip()

    while line !="":
        start,end = line.split()
        time.append((int(start),int(end)))
        times_opimize.add(int(start))
        times_opimize.add(int(end))


        line = f.readline().strip()

    time.sort()


    max_pass = 0
    all_time_one = 0
    passanges = 0 #количество людей в автобусе

    for clock in range(max(times_opimize)+1): #Это своего рода часы.Они считает до тех пор,пока в автобус кто-то заходит и кто-то выходит
        if clock in times_opimize: #Условие,мы проходимся по массиву только тогда,когда в данный момент времени clock кто-то заходил или выходил из автобуса

            for i in range(len(time)): #Считаем количество людей в автобусе в момент времени clock
                if time[i][0] == clock:
                    passanges +=1
                if time[i][1] == clock:
                    passanges -=1



        if passanges == 1: #Если в данный момент времени clock количество людей в автобусе было равно 1,тогда увеличиваем all_time_one на 1
            all_time_one+=1

        if max_pass < passanges: #Считаем максимальное кол-во пассажиров,которые были в автобусе вместе
            max_pass = passanges
print(max_pass, all_time_one) #23 11795

