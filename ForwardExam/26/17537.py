with open("26_17537.txt") as file:
    N,rids,mests = map(int,file.readline().strip().split())
    line = file.readline().strip()
    data = [rids]*mests
    while line !="":
        rid,mest = map(int,line.split())

        data[mest-1] = min(rid,data[mest-1])
        line = file.readline().strip()
ans_rid = 0
ans_mesto = 0
for x in range(1,mests):
    para = min(data[x],data[x-1])-1
    if para >= ans_rid:
        ans_rid = para
        ans_mesto = x+1
print(ans_rid,ans_mesto)
#9991 5643
