mm = -10000000000000
data = list()
with open("17_20005(1).txt") as file:
    line = file.readline().strip()

    while line !="":
        p = int(line)
        if len((str(abs(p)))) == 4:
            mm = max(mm,p)
        data.append(p)
        line = file.readline().strip()
ans = list()
for id in range(len(data)-1):
    q1 = data[id]
    q2 = data[id+1]
    if ((q1< mm) + (q2 <mm)) ==1:
        t = q1**2 + q2**2
        if str(t)[-2::] == "12":
            ans.append(q1**2 + q2**2)

print(len(ans),min(ans))
#38 191556612