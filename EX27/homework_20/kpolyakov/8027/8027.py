data = list()

with open("B") as file:
    line = file.readline().strip()
    while line !="":
        x,y = line.split("\t")
        x = float(str(x).replace(",","."))
        y = float(str(y).replace(",","."))
        data.append((x,y))
        line = file.readline().strip()

from math import sqrt
def d(p,p1):

    x1,y1 = p
    x2,y2 = p1
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def get_cluster_A(p0):
    x,y = p0
    if x-8<0 and y-6<0:
        return 0
    elif y-6 >= x-8:
        return 1
    elif  y-6 < x-8:
        return 2
    else:
        print(p0)
def get_cluster_B(p0):
    x,y = p0


    if y-6 >= x-9:
        return 1
    elif  y-6 < x-9:
        return 2
    else:
        print(p0)



#всё равно выбивает else ,я не знаю почему


cluster_0 = list()
cluster_1 = list()
cluster_2 = list()
while len(data) != 0:
    p0 = data.pop()
    n = get_cluster_B(p0)
    match n:
        case 1 :
            cluster_1.append(p0)
        case 2 :
            cluster_2.append(p0)
        case 0 :
            cluster_0.append(p0)
clusters = list()
#clusters.append(cluster_0)
clusters.append(cluster_1)
clusters.append(cluster_2)

print(len(cluster_0),len(cluster_1),len(cluster_2))
Px = list()
Py=list()
def get_centroid(cluster):
    m = []
    for p in cluster:
        s = sum(d(p,p1) for p1 in cluster)
        m.append((s,p))
    return min(m)[1]
centroids = [get_centroid(cluster) for cluster in clusters]
for median in centroids:
    Px.append(median[0])
    Py.append(median[1])
print(sum(Px)*100000//len(Px),sum(Py)*100000//len(Py))
#808576 580719