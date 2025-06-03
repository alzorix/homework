

DATA_other_citys = dict()

DATA_normal_citys = dict()
with open("../../homework1/files/26-85.txt") as file:
    kolvo_iacheek = int(file.readline().strip())
    list_seat = list()

    line = file.readline().strip()
    while line != "":
        row_number,row_seat,chauvinism = line.split(" ")
        row_seat = int(row_seat)
        row_number = int(row_number)



        #print(d,r)
        if chauvinism =="1":
            if row_number not in DATA_other_citys:
                DATA_other_citys[row_number] = {row_seat}
            else:
                DATA_other_citys[row_number].add(row_seat)
        else:
            if row_number not in DATA_normal_citys:
                DATA_normal_citys[row_number] = {row_seat}
            else:
                DATA_normal_citys[row_number].add(row_seat)




        line = file.readline().strip()

    #print(list_seat)





'''Найдите ряд с наибольшим номером, в котором есть ровно сто свободных мест подряд между участниками из других городов,
 а также хотя бы пятьсот мест, занятых участниками из города Н. Гарантируется, что есть хотя бы один ряд, удовлетворяющий этому условию.'''

def test(x,y,s):
    count = 0
    try:
        for i in DATA_normal_citys[s]:
            if x<i and i <y:
                count+=1

        return count
    except:
        return 0


list_good_one_ysl = list()

for s in DATA_other_citys:


    FLAG = True
    line = list(DATA_other_citys[s])
    line.sort()
    #print(line)

    for i in range(len(DATA_other_citys)-1):
        if abs(line[i]- line[i+1]) - test(line[i],line[i+1],s)  == 100:
            None
            #print(abs(line[i]- line[i-1]) -1)
        else:
            #print(abs(line[i]- line[i+1]))
            FLAG = False
    if FLAG:
        #print(s)
        list_good_one_ysl.append(s)

list_good_two_ysl = list()

for s in DATA_normal_citys:


    FLAG = True
    line = list(DATA_other_citys[s])
    line.sort()
    #print(line)

    for i in range(len(DATA_other_citys)-1):
        if abs(line[i]- line[i+1])  >= 500:

            print(abs(line[i]- line[i-1]) -1)
        else:
            print(abs(line[i]- line[i+1]))
            FLAG = False
    if FLAG:
        print(s)
        list_good_one_ysl.append(s)




print(list_good_two_ysl,list_good_one_ysl) #Оба пусты