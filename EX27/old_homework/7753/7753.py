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

    return sqrt(  (x2-x1)**2 +  (y2-y1)**  2     )

def get_cluster(p0):


    cluster = [p for p in data if dist(p,p0)<1]

    if len(cluster) >0:
        for x in cluster:
            data.remove(x)
        new_clusters = [ get_cluster(p) for p in cluster ]
        cluster = cluster + sum(new_clusters,[])
    return cluster
clusters = list()
while len(data) !=0 :
    p0 = data.pop()
    cluster = [p0] + get_cluster(p0)
    clusters.append(cluster)
    #print(len(cluster))

clusters = [ cluster for cluster in clusters if len(cluster) >=30  ] #убираем аномалии
print(len(clusters))

def get_centroid(cluster):
    m = []
    for p0 in cluster:
        d = sum(dist(p0,p) for p in cluster)

        m.append((d,p0))
    return min(m)[1]

centroids = [get_centroid(cluster) for cluster in clusters]
X_centroids = list()
Y_centroids = list()
for centroid in centroids:
    X,Y = centroid
    X_centroids.append(X)
    Y_centroids.append(Y)

print(sum(X_centroids) / len(X_centroids)*10_000,sum(Y_centroids) / len(Y_centroids)*10_000)
#39723 45534




