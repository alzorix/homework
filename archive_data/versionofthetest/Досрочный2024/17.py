Im = list()

minimum = list()
with open("17.txt") as sup:
    line = sup.readline().strip()
    while line != "":
        iline = int(line)
        Im.append(iline)
        #print(line[-2:])
        if iline % 19 == 0:
            minimum.append(iline)



        line = sup.readline().strip()
m = min(minimum)
minimum.clear()
s = list()
for i in range(len(Im)-1):
    if ( Im[i] > m) or ( Im[i+1] > m):
        s.append(Im[i] + Im[i+1])



print(len(s),max(s))
