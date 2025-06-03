with open("26_17565.txt") as file:
    int_candidats,mesta = file.readline().strip().split()
    int_candidats = int(int_candidats)
    mesta = int(mesta)
    line = file.readline().strip()
    candidats = list()
    candidats_D = dict()
    balls = set()
    while line!="":
        ID,one_ex,two_ex,three_ex,sobes = line.split()
        ID = int(ID)
        ball = int(one_ex)+ int(two_ex)+ int(three_ex)
        candidats.append((ball,int(sobes),ID))#ball,sobes,id

        if ball not in candidats_D:
            candidats_D[ball] = {(ball,int(sobes),ID)}
        else:
            candidats_D[ball].add((ball,int(sobes),ID))




        balls.add(ball)
        line = file.readline().strip()

    mball = max(balls)
    #print(mball,len(candidats_D),len(candidats))

    while mball !=0:

        DATA  = candidats_D.get(mball)

        if DATA != None:
            DATA = list(DATA)


            if len(DATA) < mesta:
                mesta -= len(DATA)
                mball-=1
                info_ID = DATA[len(DATA)-1][2]
            else:
                print(info_ID,len(DATA))

                exit()
        else:
            mball -= 1



#7600410 14