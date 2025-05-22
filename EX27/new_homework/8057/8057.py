data =list()

with open("A") as file:
    line = file.readline().strip()
    while line != "":
        x,y = line.split(" ")
        x = float(str(x).replace(",","."))
        y = float(str(y).replace(",","."))
        data.append((x,y))
        line = file.readline().strip()
from math import sqrt


def d(p1,p0):
    x0,y0 = p0
    x1, y1 = p1
    return sqrt(   (x1-x0)**2 + (y1-y0)**2             )
def get_cluster(p0):
    cluster = [p for p in data if d(p0,p) < 1]
    if cluster != "":
        for p in cluster:
            data.remove(p)
        next_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster,[])
    return cluster
clusters = list()
while len(data) !=0:
    p0 = data.pop()
    cluster = [p0]+get_cluster(p0)
    clusters.append(cluster)

def centroid(cluster):
    m = list()
    for p0 in cluster:
        summ_p = sum(d(p0,p) for p in cluster)
        m.append((summ_p,p0))
    return min(m)[1]
centroids = [centroid(p) for p in clusters]

#если мы условно удаляем анамалии