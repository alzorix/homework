

DATA = dict()



with open("../../homework1/files/26-110.txt") as file:
        N = file.readline().strip()  # кол-во точек
        line = file.readline().strip()
        while line != "":

            riad,raw = line.split()
            riad = int(riad)
            raw = int(raw)
            if riad in DATA:
                DATA[riad].add(raw)

            else:
                DATA[riad] = {raw}



            line = file.readline().strip()

        file.close()


DATA = dict(sorted(DATA.items()))
#print(DATA)


potantial_otvet = list()

for i in DATA:
    line = list(DATA[i])
    line.sort()
    count_line_bukv = 1


    for s in range(len(line)-1):

        temp = abs(line[s] - line[s-1]) -1

        if temp<=10:


            count_line_bukv = count_line_bukv+temp+1
        else:
            if count_line_bukv !=1:
                potantial_otvet.append((count_line_bukv,i))
                count_line_bukv =1
    if count_line_bukv != 1:
        potantial_otvet.append((count_line_bukv,i))
        count_line_bukv = 1






print(max(potantial_otvet)) #(10, 97635)
