with open("26-107.txt") as file:
    L,N = file.readline().strip().split()
    line =  file.readline().strip()
    orders = list()

    while line !="":

        start,end = line.split()
        orders.append((int(end),int(start)))
        line = file.readline().strip()
    orders.sort()

    #Запишите в ответе два целых числа: наибольшее возможное количество вылетов и наименьшее возможное время вылета последнего рейса.
    time = 0
    count = 0
    for i in range(len(orders)):
        end,start = orders[i]
        if time <=start:
            last = time
            time = end
            count+=1


orders.sort(key=lambda  x:x[1])

for i in range(len(orders)):
    end, start = orders[i]
    if last <= start:
        last = start



print(count,last) # 50% 102 9980

