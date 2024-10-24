with open("26-39.txt") as file:
    line = file.readline().strip().split()
    count_cont = int(line[0])
    massmax = int(line[1])

    list_mass = list()
    line = file.readline().strip()

    VIP =list()
    while line !="":
        intline = int(line)
        if 180 <=intline<= 200:
                VIP.append(intline)
        else:
         list_mass.append(intline)
        line = file.readline().strip()

    VIP.sort()
    VIP.reverse() #Грузы массой от 180 до 200 кг включительно грузят в первую очередь, выбирая грузы по убыванию массы, начиная с самого тяжёлого.
    list_mass.sort()

    good = list()


    for i in range(len(VIP)):
        if VIP[i] <= massmax:
            massmax -=VIP[i]
            good.append(VIP[i])
        else:
            break

    fix_mass = massmax

    good2 = list()
    perem = 0

    for i in range(len(list_mass)):
        if list_mass[i] <= massmax:
            massmax -=list_mass[i]
            good2.append(list_mass[i])
            perem = i

    K = len(list_mass) -1
    while perem >= 0:
        while K >= 0:
            if sum(good2) - good2[perem] + list_mass[K] <= fix_mass and list_mass[K] != 0 :
                good2[perem] =  list_mass[K]
                list_mass[K] = 0
                perem-=1
                break
            else:
                K-=1


print(len(good)+len(good2),sum(good)+sum(good2))



