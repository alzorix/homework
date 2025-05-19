data = list()

with open("B") as file:
    line = file.readline().strip()

    while line !="":
        x,y = line.split(" ")
        x = float(str(x).replace(",","."))
        y = float(str(y).replace(",","."))
        data.append((x,y))
        line = file.readline().strip()


from math import sqrt
def d(p,p1):
    x2,y2 = p
    x1,y1 = p1
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def get_cluster(p0):
    cluster = [p for p in data if d(p,p0) <1]
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
    clusters.append(cluster)
    print(len(cluster))

def dot(cluster): #возвращает крайние точки кластера
    dots = list()
    for other_cluster in clusters:
        if other_cluster != cluster:
            candidats = list()
            for candidat in cluster:
                for p in other_cluster:
                    candidats.append((d(candidat,p),candidat))
            dots.append(min(candidats)[1])
    return dots

global_dots = [dot(cluster) for cluster in clusters]
print(global_dots)


x_dots = list()
y_dots = list()
for dots in global_dots:
    for dot in dots:


        x = dot[0]
        y = dot[1]
        x_dots.append(x)
        y_dots.append(y)

print(sum(x_dots)*10_000//len(x_dots),sum(y_dots)*10_000//len(y_dots))
#51428 45632
#28289 38015