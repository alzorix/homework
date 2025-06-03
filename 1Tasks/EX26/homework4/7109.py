with open("26-140.txt") as file:
    film_int = file.readline().strip()
    line = file.readline().strip()
    films_lenta = list()
    while line !="":
        st,nd = line.split()
        films_lenta.append((int(st), int(nd) ))
        line = file.readline().strip()
    films_lenta.sort()

    loooongtime = 0

    allmetr = list()

    filmpokaz =  0

    t = list()

    for clock in range(44640):

        for film in films_lenta:
            start,end = film

            if start == clock:
                filmpokaz+=1
            if end == clock:
                filmpokaz-=1

        if filmpokaz != 0:
            loooongtime +=1
            allmetr.append(clock)
        else:
            t.append(loooongtime)
            loooongtime = 0
print(len(allmetr),max(t)) #38032 3014