data = list()

with open("A") as file:
    line = file.readline().strip()
    while line !="":
        corX,corY = line.split("\t")
        corX = float(str(corX).replace(",","."))
        corY = float(str(corY).replace(",","."))
        data.append((corX,corY))
        line = file.readline().strip()

from math import sqrt
def dist(p1,p2):
    x1,y1 = p1
    x2,y2 = p2

    return sqrt(  (x1-x2)**2  + (y1-y2)**2  )

def get_cluster(p0):
    cluster = [p for p in data if dist(p,p0) < 1]
    if len(cluster) >0:
        for p in cluster:
            data.remove(p)
        next_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster,[])
    return cluster

clusters = list()
while len(data)>0:
    p0 = data.pop()
    cluster = [p0] + get_cluster(p0)
    #print(len(cluster))
    clusters.append(cluster)
def get_radios(cluster):
    m = []
    for p in cluster:
        s = sum(dist(p,p1) for p1 in cluster)
        m.append((s,p))
    return max(m)[1]

radios_gets = [get_radios(cluster) for cluster in clusters]


radios= list()

for centroid in radios_gets:
    x = centroid[0]
    y = centroid[1]
    radios.append(x)
    radios.append(y)


print(sum(radios)*10000//(len(radios)))
#18940.0
#Как найти центр кластера ?