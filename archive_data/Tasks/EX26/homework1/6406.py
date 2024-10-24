with open("files/26-119.txt") as file:
    fist_line = file.readline().strip().split(" ")

    kolvo_auto = int(fist_line[0])
    auto = int(fist_line[1]) #L
    buss = int(fist_line[2]) #N

    passanges = auto+buss

    list_passanges = list()

    line = file.readline().strip()
    while line != "":
        start_time,time,type = line.split(" ")

        list_passanges.append((int(start_time),int(start_time)+int(time),type))
        line = file.readline().strip()

    list_passanges.sort()


    iacheki = list()
    for  a in range(auto):
        iacheki.append((0,ord("A")))

    for b in range(auto,passanges):
        iacheki.append((0,ord("B")))


    count_funny_buss = 0
    count_bad_autos = 0


    for i in range(kolvo_auto):
        start = list_passanges[i][0]
        FLAG = True
        end = list_passanges[i][1]
        type = list_passanges[i][2]
        for s in range(len(iacheki)):

            if iacheki[s][0] <= start:
                if iacheki[s][1] >= ord(type):

                    iacheki[s] = (end,iacheki[s][1])


                    if type == "B":
                        count_funny_buss+=1

                    FLAG = False
                    break
        if FLAG:

            count_bad_autos +=1

print(count_funny_buss,count_bad_autos)

#900 437 - ответ неверный