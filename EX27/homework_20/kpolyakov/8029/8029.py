data = list()
with open("B") as file:
    line = file.readline().strip()
    while line !="":
        x,y = line.split("\t")
        x = float(str(x).replace(",","."))
        y = float(str(y).replace(",","."))
        data.append((x,y))
        line = file.readline().strip()
from math import sqrt
def d(p,p1):
    x2,y2 = p
    x1,y1 = p1
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def get_cluster(p0):
    cluster = [p for p in data if d(p,p0) <0.57]
    if len(cluster)>0:
        for p in cluster:
            data.remove(p)
        new_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(new_cluster,[])
    return cluster
clusters = list()
while len(data) > 0:
    p0 = data.pop()
    cluster = get_cluster(p0) + [p0]
    if len(cluster) >20:
        clusters.append(cluster)
        print(len(cluster))


def get_centroid(cluster):
    m = []
    for p in cluster:
        s = sum(d(p,p1) for p1 in cluster)
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

print(sum(x_centroids)*100000//len(x_centroids),sum(y_centroids)*100000//len(y_centroids))
#650914 400449
#В Б  график представляет из себя 3 закрашенных круга,а вокруг них очень близка находится окружность. Тут необходима реализация с радиусом