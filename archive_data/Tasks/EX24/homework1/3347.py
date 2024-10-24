cout = 1
maxcount=0

with open("3347") as s :
    line = s.readline().strip()
    line = str(1111145111111)
    for l in range(len(line)-1):
        if line[l] == line[l+1]:
            cout+=1
        else:
            if cout > maxcount:
                maxcount = cout
            cout =1
    if cout > maxcount:
        maxcount = cout
print(maxcount)
#1111145111111