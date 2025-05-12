data = list()

with open("B") as file:
    line = file.readline().strip()

    while line !="":
        x,y = line.split("\t")
        x = float(str(x).replace(",","."))

        y = float(str(y).replace(",","."))
        data.append((x,y))
        line = file.readline().strip()

#print(data)


def dist(p1,p2):
    x1,y1 = p1
    x2,y2 = p2

    return max(abs(x2-x1) , abs(y2-y1))

def get_cluster(p0):
    cluster = [p for p in data if dist(p,p0) <0.5]
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
    print(len(cluster))
    clusters.append(cluster)
print(len(clusters))

def get_centroid(cluster):
    m = []
    for p in cluster:
        s = sum(dist(p,p1) for p1 in cluster)
        m.append((s,p))
    return min(m)[1]
centroids = [get_centroid(cluster)  for cluster in clusters ]
x_centr = list()
y_centr = list()
for center in centroids:
    x = center[0]
    y = center[1]
    x_centr.append(x)
    y_centr.append(y)
print(sum(x_centr)*10_000 // len(x_centr),sum(y_centr)*10_000//len(y_centr))
#26521 53559

#14678 -9311
#ответ у файла Б неверный
