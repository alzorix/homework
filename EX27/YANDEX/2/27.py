data = list()
with open("27_A.txt") as file:
    line = file.readline().strip()
    while line !="":
        x,y = map(float,line.replace(",",".").split())
        data.append((x,y))
        line = file.readline().strip()

print(len(data))
from math import sqrt
def d(p,p0):
    x0,y0 = p0
    x,y = p
    return sqrt((x-x0)**2 + (y -y0)**2)

def get_cluster(p0):
    new_cluster= [p for p in data if d(p,p0) < 10]
    if len(new_cluster) != 0:
        for p in new_cluster:
            data.remove(p)
        cluster = [get_cluster(p) for p in new_cluster]
        new_cluster = new_cluster + sum(cluster,[])
    return new_cluster
clusters = list()
while len(data) !=0:
    p0 = data.pop()
    cluster = get_cluster(p0) + [p0]
    clusters.append(cluster)
    print(len(cluster))

def get_median(all_n:list):
    all_n.sort()
    dlina = len(all_n)
    if dlina % 2 ==0:
        t = dlina//2-1
        median = (all_n[t] + all_n[t+1])/2
    else:
        t = dlina //2
        median = all_n[t]
    return median

def get_q1(all_n:list()):
    res = get_median(all_n)

    new_list  = list()

    for n in all_n:
        if n < res:
            new_list.append(n)

    ans = get_median(new_list)
    return ans

def get_q3(all_n:list()):
    res = get_median(all_n)

    new_list = list()

    for n in all_n:
        if n > res:
            new_list.append(n)

    ans = get_median(new_list)
    return ans

VIBROS = 0
def clear(cluster):
    global VIBROS
    all_x = list()
    all_y = list()

    its_clear = list()

    for p in cluster:

        x,y = p
        all_x.append(x)
        all_y.append(y)

    q1x = get_q1(all_x)
    q1y = get_q1(all_y)
    q3x = get_q3(all_x)
    q3y = get_q3(all_y)

    IQR_X = q3x-q1x
    IQR_Y = q3y-q1y

    x_start = q1x - 1.5 * IQR_X
    x_end = q3x + 1.5 * IQR_X

    y_start = q1y - 1.5 * IQR_Y
    y_end = q3y + 1.5 * IQR_Y

    for p in cluster:

        x,y = p
        if x_start <= x <=x_end and y_start <= y <=y_end:
            its_clear.append(p)
        else:
            VIBROS +=1
    return its_clear


clear_clusters = [clear(cluster) for cluster in clusters]
print(clusters)
print(clear_clusters)
#похоже на правду


Is = list()

def get_I(clusters):

    for cluster in clusters:
        Future_I = list()
        for p0 in cluster:
            for p1 in cluster:
                if p0 != p1:
                    Future_I.append(d(p0,p1))

        I = sum(Future_I)/ len(Future_I)/len(cluster)
        Is.append(I) #судя по заданию кластер не нужен
get_I(clear_clusters)

print(VIBROS,max(Is)*100000)
#25 4061-
# 4061 - неверный ответ
#467 200-
# 200 - неверный ответ
