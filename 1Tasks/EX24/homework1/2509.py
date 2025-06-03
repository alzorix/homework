

cout = 1
maxcount=0
with open("2509") as s:

    line = s.readline().strip()
    for l in range(len(line)-1):
        #print(line[l])
        if line[l] != line[l+1]:
            cout+=1
        else:
            if cout > maxcount:
                maxcount =cout
            cout = 1
    if cout > maxcount:
        maxcount = cout
print(maxcount)




