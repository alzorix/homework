with open("26-129.txt") as file:
    N = file.readline().strip()
    line = file.readline().strip()

    transport = [0]* int(N)
    detail_index =1
    start= 0
    end = len(N)
    usedtime = list()
    last = 0


    details = list()
    while line!="":
        shlif,colorize = line.split()
        shlif = int(shlif)
        colorize = int(colorize)
        F = False
        if min(shlif,colorize) == shlif:
            F = True

        details.append((shlif,colorize,detail_index,F))


        # if min(shlif,colorize) not in usedtime:
        #     if min(shlif,colorize) == shlif:
        #         transport[start] = detail_index
        #         usedtime.append(shlif)
        #         last = detail_index
        #         usedtime.append(colorize)
        #         start+=1
        #     else:
        #         transport[end] = detail_index
        #         usedtime.append(shlif)
        #         usedtime.append(colorize)
        #         last = detail_index
        #         end -=1
        detail_index +=1
        line = file.readline().strip()


details.sort()

for i in details:
 shlif,colorize,detail_index,F = i
 if min(shlif,colorize) not in usedtime:
    if F:
        transport[start] = detail_index
        usedtime.append(shlif)
        last = detail_index
        usedtime.append(colorize)
        start+=1
    else:
        transport[end] = detail_index
        usedtime.append(shlif)
        usedtime.append(colorize)
        last = detail_index
        end -=1




for i in range(len(transport)):
    if transport[i] == last:
        print(last,i) #997 488 -50% # с сортир detail_index,F





