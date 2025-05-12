data = list()
with open("B") as file:
    line = file.readline().strip()
    while line !="":
        x, y = line.split(" ")
        x = float(x.replace(",", "."))
        y = float(y.replace(",", "."))
        data.append((x,y))
        line = file.readline().strip()

from math import sqrt
def d(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return sqrt((x2-x1)**2 + (y2-y1)**2)
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
def izolate_dot(cluster):
    cluster_edit = deepcopy(cluster)
    izolete_list = list()

    while len(cluster_edit) >0:
        p0 = cluster_edit.pop()
        dots = [p for p in cluster if d(p, p0) < 1]
        izolete_list.append((len(dots),p0[1],p0[0]))
    return min(izolete_list)

dots = [izolate_dot(clust)[2] for clust in clusters]
print(dots)
print(sum(dots) / len(dots) * 100000)
dots = [izolate_dot(clust)[1] for clust in clusters]

print(sum(dots) / len(dots) * 100000)
#135491 131265
#232818 15126