bukviposlex = dict()

lastdict = dict()
with open("6286") as file:
    line = file.readline().strip()
    while line!="":
        for i in range(len(line)-1):
            if line[i] == "X":

                if line[i+1] not in bukviposlex:
                    bukviposlex[line[i+1]] = 1
                else:
                    bukviposlex[line[i+1]]+=1

        #После строки
        max_test = max(bukviposlex.values())
        for i in bukviposlex:
            if bukviposlex.get(i) == max_test:
                need_str = i
                if need_str not in lastdict:
                    lastdict[need_str] = 1
                else:
                    lastdict[need_str]+=1


        line = file.readline().strip()
        bukviposlex.clear()

print(max(lastdict.values()))


#928