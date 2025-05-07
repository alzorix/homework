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
