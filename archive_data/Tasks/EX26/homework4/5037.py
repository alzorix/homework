with open("26-79.txt") as f:
    N,K = f.readline().strip().split()
    K = int(K)

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

for key in keys:
    line = map_carta[key]
    line.sort()
    C =0

    for i in range(len(line)-1):
            if abs(line[i+1] -line[i])-1 == 1:
                C +=1


    if C == K:
        print(key)
        exit()




