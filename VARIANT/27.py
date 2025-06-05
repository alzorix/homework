data = list()
with open("27_B_21911.txt") as file:
    line = file.readline().strip()
    line = file.readline().strip()
    while line !="":
        x,y = map(float,line.replace(",",".").split())
        data.append((x,y))


        line = file.readline().strip()
from math import sqrt
def d(p,p1):
    x,y = p
    x1,y1 = p1

    return sqrt( (x1-x)**2+ (y1-y)**2 )
#Это для Б:
def get_cluster(p0):
    cluster = [p for p in data if d(p,p0)<5]
    if len(cluster) != 0:
        for p in cluster:
            data.remove(p)

        new_cluster = [get_cluster(p) for p in cluster]

        cluster = cluster + sum(new_cluster,[])
    return cluster
clusters = list()
while len(data) != 0:
    p = data.pop()
    cluster = get_cluster(p) + [p]
    print(len(cluster))
    clusters.append(cluster)

# def get_cluster_A(p0):
#     x,y = p0
#     if y > 2:
#         return 0
#     else:
#         return 1
# clusters = list()
# cluster_1 = list()
# cluster_0 = list()
# while len(data) != 0:
#     p = data.pop()
#     r = get_cluster_A(p)
#     match r:
#         case 0:
#             cluster_0.append(p)
#         case 1:
#             cluster_1.append(p)
# clusters = [cluster_0,cluster_1]

print(len(clusters))
x_centr = list()
y_centr = list()
def get_center(cluster):
    candidats = list()
    for p in cluster:
        s = sum(d(p,p1) for p1 in cluster)
        candidats.append((s,p))
    ans= min(candidats)[1]
    x_centr.append(ans[0])
    y_centr.append(ans[1])
    return ans
centroids = [get_center(cluster)  for cluster in clusters ]


print(sum(x_centr)*10_000 / len(x_centr),sum(y_centr)*10_000/len(y_centr))
#26216 24182
#150891 63754