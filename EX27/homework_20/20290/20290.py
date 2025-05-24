data = list()
with open("27.6.A_20290.txt") as file:
    R = file.readline().strip()
    line = file.readline().strip()
    while line != "":
        x,y = map(float,map(lambda s: s.replace(",","."),line.split(" ")))
        data.append((x,y))
        line = file.readline().strip()
from math import sqrt
def d(p,p1):
    x,y = p
    x1,y1 = p1
    return sqrt((x-x1)**2 + (y - y1)**2)

def get_cluster(p0):
    cluster = [p for p in data if d(p0,p)<0.5]
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
s = list()
for m,l in enumerate(clusters):
    s.append((len(l),m))
clusters.pop(min(s)[1])
print(len(clusters))
print(clusters)
#Как расчитать координаты края?
x = list()
y = list()
def end_dot(cluster):
    ans = list()
    for other_cluster in clusters:
        if cluster != other_cluster:
            candidats = list()
            for other_dot in other_cluster:
                for our_dot in cluster:
                    candidats.append((d(our_dot,other_dot),our_dot))
            dot = min(candidats)[1]
            x.append(dot[0])
            y.append(dot[1])

            ans.append(min(candidats)[1])
    return ans

dots = [end_dot(cluster) for cluster in clusters]

print(sum(x)/len(x)*10_000,sum(y)/len(y)*10_000)
#37051.34281597505 -781.0933950960181
# Т.е. не верно