data = list()
with open("B") as file:
    line = file.readline().strip()
    while line !="":

        x,y = line.split(" ")

        x = float(x.replace(",","."))
        y = float(y.replace(",","."))

        data.append((x,y))
        line = file.readline().strip(
        )

from math import sqrt

def d(p1,p2):

    x1,y1 = p1
    x2,y2 = p2
    return sqrt(  (x2-x1)**2 + (y2-y1)**2    )

def get_cluster(p0):
    cluster = [p for p in data if d(p,p0) <0.4]
    if len(cluster) >0:
        for p in cluster:
            data.remove(p)
        new_cluster  = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(new_cluster,[])
    return cluster
clusters = list()
while len(data)> 0:
    p0 = data.pop()
    cluster = get_cluster(p0) + [p0]
    clusters.append(cluster)
    print(len(cluster))

from copy import deepcopy
def P(cluster):
    counts = []
    for p0 in cluster:
        c = 0
        for p in cluster:
            if d(p, p0) <1 :
                c += 1
        counts.append(c)
    return sum(counts) / len(counts)

Ps = [P(clust) for clust in clusters ]
print(Ps)
print(min(Ps)*100_000,sum(Ps)/len(Ps)*100_000)
#5158000 9476083
#7604400 18899514