#похожая ситуация с 8029
#как отфильтровать аномалию без костылей?
data = list()

with open("A") as file:
    line = file.readline().strip()
    while line !="":
        x,y = line.split("\t")
        x = float(str(x).replace(",","."))
        y = float(str(y).replace(",","."))
        data.append((x,y))
        line = file.readline().strip()
from math import sqrt
def d(p0,p):

    x1,y1 = p
    x2,y2 = p0
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