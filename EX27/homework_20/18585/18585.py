data = list()

with open("B.txt") as file:

    R,K =  file.readline().strip().split(" ")
    line = file.readline().strip()

    while line != "":
        x,y,z = line.split(" ")
        x = float(x.replace(",","."))
        y = float(y.replace(",", "."))
        z = float(z.replace(",", "."))

        y = (y+z) / 2

        data.append((x,y))

        line = file.readline().strip()

from math import sqrt
def d(p,p1):

    x1,y1 = p
    x2,y2 = p1
    return sqrt((x2-x1)**2 + (y2-y1)**2)
def get_cluster(p0):
    cluster = [p for p in data if d(p,p0) <0.2]
    if len(cluster) > 0:
        for p in cluster:
            data.remove(p)
        new_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(new_cluster,[])
    return cluster

clusters = list()
while len(data) > 0 :
    p0 = data.pop()
    cluster = get_cluster(p0) + [p0]
    if len(cluster) >= int(K):
        clusters.append(cluster)
    print(len(cluster))

def get_metoid(cluster):
    m = []
    for p in cluster:
        ss = sum(d(p,p0) for p0 in cluster)
        m.append((ss,p))
    return min(m)[1]

metoids = [get_metoid(cluster) for cluster in clusters]
print(metoids)

Sx = list()
Sy = list()
for met in metoids:
    Sx.append(met[0])
    Sy.append(met[1])

print(int(sum(Sx)*100_000/len(Sx)) ,int(sum(Sy)*100_000/len(Sy)))
#728724 506096
#328813 419784