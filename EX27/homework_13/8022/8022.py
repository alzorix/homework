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
    cluster = [p for p in data if d(p,p0) <1]
    if len(cluster) > 0:
        for p in cluster:
            data.remove(p)
        new_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(new_cluster,[])
    return cluster
clusters = list()
while len(data) != 0:
    p0 = data.pop()
    cluster = [p0] + get_cluster(p0)
    clusters.append(cluster)
    print(len(cluster))

def get_dialogonale(cluster):
    candidats = list()
    for p0 in cluster:
        for p1 in cluster:
            candidats.append((d(p1,p0),p1,p0))

    max_diag = max(candidats)
    p1 = max_diag[1]
    p2 = max_diag[2]
    x1,y1 = p1
    x2, y2 = p2
    return ((x1,x2),(y1,y2))
Px = list()
Py = list()
for cluster in clusters:
    coordinates = get_dialogonale(cluster) #найдите точки, образующие диагонали всех кластеров
    Px.append(coordinates[0][0])
    Px.append(coordinates[0][1])
    Py.append(coordinates[1][0])
    Py.append(coordinates[1][1])
print(sum(Px) / len(Px) * 10_000,sum(Py) / len(Py) * 10_000)
#16730 48696
#23982 47539