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

def T(s):
    return s >0 # Проверял модулем,хех. 0 Никто не отменял!

for ind in range(0,len(data)-1):
    x = data[ind]
    y = data[ind + 1]

    if T(x) or T(y): #Проверял зачем-то на чётность
        if x + y < c:
            ans.append(x**2+y**2)
print(len(ans),max(ans))
#4706 195643981

