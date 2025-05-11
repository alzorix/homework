data = list()
with open("B") as file:
    line = file.readline().strip()

    while line!="":
        corX,corY = line.split("\t")
        corX = float(str(corX).replace(",","."))
        corY = float(str(corY).replace(",","."))
        data.append((corX,corY))
        line = file.readline().strip()

from math import sqrt

def distance(p1,p2):
    x1,y1 = p1
    x2, y2 = p2
    return sqrt( (x2-x1)**2 + (y2-y1)**2)

def get_cluster(p0):
    cluster = [p for p in data if distance(p0,p) <1]
    if len(cluster)>0:
        for p in cluster:
            data.remove(p)
        next_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster,[])
    return cluster
clusters = list()
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + get_cluster(p0)
    clusters.append( cluster)

def get_centroid(cluster):
    m = []
    for p in cluster:
        s = sum(distance(p,p1) for p1 in cluster)
        m.append((s,p))
    return min(m)[1]
centroids = [get_centroid(cluster) for cluster in clusters]
x_centroids = list()
y_centroids = list()
for centroid in centroids:
    x = centroid[0]
    y = centroid[1]
    x_centroids.append(x)
    y_centroids.append(y)

print(sum(x_centroids)*10000//len(x_centroids),sum(y_centroids)*10000//len(y_centroids))
#14394 35648
#25130 43931