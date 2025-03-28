database = list()
with open("26_20815.txt") as f:
    fdata = f.readline().strip()
    kandidats,mesta = fdata.split()
    fdata = f.readline().strip()
    while fdata !="":
        ID,a1,a2,a3,sobec = fdata.split()
        balls = int(a1)+int(a2)+int(a3)

        database.append((balls + int(sobec),int(sobec),-int(ID),balls))
        fdata = f.readline().strip()


database.sort(reverse=True)


search = database[int(mesta)-1][0]
#достаём кол-во баллов ,которое может может быть проходным или полупроходным
print(search)

search1 = database[int(mesta)][0]
print(search1)
#Если серч = серч1 значит полупроходной,в противном серч проходной ,а полупроходного нет

for s in range(int(mesta)-1,-1,-1):
    if database[s][0] != search:
        print(database[s])
        real_prohod =-database[s][3]
        break
c = 0
for x in database:
    if x[0] == search:
        c+=1
print(c)


