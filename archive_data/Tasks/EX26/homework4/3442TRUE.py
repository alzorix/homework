with open("26-j10.txt") as fike:
    line = fike.readline().strip().split()
    D = int(line[  0  ])
    E = int(line[  1  ])
    lenfiles  = int(line[   2 ])

    Dfiles = list()
    Efiles = list()

    nosorted = list()

    line = fike.readline().strip()
    while line !="":
        line = int(line)

        nosorted.append(line)
        line = fike.readline().strip()

    nosorted.sort()
    for line in nosorted:

        if line > 500:
            if D >= line:
                lastbalanceD = D
                Dfiles.append(line)
                D  -= line
        else:
            if E >= line:
                lastbalanceE = E
                Efiles.append(line)
                E -= line

    #Ответ в первый раз не сошёлся,начал искать файлы побольше.
    mD=max(Dfiles)
    mE=max(Efiles)
    nosorted.reverse()
    for line in nosorted:
        if mD <= line and line <= lastbalanceD:
            mD = line
            break
    #nosorted.sort()
    for line in nosorted:
        if line <= 500:
            if mE <= line and line <= lastbalanceE:
                mE = line
                break



    print(len(Dfiles)+ len(Efiles),mD+ mE)