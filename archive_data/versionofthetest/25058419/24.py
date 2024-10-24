
with open("24.txt") as file:
    line = file.readline().strip()
    file.close()
count = 1
maxx= 0
for lc in range(len(line)-1):
    if line[lc] + line[lc+1] == "**" or line[lc] + line[lc+1] == "++"or line[lc] + line[lc+1] == "*+"or line[lc] + line[lc+1] == "+*":
        count = 1
    else:
        count+=1
        if maxx <count:
            maxx = count
print(maxx)
#191