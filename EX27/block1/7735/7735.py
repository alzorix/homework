data = list()

with open("A") as file:
    line = file.readline().strip()

    while line !="":
        x,y = line.split("\t")
        x = float(str(x).replace(",","."))
        y = float(str(y).replace(",","."))
        data.append((x,y))
        line = file.readline().strip()

#print(data)

from math import sqrt
def d(p,p1):
    x2,y2 = p
    x1,y1 = p1
    return sqrt((x2-x1)**2  + (y2-y1) **2)

def get_cluster(p0):
    cluster = [p for p in data if d(p,p0) <1]
    if len(cluster) > 0:
        for p in cluster:
            data.remove(p)
        new_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(new_cluster,[])
    return cluster

clusters = list()
while len(data) > 0 :
    p0 = data.pop()
    cluster = get_cluster(p0) + [p0]
    if len(cluster) >=30:
        clusters.append(cluster)
        print(len(cluster))

def get_center(cluster):
    m = []
    for p in cluster:
        s = sum(d(p,p1) for p1 in cluster)
        m.append((s,p))
    return min(m)[1]
centers = [get_center(cluster) for cluster in clusters ]
x_center = list()
y_center = list()
for center in centers:
    x = center[0]
    y = center[1]
    x_center.append(x)
    y_center.append(y)
print(sum(x_center)*100000 / len(x_center),sum(y_center)*100000/len(y_center))
#422710 715407
#653692 473162