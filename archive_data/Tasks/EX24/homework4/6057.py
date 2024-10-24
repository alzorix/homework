

maxcountA = -float("inf")

currentbukva = ""
goodbukva = ""
kolv_bukv = float("inf")
with open("6057") as file:
    line = file.readline().strip()
    count = 1
    while line !="":

        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                count+=1
                #currentbukva = line[i]

            else:

                if count > maxcountA:
                    #maxcountAstr = line
                    maxcountA = count
                    goodbukva = line[i]
                    kolvo_bukv = line.count(goodbukva)




                    #dlinastroki = len(line)
                elif count ==maxcountA:
                    if line.count(line[i]) <kolvo_bukv:
                        #maxcountAstr = line
                        maxcountA = count
                        goodbukva = line[i]
                        kolvo_bukv = line.count(goodbukva)


                count = 1

        if count > maxcountA:
            #maxcountAstr = line
            maxcountA = count
            goodbukva = line[i]
            kolvo_bukv = line.count(goodbukva)

            # dlinastroki = len(line)
        elif count == maxcountA:
            if line.count(line[i]) < kolvo_bukv:
                #maxcountAstr = line
                maxcountA = count
                goodbukva = line[i]
                kolvo_bukv = line.count(goodbukva)

        line = file.readline().strip()


print(kolvo_bukv)



#8