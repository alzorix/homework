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
def S(cluster):
    cluster_edit = deepcopy(cluster)
    SR_S_list = list()

    while len(cluster_edit) >0:
        p0 = cluster_edit.pop()
        x = [d(p0,p) for p in cluster_edit]
        for x1 in x:
            SR_S_list.append(x1)
    return sum(SR_S_list) / len(SR_S_list)

Ss = [S(clust) for clust in clusters]
print(Ss)

print(min(Ss) * 100000,max(Ss) * 100000)
#79724 158994
#205908 237869