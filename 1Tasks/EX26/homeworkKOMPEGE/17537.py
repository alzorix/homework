with open("26_17537.txt") as f:
    line = f.readline().strip()
    orders,riads,mests = line.split()
    int_orders= int(orders  )
    int_riads= int(riads  )
    int_mests= int(mests  )

    kinozal = dict()

    line = f.readline().strip()
    while line!="":
        riad,mest =  line.split()

        riad = int(riad)
        mest = int(mest)

        if riad not in kinozal:
            kinozal[riad] = [mest]
        else:
            kinozal[riad].append(mest)
        line = f.readline().strip()
    #print(kinozal)

    kino_riads = list(kinozal.keys())
    #print(kino_riads)
    kino_riads.sort()
    kino_riads.reverse()
    for num_r in kino_riads:
        s = kinozal[num_r]
        print(s)
        break
    # как реализовать проверку?
