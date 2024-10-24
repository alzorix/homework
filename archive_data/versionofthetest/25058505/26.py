with open("26_17881.txt") as file:
    int_students = int(file.readline().strip())
    line = file.readline().strip()


    RATING_VIP= list()
    RATING_normis_CLASS = list()
    RATING_WORKING_CLASS = list()
    RATING_will_be_trash = list()
    RATING_trash = list()


    vip_stipendia = int(int_students * 25//100)


    while line !="":

        ID,math,rus,eng,inf = line.split()
        avarage = (int(math)+ int(eng)+ int(rus)+ int(inf))//4

        index = (math != "2") + (rus != "2") + (inf != "2") + (eng != "2")
        if index ==4:
            RATING_VIP.append((-avarage,ID))
        elif index == 3:
            RATING_normis_CLASS.append(ID)
        elif index ==2:
            RATING_WORKING_CLASS.append(ID)
        elif index == 1:
            RATING_will_be_trash.append(ID)
        elif index == 0:
            RATING_trash.append(ID)
        else:
            print(index)
        line = file.readline().strip()

    RATING_VIP.sort()
    RATING_WORKING_CLASS.sort()
    RATING_normis_CLASS.sort()
    RATING_will_be_trash.sort()
    RATING_trash.sort()

    rating = list()

    rating.extend(  RATING_VIP )
    rating.extend(RATING_normis_CLASS)
    rating.extend(RATING_WORKING_CLASS)
    rating.extend(RATING_will_be_trash )
    rating.extend( RATING_trash)


    for i in range(vip_stipendia):

        last = rating[i]

    print(last[1],RATING_WORKING_CLASS[0])
