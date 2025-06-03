data = list()
with open("27_A.txt") as file:
    line = file.readline().strip()
    while line !="":
        x,y = map(float,line.replace(",",".").split())
        data.append((x,y))
        line = file.readline().strip()
print(len(data))
x_m = 0
y_m = 0
for p in data:
    x,y = p
    x_m = max(x_m,x)
    y_m = max(y_m, y)
x_m = int(x_m)+1
y_m = int(y_m)+1
count_boxes = x_m*y_m

clusters = [[[] for x in range(y_m)] for x in range(x_m)]

def add_cluster(p0):
    x,y = p0
    x = int(x)
    y = int(y)
    clusters[x][y].append(p0)

from copy import deepcopy
data_copy = deepcopy(data)

while len(data) !=0:
    p0 = data.pop()
    add_cluster(p0)

def get_sosed(cluster_coordinates):

    sosedi = []
    x, y = cluster_coordinates
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for sx, sy in directions:
        nx = x + sx
        ny = y + sy
        if 0 <= nx < x_m and 0 <= ny < y_m:
            sosedi.append((nx, ny))
    return sosedi


from math import sqrt


def d(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)


def its_social(p0):
    c = 0
    for p in data_copy:
        if p != p0:
            if d(p, p0) < 0.1:
                c += 1
    if c >= 14:
        return True
    else:
        return False


#A:
max_points = 0
best_pair = None
for x in range(x_m):
    for y in range(y_m):
        cluster = clusters[x][y]
        sosedi = get_sosed((x,y))

        for sx,sy in sosedi:
            sosed_animal = len(clusters[sx][sy])
            all_animal = len(cluster) + sosed_animal
            if all_animal > max_points:
                max_points = all_animal
                best_pair = ((x,y),(sx,sy))
print(best_pair)

all_best_pair = []
x = best_pair[0][0]
y = best_pair[0][1]
all_best_pair.extend(clusters[x][y])
x = best_pair[1][0]
y = best_pair[1][1]
all_best_pair.extend(clusters[x][y])
print(all_best_pair)
S = 0
K = 0
for p in all_best_pair:
    if its_social(p):
        S+=1
    else:
        K+=1
print(S,K)

#B
# max_points = 0
# best_pair = None
# for x in range(x_m):
#     for y in range(y_m):
#         cluster = clusters[x][y]
#         sosedi = get_sosed((x,y))
#
#         for sosed  in sosedi:
#             sx, sy = sosed
#
#             for sosed2 in sosedi:
#                 if sosed != sosed2:
#                     sx2, sy2 = sosed2
#
#
#                     sosed_animal = len(clusters[sx][sy])
#                     sosed2_animal = len(clusters[sx2][sy2])
#                     all_animal = len(cluster) + sosed_animal + sosed2_animal
#                     if all_animal > max_points:
#                         max_points = all_animal
#                         best_pair = ((x,y),(sx,sy),(sx2,sy2))
# print(best_pair)

# all_best_pair = []
# x = best_pair[0][0]
# y = best_pair[0][1]
# all_best_pair.extend(clusters[x][y])
# x = best_pair[1][0]
# y = best_pair[1][1]
# all_best_pair.extend(clusters[x][y])
# x = best_pair[2][0]
# y = best_pair[2][1]
# all_best_pair.extend(clusters[x][y])
# print(all_best_pair)
# S = 0
# K = 0
# for p in all_best_pair:
#     if its_social(p):
#         S+=1
#     else:
#         K+=1
# print(S,K)
#Суммарно потратил примерно час на это задание

#104 453
#2156  158