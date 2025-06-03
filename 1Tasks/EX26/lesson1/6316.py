with open("files/26-111.txt") as file:
    kolvo_iacheek = int(file.readline().strip())
    passanges = int(file.readline().strip())
    print(kolvo_iacheek,passanges)
    list_passanges = list()

    line = file.readline().strip()
    while line != "":
        d,r = line.split(" ")
        #print(d,r)


        list_passanges.append((int(d),int(r)))
        line = file.readline().strip()

    list_passanges.sort()
    print(list_passanges)

    iacheki = [0]*kolvo_iacheek
    count_funny_passanges = 0
    last_number_iacheki=0

    for i in range(passanges):
        start = list_passanges[i][0]
        end = list_passanges[i][1]
        for s in range(len(iacheki)):
            if iacheki[s] < start:
                iacheki[s] = end
                count_funny_passanges +=1
                last_number_iacheki = s+1
                break
print(count_funny_passanges,last_number_iacheki)

