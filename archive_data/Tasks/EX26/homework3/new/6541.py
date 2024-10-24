



owner_data_humber_home = -float("inf")
owner_data_last_client = 0

with open(" 26-122.txt") as file:


    fline = file.readline().strip().split()

    int_appartamentsonline = int(fline[0])

    int_orders = int(fline[1])

    orders = list()

    appartaments = [(0,0)]*int_orders
    print(appartaments)




    line = file.readline().strip()
    ''' два целых числа: час заезда и час выезда, считая от начала сезона.'''
    while line !="":

        start,end = line.split()
        orders.append((int(start),int(end)))
        line = file.readline().strip()


    orders.sort()
    #print(orders)

    for order in orders:

        start,end = order


        for id_ap in range(len(appartaments)):
            #print(appartaments[id_ap])

            if  start > appartaments[id_ap][1]:
                appartaments[id_ap] = (start,end)
                owner_data_last_client = start



                if id_ap//int_appartamentsonline > owner_data_humber_home:
                    owner_data_humber_home = id_ap//int_appartamentsonline


                break

print(owner_data_last_client)

count_full_appartaments = 0
for x in appartaments:
    temp = owner_data_last_client+1

    if temp<= x[1]:
        count_full_appartaments+=1


print(owner_data_humber_home +1,count_full_appartaments) # 13.2 120 - Ответ верный
#14 120
