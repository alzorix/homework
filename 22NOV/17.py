c = 0
data = list()
with open("17.txt") as file:
    line = file.readline().strip()
    while line != "":
        if int(line) % 2 ==0:
            c+=1
        data.append(int(line))
        line = file.readline().strip()
ans = list()
for ind in range(0,len(data)-1):
    x = data[ind]
    y = data[ind + 1]
    if x % 2 ==0 or y % 2 ==0:
        if x + y < c:
            ans.append(x**2+y**2)
print(len(ans),max(ans))
#5331 195643981