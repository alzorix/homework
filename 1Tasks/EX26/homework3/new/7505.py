with open("26-150.txt") as file:
    line = file.readline().strip()
    kolvo_seat,kolvo_riad,kolvo_mest = list(map(int,line.split()))

    line = file.readline().strip()

    a = [kolvo_riad+1]*(kolvo_mest+1) # Этот список будет хранить min номера рядов для каждого места

    DATA = dict()
    while line != "":
        riad,seat = list(map(int,line.split()))
        print(riad,seat)


        a[seat] = min(a[seat],riad)



        line = file.readline().strip()

    t = 0

    for i in range(1,kolvo_mest):
        t = max(t,min(a[i]-1,a[i+1]-1)) #Ищем максимальный номер ряда перед которым оба места i и i+1 свободны.

    sp = list()
    for i in  range(1,kolvo_mest):
        if min(a[i]-1,a[i+1]-1) == t:

            sp.append(i+1)
    print(t,max(sp))

