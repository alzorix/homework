data = list()
with open("B") as file:
    line = file.readline().strip()
    while line != "":

        x,y = line.split("\t")
        x = float(x.replace(",","."))
        y = float(y.replace(",", "."))
        data.append((x,y))
        line = file.readline().strip()
from math import sqrt
def d(p,p1):
    x2,y2 = p
    x1,y1 = p1
    return sqrt((x2-x1)**2 + (y2-y1)**2)
def get_cluster_A(p0):
    x,y = p0
    if  y - 5 <0:
        return 4
    if x - 5 <0:
        return 2
    return 1

def get_cluster_B(p0):
    x,y = p0

    if x - 10 >0:
        if y - 10< 0:
            return 4
        elif  (y -10) / (x - 10) < 1:
            return 1
        return 0
    else:
        if (y -10) / (x - 10) < 1:
            return 2
        else:
            return 3




cluster_0 = list()


cluster_1 = list()
cluster_2 = list()
cluster_3 = list()
cluster_4 = list()
while len(data) > 0 :
    p0 = data.pop()
    number = get_cluster_B(p0)

    match number:
        case 1:
            cluster_1.append(p0)
        case 2:
            cluster_2.append(p0)
        case 3:
            cluster_3.append(p0)
        case 4:
            cluster_4.append(p0)
        case 0:
            cluster_0.append(p0)

clusters = list()
clusters.append(cluster_0)

clusters.append(cluster_1)
clusters.append(cluster_2)

clusters.append(cluster_3)
clusters.append(cluster_4)
print(len(cluster_0),len(cluster_1),len(cluster_2),len(cluster_3),len(cluster_4))

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

#532496 533164