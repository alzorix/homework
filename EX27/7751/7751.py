data = list()
with open("A.txt") as file:
    line = file.readline().strip()

    while line != "":
        corX,corY = line.split("\t")
        corX = float(str(corX).replace(",","."))
        corY = float(str(corY).replace(",","."))

        data.append((corX,corY))
        line = file.readline().strip()
print(data)

#Раст меж двумя точками
from math import sqrt
def dsinanse(x1,y1,x2,y2):

    return sqrt((x1-x2)**2 + (y1-y2)**2)