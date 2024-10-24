
test = 0

with open("26-128.txt") as file:
    ''' Первая строка входного файла содержит натуральное число N (1 ≤ N ≤ 1000) – количество заявок на проведение мероприятий.'''
    int_orders = int(file.readline().strip())
    line = file.readline().strip()


    orders = list()
    while line !="":
        start,end = line.split()

        orders.append((int(start),int(end)))
        line = file.readline().strip()

    orders.sort(key= lambda x:x[1])
    time_end =0
    count = 0
    print(orders)

    for i in range(len(orders)):
        if orders[i][0] >= time_end:
            last_time = time_end
            time_end = orders[i][1]
            s = time_end
            if int(time_end) > test:
                test = int(end)

            count+=1



orders.sort()
orders.reverse()

for i in range(len(orders)):
    if orders[i][0] >= last_time:
        time_end = orders[i][1]


print(count,time_end)#16 1345

