Iemzmei = list() # Произносится как Я ем змея,но задом наперёд: яемз...

maxx = list()
with open("17var03.txt") as sup:
    line = sup.readline().strip()
    while line != "":
        Iemzmei.append(int(line))
        #print(line[-2:])
        if line[-2:] == "90" :
            maxx.append(int(line))



        line = sup.readline().strip()
m = max(maxx)
print(m)
maxx.clear()

for i in range(len(Iemzmei)-2):
    if (len(str(abs(Iemzmei[i]))) ==4)or (len(str(abs(Iemzmei[i + 1]))) ==4)or (len(str(abs(Iemzmei[i+ 2]))) ==4):
        if Iemzmei[i]+Iemzmei[i + 1]+Iemzmei[i + 2]  >m:
            maxx.append(Iemzmei[i]+Iemzmei[i + 1]+Iemzmei[i + 2] )

print(len(maxx),min(maxx))
