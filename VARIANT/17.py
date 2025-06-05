MIN_CHISLO_YSL = 100000000
data = list()
with open("17_21903.txt") as file:
    line =file.readline().strip()

    while line !="":
        if len(str(abs(int(line))))== 3:
            if line[-2::] == "15":
                MIN_CHISLO_YSL = min(MIN_CHISLO_YSL,int(line)**2)
        data.append(int(line))
        line = file.readline().strip()
ans = list()
for x in range(len(data)-2):
    fist = data[x]
    second = data[x+1]
    third = data[x+2]
    if (fist < 0 and second <0 and third<0) or (fist  > 0 and second  >0 and third >0) or (fist == 0 and second == 0 and third==0):
        if max(fist,second,third) * min(fist,second,third) > MIN_CHISLO_YSL:
            ans.append(max(fist,second,third) * min(fist,second,third))
print(len(ans),min(ans))
