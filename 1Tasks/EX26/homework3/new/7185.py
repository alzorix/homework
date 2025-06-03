with open("26-142.txt") as file:
    intorders = file.readline().strip()

    line = file.readline().strip()
    orders = list()
    while line !="":
        start,end = line.split()
        start = int(start)
        end = int(end)
        orders.append((start,end))
        line = file.readline().strip()

    orders.sort(key=lambda x:x[1])

    time = 0
    count =0
    maxxx = -float("inf")

    conf = 0
    last_conf = 0


    for data in orders:
        start,end = data
        if start >= conf:
            last_conf = conf-10

            conf = end +10
            count+=1

orders.sort()

orders.reverse()


print(count,orders[0][0] - last_conf) #64 27 ++++


