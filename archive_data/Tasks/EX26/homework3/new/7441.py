with open("26-148.txt") as file:
    zn = file.readline().strip()
    line = file.readline().strip()

    seats = dict()
    while line !=(""):
        rid,mesto = line.split()

        rid = int(rid)
        mesto = int(mesto)
        if rid not in seats:
            seats[rid] = {mesto}
        else:
            seats[rid].add(mesto)


        line = file.readline().strip()
slist = list(seats.keys())
slist.sort()
slist.reverse()

for i in slist:
    line = list(seats[i])
    line.sort()
    #print(line)
    if line[0] >5:
        print(i,line[0]-5)
        exit()
    for index in range(len(line)-1):
        if abs(line[index] - line[index+1]) >5:
            print(i,line[index]+1)
            exit()

#998 10