data = list()
balli_vse = list()
with open("26_20815.txt") as file:
    N,K = map(int,file.readline().strip().split()) #K - места
    line = file.readline().strip()
    while line !="":
        ID,exam1,exam2,exam3,sobes = map(int,line.split())
        balli_vse.append((exam1+exam2+exam3+sobes))
        data.append((exam1+exam2+exam3+sobes,sobes,-ID))
        line = file.readline().strip()
data.sort(reverse=True)


otrid = list()

from copy import deepcopy
data_copy = deepcopy(data)

balli_otrid = list()
for _ in range(K):
    chel = data[0]
    data.remove(chel)

    otrid.append(chel)
    balli_otrid.append(chel[0])


ans1 = list()
polyprox = set()
for id_order in range(len(balli_otrid)):
    t = balli_otrid[id_order]
    if balli_otrid.count(t) == balli_vse.count(t):
        ans1.append(t)
    else:
        polyprox.add(t)
t = list(polyprox)[0]
#print(polyprox)
chelli_with_polyprox=0
for chellik in data_copy:
    if chellik[0] == t:
        chelli_with_polyprox+=1


ansewer_1 = list()
for x in otrid:
    balls,_,id = x
    if balls in ans1:
        ansewer_1.append((balls,-id))

print(chelli_with_polyprox)
print(ansewer_1.pop())
#45539 127