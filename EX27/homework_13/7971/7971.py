from  math import sqrt
data = list()
def d(p1,p2):
    x1,y1 = p1
    x2, y2 = p2
    return sqrt((x2-x1)**2 + (y2-y1)**2)

with open("B") as file:
    line = file.readline().strip()

    while line != "":
        x,y = line.split("\t")
        x = float(x.replace(",", "."))
        y = float(y.replace(",", "."))
        data.append((x,y))
        line = file.readline().strip()
print(len(data))
def get_cluster(p0):
    cluster = [p for p in data if d(p0,p) <1]
    if len(cluster) > 0:
        for p in cluster:
            data.remove(p)
        new_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(new_cluster,[])
    return cluster
clusters = list()
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + get_cluster(p0)
    clusters.append(cluster)
    print(len(cluster))

def get_centroid(cluster):
    m = []
    for p in cluster:
        s = sum(d(p,p1) for p1 in cluster)
        m.append((s, p))
    return min(m)[1]

def get_radios(cluster):
        m = []
        p0 = get_centroid(cluster)
        for p in cluster:
            m.append(d(p0, p))
        return max(m)
radios = [get_radios(cluster) for cluster in clusters]
ans = list()

print(sum(radios)*10000//(len(radios)))

#27309 21686
