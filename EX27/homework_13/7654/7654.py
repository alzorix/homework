data = list()
with open("A") as file:
    line = file.readline().strip()

    while line !="":
        x,y,h = line.split("\t")
        x = float(str(x).replace(",","."))
        y = float(str(y).replace(",","."))
        h = float(h.replace(",", "."))
        data.append((x,y,h))


        line = file.readline().strip()
#print(data)
from  math import sqrt
def dist(p,p1):
    x2,y2,_ = p
    x1,y1,_ = p1
    return sqrt(  (x2-x1)**2  + (y2-y1) **2        )


def get_cluster(p0):
    cluster = [p for p in data if dist(p0,p)<30]
    if len(cluster)>0:
        for p in cluster:
            data.remove(p)
        new_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(new_cluster,[])
    return cluster

clusters = list()
while len(data) >0:
    p0 = data.pop()

    cluster = [p0] + get_cluster(p0)
    if len(cluster)>10:

        clusters.append(cluster)
        print(len(cluster))
def distPLUS(p,p1):
    x2,y2,center = p
    x1,y1,h1 = p1
    return sqrt((x2-x1)**2  + (y2-y1) **2) *h1

def get_center(cluster):
    m = []
    for p in cluster:
        s = sum(distPLUS(p,p1) for p1 in cluster)
        m.append((s,p))
    return min(m)[1]

centers = [get_center(cluster) for cluster in clusters]


x_centr = list()
y_centr = list()
for center in centers:
    x = center[0]
    y = center[1]
    x_centr.append(x)
    y_centr.append(y)

print(abs(sum(x_centr)*100000/len(x_centr)),abs(sum(y_centr)*100000/len(y_centr)))
#25667971 24175730
#1659383 1838931

#++