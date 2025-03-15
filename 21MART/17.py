data = list()

chetchik = 0
with open("17.txt") as file:
    line = file.readline().strip()
    while line != "":
        if int(line)% 32 ==0:
            chetchik+=1
        data.append(int(line))
        line = file.readline().strip()
ans = list()
def ysl(num):
    return abs(num) != num

for id in range(len(data)-1):
    chisl1= data[id]
    chisl2 = data[id+1]

    if chisl1+chisl2<chetchik:
        if ysl(chisl1) or chisl2:
            ans.append(chisl1+chisl2)
print(len(ans),max(ans))