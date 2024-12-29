database = list()
database_for_idiots = list()
with open("26.txt") as file:
    trash_data = file.readline().strip()
    nice_data = int(int(trash_data) * 0.20)
    line = file.readline().strip()
    while line != "":
        ID,t1,t2,t3,t4 = line.split()
        sr_arifm = int(t1)+int(t2)+int(t3)+int(t4) / 4
        l = (t1+t2+t3+t4).count("1")
        if l ==0:
            database.append((-sr_arifm, ID, (t1, t2, t3, t4)))
        else:
            database_for_idiots.append((l,ID))

        line = file.readline().strip()

database.sort()
database_for_idiots.sort()

good_id = database[nice_data-1][1]

for x in range(len(database_for_idiots)):


    if int(database_for_idiots[x][0]) >1:
        print(good_id,database_for_idiots[x][1])
        exit()

