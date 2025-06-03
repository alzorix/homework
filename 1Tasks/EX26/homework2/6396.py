all_time = list()
with open("26-117.txt") as file:
    fist_line = file.readline().strip().split(" ")

    kolvo_rooms = int(fist_line[0])
    orders_kolvo = int(fist_line[1])








    data_orders= list()

    line = file.readline().strip()
    while line != "":
        start_time,end_time = line.split(" ")

        data_orders.append((int(start_time),int(end_time)))
        line = file.readline().strip()

    data_orders.sort()


    rooms = list()
    for  a in range(kolvo_rooms):
        rooms.append(0)

    for i in range(orders_kolvo):

        start,end = data_orders[i]
        m = min(rooms)

        for x in range(len(rooms) - 1, -1, -1):

            if m <=end:

                if rooms[x] ==m:
                    if start <= 10080:
                        if m!=0:
                            all_time.append(m - start)

                        last_client = x
                    rooms[x] = 30 +end+1
                    break

            #
            #
            # if rooms[s] <= start:
            #
            #
            #
            #     rooms[s] = end +30+1
            #     if start <=10080:
            #         last_client =s
            #     break
            #
            #



        # else:
        #
        #     m = min(rooms)
        #     if m <=end:
        #
        #
        #         for x in range(len(rooms)-1,-1,-1):
        #             if rooms[x] ==m:
        #                 if start <= 10080:
        #                     all_time.append(m - start)
        #
        #                     last_client = x
        #                 rooms[x] = 30 +end+1
        #                 break
print(max(all_time),last_client+1,) #50% : 79 30



