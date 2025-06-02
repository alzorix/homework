data =list()

with open("B") as file:
    line = file.readline().strip()
    while line != "":
        x,y = line.split("\t")
        x = float(str(x).replace(",","."))
        y = float(str(y).replace(",","."))
        data.append((x,y))
        line = file.readline().strip()
from math import sqrt


def d(p1,p0):
    x0,y0 = p0
    x1, y1 = p1
    return sqrt(   (x1-x0)**2 + (y1-y0)**2             )
# def get_cluster(p0):
#     cluster = [p for p in data if d(p0,p) < 1]
#     if cluster != "":
#         for p in cluster:
#             data.remove(p)
#         next_cluster = [get_cluster(p) for p in cluster]
#         cluster = cluster + sum(next_cluster,[])
#     return cluster
cluster0 = list()
cluster1 = list()
cluster2 = list()
def get_cluster(p):
    x,y = p
    if (x-2)**2 + (y-3)**2 <= 9:
        return 0
    elif (x - 6) **2 +(y-10) **2  <= 9:
        return 1
    elif (x - 10)**2 + (y-3) **2  <= 9:
        return 2

clusters = list()
while len(data) !=0:
    p0 = data.pop()
    p = get_cluster(p0)
    match p:
        case 0:
            cluster0.append(p0)
        case 1:
            cluster1.append(p0)
        case 2:
            cluster2.append(p0)
clusters = [cluster0,cluster1,cluster2]
def centroid(cluster):
    m = list()
    for p0 in cluster:
        summ_p = sum(d(p0,p) for p in cluster)
        m.append((summ_p,p0))
    return min(m)[1]

centroids = [centroid(p) for p in clusters]

#если мы условно удаляем аномалии
x_centroids = list()
y_centroids = list()
for centroid in centroids:
    x = centroid[0]

    y = centroid[1]
    x_centroids.append(x)
    y_centroids.append(y)

print(sum(x_centroids)*100000//len(x_centroids),sum(y_centroids)*100000//len(y_centroids))
#622984 298914
#593420 532705