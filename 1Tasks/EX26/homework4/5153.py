with open("26-80.txt") as f:
    K = f.readline().strip()
    N = int(K)

    line = f.readline().strip()

    map_carta = dict()
    while line !="":


        riad,mesto = line.split()
        riad = int(riad)
        mesto = int(mesto)
        if riad not  in map_carta:
            map_carta[riad] = [mesto]
        else:
            map_carta[riad].append(mesto)


        line = f.readline().strip()
    f.close()

keys = map_carta.keys()
keys = list(keys)
keys.sort(reverse= True)

#print(K)

otvet_list = list()
count = 0
#Если имеется ввиду,чтобы плодоносили и досаженные деревья.
for key in keys:
    line = map_carta[key]
    line.sort()

    l_count = 0

    for i in range(len(line)-1):
            chislo_need_trees =(abs(line[i+1] -line[i]) -1) //4 # раccтояние между местами 10 метров,т.е. 4 места  - 40 метров

            if chislo_need_trees !=0:

                count+=chislo_need_trees
                l_count +=chislo_need_trees
    if l_count !=0:
        otvet_list.append((l_count,key))



print(count,max(otvet_list)[1])# 5188255 4902 - 50%



# Если имеется ввиду,чтобы плодоносили все прижившиеся деревья:
otvet_list = list()
count = 0
for key in keys:
    line = map_carta[key]
    line.sort()

    l_count = 0

    for i in range(len(line)-1):
        sosedstvpo =0
        if (abs(line[i+1] -line[i])) <= 4:
            sosedstvpo+=1


        if sosedstvpo == 0:

                count+= 1
                l_count += 1
    if l_count !=0:
        otvet_list.append((l_count,key)) #3759 4902



print(count,max(otvet_list)[1])# 3769 4902 - 50%

