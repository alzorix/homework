data = list()
mins = list()
with open("17.txt") as file:
    line = file.readline().strip()
    while line !="":
        data.append(int(line))

        if len(str(abs(int(line)))) == 4:
            if int(line)%17==0:
                mins.append(int(line))


        line = file.readline().strip()

ysl_min = min(mins) ** 2


def ysl1(num):
    if len(str(abs(int(num)))) == 4:
        if str(num)[-2::] == "27":
            return True
    return False
ans = list()
for id in range(len(data)-2):
    fist= data[id]
    second = data[id+1]
    third = data[id+2]
    if ysl1(fist) or ysl1(second) or ysl1(third):
        fist2 = int(data[id]) **2
        second2 = int(data[id + 1]) **2
        third2 = int(data[id + 2]) **2
        if fist2 + second2 +third2 <= ysl_min:
            ans.append(abs(int(fist) )+ abs(int(second))+abs(int(third)))

print(len(ans),min(ans))

#78 4708