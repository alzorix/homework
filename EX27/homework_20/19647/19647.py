data = list()
with open("TRSW5sKIB.txt") as file:
    R = file.readline().strip()
    line = file.readline().strip()
    while line != "":

        x,y = map(float,map(lambda s: s.replace(",","."),line.split(" ")))
        data.append((x,y))
        line = file.readline().strip()
from copy import deepcopy
dataPLUS = deepcopy(data)
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

def get_centroid(cluster):
    m = []
    for p in cluster:
        s = sum(d(p,p1) for p1 in cluster)
        m.append((s,p))
    return min(m)[1]
centroids = [get_centroid(cluster) for cluster in clusters]

def get_transform(centroids):
    m = []
    for p in dataPLUS:
        s = sum(d(p,p_centroid) for p_centroid in centroids )
        #print(s)
        m.append((s,p))
    return min(m)[1]
p,s = get_transform(centroids)
print(p*10_000,s*10_000)
#23392.0 26711.999999999996
#В первой строке: ближайшие целые числа значений произведения - >
#23392 26712

#101946.99999999999 210484.0
#101947 210484