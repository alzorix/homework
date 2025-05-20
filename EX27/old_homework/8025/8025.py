data = list()
with open("B") as file:
    line = file.readline().strip()
    while line != "":
        corX,corY = line.split(" ")
        corX = float(str(corX).replace(",","."))
        corY = float(str(corY).replace(",","."))
        data.append((corX,corY))
        line = file.readline().strip()

from math import sqrt

def distance(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return sqrt(  (x2-x1)**2+   (y2-y1)**2   )


def get_cluster(p0):
    cluster = [p for p in data if distance(p0,p) < 1]
    if len(cluster)>0:
        for p in cluster:
            data.remove(p)
        next_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster,[])
    return cluster
clusters = list()

while len(data)>0:
    p0 = data.pop()
    cluster = [p0] + get_cluster(p0)
    clusters.append(cluster)
    print(len(cluster))

def get_centroid(cluster):
    x = list()
    y = list()

    for p0 in cluster:
        x.append(p0[0])
        y.append(p0[1])
    cr_x = sum(x) / len(x)
    cr_y = sum(y) / len(y)
    print(cr_y,cr_x)
    centroid = (cr_x,cr_y)

    # centroid = None
    # for p0 in cluster:
    #     if p0[0] ==cr_x:
    #         if p0[1] == cr_y:
    #             centroid = p0
    #
    # if centroid == None:
    #     raise SystemError

    return centroid
centroids = [get_centroid(cluster) for cluster in clusters]

x_centroids = list()
y_centroids = list()
for centroid in centroids:
    x = centroid[0]
    y = centroid[1]
    x_centroids.append(x)
    y_centroids.append(y)
print(sum(x_centroids)*10000//len(x_centroids),sum(y_centroids)*10000//len(y_centroids))
#31190 46669
#35259 61499