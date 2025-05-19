data = list()
with open("27B_19782.txt") as file:
    R = file.readline().strip()
    line = file.readline().strip()
    while line != "":
        x,y = map(float,map(lambda s: s.replace(",","."),line.split(" ")))
        data.append((x,y))
        line = file.readline().strip()
from math import sqrt
def d(p,p1):
    x,y = p
    x1,y1 = p1
    return sqrt((x-x1)**2 + (y - y1)**2)

def get_cluster(p0):
    cluster = [p for p in data if d(p0,p)<0.5]
    if len(cluster) !=0:
        for p in cluster:
            data.remove(p)
        new_cluster = [get_cluster(p) for p in cluster]
        cluster += sum(new_cluster,[])
    return cluster
clusters = list()
while len(data) !=0:
    p0 = data.pop()
    cluster = get_cluster(p0) + [p0]
    clusters.append(cluster)
    print(len(cluster))

def get_radious(cluster):
    m = []
    for p in cluster:
        s = sum(d(p,p1) for p1 in cluster)
        m.append((s,p))
    R_c = min(m)[1]
    m.clear()
    for p in cluster:
        s = d(p,R_c)
        m.append(s)
    return max(m)
radious = [get_radious(cluster) for cluster in clusters]

print(min(radious)*10_000,max(radious)*10_000)
#9428 12578

#5255 17314