data = list()
with open("") as file:
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
s = list()
for m,l in enumerate(clusters):
    s.append((l,m))
clusters.pop(min(s)[1])
#Как расчитать координаты края?