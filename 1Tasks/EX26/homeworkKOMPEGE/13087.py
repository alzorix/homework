with open("26_13087.txt") as file:
    int_orders = int(file.readline().strip())

    line = file.readline().strip()
    orders = list()
    while line !="":
        start,end = line.split()
        orders.append((int(start),int(end)))
        line = file.readline().strip()

orders.sort(key = lambda x:x[1])

time = 0
times = 0
for i in range(len(orders)):
    if time <= orders[i][0]:
        times +=1
        past_time = time -20


        time = orders[i][1] + 20




orders.sort(key=lambda  x:x[0])
orders.reverse()
print(times,orders[0][0] - past_time)

#16 52 +