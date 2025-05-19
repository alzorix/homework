data = list()
with open("27B_18622.txt") as file:
    line = file.readline().strip()
    while line !="":
        x,y = line.split(" ")
        x = float(x.replace(",","."))
        y = float(y.replace(",", "."))

        data.append((x,y))
        line = file.readline().strip()
from math import sqrt
def d(p1,p0):
    x0,y0 = p0
    x1,y1 = p1
    return sqrt((x1 - x0) **2 + (y1 - y0) **2)



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

t = list()
for n,cluster in enumerate(clusters):
    t.append((len(cluster),n))
clusters.pop(max(t)[1])




def get_centroid(cluster):
    m = []
    for p in cluster:
        s = sum(d(p,p1) for p1 in cluster)
        m.append((s,p))
    return min(m)[1]
centroids = [get_centroid(cluster) for cluster in clusters]

Sx = list()
Sy = list()
for centroid in centroids:
    Sx.append(centroid[0])
    Sy.append(centroid[1])

print(int(sum(Sx)*10_000/len(Sx)) ,int(sum(Sy)*10_000/len(Sy)))
#4597 23685
#25450 24994