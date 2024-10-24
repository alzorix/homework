

count = 1
maxcount=0

one = 0 #Номер начала послед
goodone = 0
fist = True
with open("3351.txt") as s:

    line = s.readline().strip()
    for l in range(len(line)-1):
        #print(line[l])
        if ord(line[l])  > ord(line[l+1]) :
            if fist:
                one = l
                fist = False
            count+=1


        else:
            if count > maxcount:
                maxcount =count
                goodone = one
            count = 1
            fist = True
    if count > maxcount:
        maxcount = count
        goodone = one



print(goodone+1)





