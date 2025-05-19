data = list()
with open("27_B_21599.txt") as file:
    line = file.readline().strip()
    while line != "":
        x,y = map(float,map(lambda s: s.replace(",","."),line.split("\t")))
        data.append((x,y))
        line = file.readline().strip()
from math import sqrt
def d(p,p1):
    x,y = p
    x1,y1 = p1
    return sqrt((x-x1)**2 + (y - y1)**2)
# def get_cluster_A(p0):
#     x,y = p0
#     if y <-5:
#         return 0
#     elif y > 1.732*(x-12.5): #молимся,что это верные точки
#         return 1
#     else:
#         return 2
#
# cluster_1 = list()
# cluster_2 = list()
# cluster_0 = list()
#
#
#
# clusters = list()
# while len(data) !=0:
#     p0 = data.pop()
#     cluster = get_cluster_A(p0)
#     match cluster:
#         case 0: cluster_0.append(p0)
#         case 1: cluster_1.append(p0)
#         case 2: cluster_2.append(p0)
# print(len(cluster_0),len(cluster_1),len(cluster_2))
# clusters.append(cluster_1)
# clusters.append(cluster_2)
# clusters.append(cluster_0)
# Px = list()
# Py=list()
# def get_center(cluster):
#     m = []
#     for p0 in cluster:
#         s = sum(d(p0,p) for p in cluster)
#         m.append((s,p0))
#
#     x,y = min(m)[1]
#     Px.append(x)
#     Py.append(y)
#     return 1
#
# trash = [get_center(cluster) for cluster in clusters]
# print((sum(Px)*10_000/len(Px)),(sum(Py)*10_000/len(Py)))


#178755 2896

def get_cluster(p0):
    cluster = [p for p in data if d(p0,p)<1.5] #Посмотрите на график, он для Б,колесо придумывать не надо )
    if len(cluster) !=0:
        for p in cluster:
            data.remove(p)
        new_cluster = [get_cluster(p) for p in cluster]
        cluster += sum(new_cluster,[])
    return cluster
clusters = list()
while len(data) !=0:
    p0 = data.pop()
    cluster = get_cluster(p0) + [p0]
    clusters.append(cluster)
    print(len(cluster))
Fx = list()
Fy = list()
def get_centroid(cluster):
    m = []
    for p in cluster:
        s = sum(d(p,p1) for p1 in cluster)
        m.append((s,p))
    Fx.append(min(m)[1][0])
    Fy.append(min(m)[1][1])
    return 1
c = [get_centroid(cluster) for cluster in clusters]
print((sum(Fx)*10_000/len(Fx)),(sum(Fy)*10_000/len(Fy)))
#37392 50998