with open("26-130.txt") as file:
    pos = file.readline().strip()
    line =  file.readline().strip()
    people = list()

    while line !="":

        start,end = line.split()
        people.append((int(start),int(end)))
        line = file.readline().strip()
    people.sort()
    temp = set()
    peopleinshop=0
    peopleinshop_last = 21312312
    itslong =0
    lastlong = 0
    itslongpeople = 0
    peak = 0
    times = list()
    for clock in range(1441):
        peopleinshop_last = peopleinshop #сохраняем предыд результат
        for i in range(len(people)):
            if people[i][0] == clock:
                peopleinshop+=1
            if people[i][1] == clock-1:
                peopleinshop-=1

        temp.add(peopleinshop)
        if peopleinshop == peopleinshop_last: # в течение которых число посетителей, находящихся в магазине, не изменялось
            itslong+=1


        else:
            if itslong !=0:
                 if peopleinshop_last > itslongpeople: #Далее менеджер выбирает пики посещаемости – промежутки времени, когда количество посетителей в магазине было наибольшим.
                    itslongpeople = peopleinshop_last
                    peak=1
                    itslong =0

                 elif  peopleinshop_last == itslongpeople:
                    itslongpeople = peopleinshop_last
                    peak+=1
                    itslong =0

print(peak,itslongpeople)#1 644






