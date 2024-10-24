with open("2623") as f:
    line = f.readline().strip().split()
    storage = int(line[0])
    users_data = list()
    line = f.readline().strip()
    while line !="":
        users_data.append(int(line))
        line = f.readline().strip()


    balance = storage
    users_data.sort()
    index =0


    good = list()
    while True:
        if users_data[index] <= balance:
            balance = balance - users_data[index]
            good.append(users_data[index])
            index +=1
        else:
            break
    users_data.reverse()
    f = 0
    mgood = max(good) +balance
    for i in users_data:
        if  f < i and mgood>=i:
            f = i
            break

print(len(good),f)#2373 67 +
