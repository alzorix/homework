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

    x1,y1 = p
    x2,y2 = p1
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

X_medians = list()
Y_medians = list()

def get_medians(cluster):
    X_MEDIAN = None
    #X - ZONE
    for x_candidat in cluster:
        count_more = 0
        count_less = 0
        x_candidat_x = x_candidat[0]
        for test_p in cluster:
            if x_candidat != test_p:
                x_test = test_p[0]
                if x_candidat_x > x_test:
                    count_less+=1
                if x_candidat_x < x_test:
                    count_more +=1
                if x_candidat_x ==x_test:
                    None
        if count_less == count_more:
            X_MEDIAN = x_candidat_x
            break
    if X_MEDIAN == None:
        raise RuntimeError
    Y_MEDIAN = None
    #Y - ZONE
    for Y_candidat in cluster:
        count_more = 0
        count_less = 0
        Y_candidat_Y = Y_candidat[1]
        for test_p in cluster:
            if Y_candidat != test_p:
                Y_test = test_p[1]
                if Y_candidat_Y > Y_test:
                    count_less+=1
                if Y_candidat_Y < Y_test:
                    count_more +=1
                if Y_candidat_Y ==Y_test:
                    None
        if count_less == count_more:
            Y_MEDIAN = Y_candidat_Y
            break
    if Y_MEDIAN == None:
        raise RuntimeError
    return ((X_MEDIAN,Y_MEDIAN))

medians = [get_medians(cluster) for cluster in clusters]
print(medians)

Px = list()
Py=list()

for median in medians:
    Px.append(median[0])
    Py.append(median[1])
print(sum(Px)*10000//len(Px),sum(Py)*10000//len(Py))
#40893 9686