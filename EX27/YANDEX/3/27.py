data = list()

with open("27_B.txt") as file:
    line = file.readline().strip()
    line = file.readline().strip()

    while line != "":

        x, y = map(float, line.replace(",", ".").split())
        data.append((x,y))


        line = file.readline().strip()
#print(data)
from math import sqrt
def d(p,p1):
    x,y = p
    x1, y1 = p1
    return sqrt((x1-x)**2  + (y1-y)**2)

def get_cluster(p0):
    cluster = [p for p in data if d(p,p0)<15]
    if len(cluster) != 0:
        for p in cluster:
            data.remove(p)
        cluster = cluster + sum([get_cluster(p) for p in cluster],[])
    return cluster
clusters = list()
while len(data) !=0:
    p0 = data.pop()
    cluster = get_cluster(p0) + [p0]
    #print(len(cluster))
    clusters.append((len(cluster),cluster))
#print(len(clusters))
clusters.sort(reverse=True)

clusters = [clusters[0][1],clusters[1][1]] #A
# clusters = [clusters[0][1],clusters[1][1],clusters[2][1]] #B

def P(cluster):
    dots = list()
    for p in cluster:
        for p1 in cluster:
            if p1 != p:
                dots.append(d(p,p1))
    SR_dist =sum(dots)/len(dots)
    MX_dist = max(dots)
    D = SR_dist/MX_dist
    return D

Ps = [P(cluster) for cluster in clusters]
print(int(min(Ps)*10_000), int(sum(Ps) / len(Ps)*10_000))
#2987 3330
