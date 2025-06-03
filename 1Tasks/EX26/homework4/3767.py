with open("26-51.txt") as file:
    N = int(file.readline().strip())
    data = list()
    line = file.readline().strip()
    while line !="":
        data.append(int(line))
        line = file.readline().strip()
    data.sort()
    min = data[0:100]
    count=0
    c =0

    ans = list()
    for i in range(len(data)):
        for i2 in range(len(data)):
            if (i +i2)%2 ==0:
                ans.append(i +i2)
                count+=1
sr = max(ans)//2
print(count,c,sr)
