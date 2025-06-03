

cout = 0
maxcount=0
with open("2519") as s:

    line = s.readline().strip()
    for l in range(len(line)):
        #print(line[l])
        if line[l] != "F" and line[l] != "C":
            cout+=1
        else:
            if cout > maxcount:
                maxcount =cout
            cout = 0
    if cout > maxcount:
        maxcount = cout
print(maxcount)

